# Yihan Li — Personal portfolio

A responsive, accessible portfolio built with plain HTML, CSS and JavaScript, based on the supplied 2026 CV. No build step or dependencies. The scientific SVG illustrations are conceptual, not experimental results.

## Local preview

Run `python3 -m http.server 8000` from this folder, then open http://localhost:8000.

## GitHub Pages

Push this folder's contents to the `main` branch of a GitHub repository. In repository Settings → Pages, select **GitHub Actions** as the source. The included workflow deploys automatically on pushes to `main`, or can be run manually from Actions. The published URL is shown by the deployment job.

All asset paths are relative, supporting both user and project Pages sites. Google Fonts is optional; system fonts are used when offline. Contact and CV download links work without JavaScript; research panels use native HTML details elements.

## Update content

Edit `index.html` for content, `styles.css` for appearance, and `script.js` for email copying and navigation state. Replace `assets/Yihan_Li_CV_2026.pdf` when updating the CV.

## Nanopore research page

`nanopore.html` is the static research page. Edit scientific text and source records in `data/nanopore.json`; edit reusable page and SVG components in `tools/build_research.py`. Run `python3 tools/build_research.py` to regenerate the HTML and seven SVG figures. Styles and progressive navigation are in `research.css` and `research.js`. No runtime build step is required. Figures are conceptual, not experimental data. Source presentations stay outside this public repository.
