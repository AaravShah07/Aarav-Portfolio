"""Check the site's files without a browser.

Usage: python tools/check_site.py            Check links and structure
       python tools/check_site.py --publish  Also fail on anything not ready to publish

Checks exact-case links and anchors, root-relative paths, image alt text and
dimensions, page titles, heading order, and duplicate IDs. With --publish, it
also fails on content markers, the draft banner, image placeholders, and tracking scripts.
"""
import html.parser
import pathlib
import re
import sys
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = [ROOT / "index.html", ROOT / "about.html", *sorted((ROOT / "projects").glob("*.html"))]
PUBLISH_MODE = "--publish" in sys.argv
TRACKERS = re.compile(r"googletagmanager|google-analytics|hotjar|segment\.com|plausible|clarity\.ms", re.I)


class Page(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids, self.refs, self.headings, self.images = [], [], [], []
        self.title = ""
        self._in_title = False
        self.classes = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        self.classes += (attrs.get("class") or "").split()
        for key in ("href", "src"):
            if attrs.get(key):
                self.refs.append(attrs[key])
        if re.fullmatch(r"h[1-6]", tag):
            self.headings.append(int(tag[1]))
        if tag == "img":
            self.images.append(attrs)
        if tag == "title":
            self._in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data


def exists_exact_case(path):
    """Compare every path segment exactly, because Windows ignores case."""
    if not path.exists():
        return False
    current = ROOT
    for part in path.relative_to(ROOT).parts:
        if part not in {entry.name for entry in current.iterdir()}:
            return False
        current = current / part
    return True


def main():
    parsed = {}
    for page in PAGES:
        parser = Page()
        parser.feed(page.read_text(encoding="utf-8"))
        parsed[page.resolve()] = parser

    errors = []
    checked = 0
    for page, data in parsed.items():
        name = page.relative_to(ROOT).as_posix()
        source = page.read_text(encoding="utf-8")

        if not data.title.strip():
            errors.append(f"{name}: missing title")
        if '<html lang="' not in source:
            errors.append(f"{name}: missing page language")
        if 'name="description"' not in source:
            errors.append(f"{name}: missing meta description")
        if 'name="viewport"' not in source:
            errors.append(f"{name}: missing viewport")
        if data.headings.count(1) != 1:
            errors.append(f"{name}: expected one h1, found {data.headings.count(1)}")
        for before, after in zip(data.headings, data.headings[1:]):
            if after > before + 1:
                errors.append(f"{name}: heading jumps from h{before} to h{after}")
        for duplicate in {i for i in data.ids if data.ids.count(i) > 1}:
            errors.append(f"{name}: duplicate id '{duplicate}'")
        for image in data.images:
            label = image.get("src", "?")
            if "alt" not in image:
                errors.append(f"{name}: image without alt: {label}")
            if not (image.get("width") and image.get("height")):
                errors.append(f"{name}: image without dimensions: {label}")

        for ref in data.refs:
            parts = urllib.parse.urlsplit(ref)
            if parts.scheme or parts.netloc:
                continue
            if ref.startswith("/"):
                errors.append(f"{name}: root-relative path: {ref}")
                continue
            checked += 1
            target = (page.parent / urllib.parse.unquote(parts.path)).resolve() if parts.path else page
            if not exists_exact_case(target):
                errors.append(f"{name}: missing or wrong-case target: {ref}")
                continue
            if parts.fragment and target in parsed and parts.fragment not in parsed[target].ids:
                errors.append(f"{name}: missing anchor: {ref}")

        if PUBLISH_MODE:
            markers = source.count("NEEDS MY INPUT")
            if markers:
                errors.append(f"{name}: {markers} [NEEDS MY INPUT] marker(s)")
            if "draft-banner" in data.classes:
                errors.append(f"{name}: draft banner still present")
            placeholders = data.classes.count("image-placeholder")
            if placeholders:
                errors.append(f"{name}: {placeholders} image placeholder(s)")
            if TRACKERS.search(source):
                errors.append(f"{name}: possible tracking script")

    for message in errors:
        print("FAIL", message)
    print(f"{len(PAGES)} pages, {checked} internal references, {len(errors)} problem(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
