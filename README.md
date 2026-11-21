# Aarav Shah: Engineering Portfolio

A personal mechanical engineering portfolio, built as a static site with HTML, CSS, and vanilla JavaScript. It has no framework, build step, backend, tracking, or paid services.

## Run it locally

You need Python 3. From the project folder, run:

```text
py tools/serve_local.py
```

Then open <http://localhost:8000/portfolio/>. This server matches the GitHub Pages `/portfolio/` URL, and it serves `404.html` for missing paths.

## Project structure

| Path | Purpose |
|---|---|
| `index.html` | Homepage |
| `projects/` | Case-study pages |
| `404.html` | Not-found page |
| `assets/css/site.css` | All shared styles, with design tokens at the top |
| `assets/js/site.js` | Mobile menu, case-study index, and subtle reveal effects |
| `assets/fonts/` | Self-hosted fonts and their licenses |
| `assets/images/` | Images by project, plus a manifest of files still needed |
| `assets/documents/` | Public documents, such as an approved resume |
| `tools/` | Local server and site checker |

## Update content

- **Text:** Edit the HTML directly.
- **Header and footer:** These are repeated in every page. Make the same change in each file.
- **Images:** Follow `assets/images/README.md`.
- **Missing content:** Search the HTML for `NEEDS MY INPUT`.
- **Email, LinkedIn:** These appear in the Contact section of `index.html` and in the footer of every page.
- **Resume:** Replace `assets/documents/aarav-shah-resume.pdf` with the new PDF, keeping that file name. Every page links to it.

Use lowercase, hyphenated filenames, and relative paths for all internal links.

## Check the site

```text
py tools/check_site.py
py tools/check_site.py --publish
```

The first command checks links, anchors, filename case, and page structure. The second also fails if draft content remains, so it must pass before publishing.

See `DEPLOYMENT.md` for publishing steps.
