# Deploying to GitHub Pages

The site publishes from the root of the `main` branch of a repository named `Aarav-Portfolio`. It is live at <https://aaravshah07.github.io/Aarav-Portfolio/> (published November 20, 2026). The repository name is case-sensitive in the URL.

## Before the first push

Git history is permanent in practice, so finish these first.

1. **Run the publish check:** `py tools/check_site.py --publish` must report no problems.
2. **Review the site:** Remove the draft banner and all placeholders, and confirm the content is accurate.
3. **Confirm permissions:** Make sure you can share team, lab, and employer material.
4. **Approve personal details:** Only approved contact details and resume files should be included. Your phone number and GPA are approved in the resume PDF only (November 13, 2026). Keep any home address out of it, and never add the phone number to the site's pages.
5. **Remove file metadata:** Check images and PDFs for GPS data and author details.

## First-time setup

### 1. Protect your email address

In GitHub, open **Settings → Emails**. Turn on **Keep my email addresses private**, then copy your `noreply` address.

### 2. Create the repository on GitHub

Create a new repository named `portfolio`. Do not add a README, `.gitignore`, or license, since the project already has its own files.

Public repositories can use GitHub Pages on the free plan. In a public repository, all files and commit history can be seen by anyone.

### 3. Commit and push

Run these from the project folder, replacing the placeholders:

```text
git init -b main
git config user.name "Your Name"
git config user.email "<your-noreply-address>"
git add .
git status
```

In the `git status` output, make sure `CLAUDE.md`, `docs/`, and `source-media/` are **not** listed. Then continue:

```text
git commit -m "Initial portfolio site"
git remote add origin https://github.com/AaravShah07/Aarav-Portfolio.git
git push -u origin main
```

### 4. Turn on GitHub Pages

1. On GitHub, open the `portfolio` repository.
2. Click **Settings**.
3. In the sidebar, click **Pages**.
4. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
5. Set the branch to **main** and the folder to **/(root)**.
6. Click **Save**.
7. Select **Enforce HTTPS** when that option is available.

Once deployment finishes, the Pages settings show the site URL. The repository's **Actions** tab shows deployment progress.

### 5. Test the live site

Use a signed-out or private browser window and check that:

- Every page, image, font, and link works.
- The site works on a phone.
- A made-up URL, such as `/Aarav-Portfolio/does-not-exist`, shows the custom 404 page and its home link works.
- All links open the correct contact details and resume.

## Add the final URL to page metadata

Done on November 20, 2026: every page has these tags in its `<head>`. A new page needs its own address in them:

```html
<link rel="canonical" href="https://aaravshah07.github.io/Aarav-Portfolio/">
<meta property="og:url" content="https://aaravshah07.github.io/Aarav-Portfolio/">
```

Add an `og:image` tag on every page so shared links show a preview. Aarav chose his photo for this (November 17, 2026), using the JPG copy because some apps don't show WebP in previews:

```html
<meta property="og:image" content="https://aaravshah07.github.io/Aarav-Portfolio/assets/images/about/aarav-shah-preview.jpg">
<meta property="og:image:width" content="400">
<meta property="og:image:height" content="400">
<meta property="og:image:alt" content="Aarav Shah">
``` A `robots.txt` file isn't useful here, because crawlers only read it from the root of the domain, not from `/Aarav-Portfolio/`.

## Updating the site

Make and test your changes locally, then run:

```text
py tools/check_site.py --publish
git add .
git status
git commit -m "Describe the change"
git push
```

GitHub redeploys automatically. If the live site looks unchanged, wait a few minutes and hard-refresh the browser.

## Troubleshooting

| Problem | Likely cause | Fix |
|---|---|---|
| The site shows a 404 | Pages is off, or the branch or folder is wrong | Check **Settings → Pages** and the **Actions** tab |
| An image works locally but not online | Filename case doesn't match | Run `py tools/check_site.py` and rename to lowercase |
| Styles or links are broken | A path begins with `/` | Use a relative path |
| Personal information was pushed | It remains in Git history | Treat it as public, remove it, and rotate it if it's a credential. Ask for help before rewriting history |

## If the URL changes

If you rename the repository or add a custom domain, update the `/Aarav-Portfolio/` home link in `404.html`. Other links are relative and will continue to work. For a custom domain, follow GitHub's custom domain instructions.

## GitHub Pages limits

GitHub documents a 1 GB limit for published sites, a recommended 1 GB repository size, and soft limits of 100 GB of bandwidth per month and 10 branch builds per hour. Pages also doesn't support server-side code, password protection, custom response headers, or server redirects.
