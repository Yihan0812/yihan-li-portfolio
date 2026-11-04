# Yihan Li — Personal portfolio

A responsive, accessible portfolio built with plain HTML, CSS and JavaScript, based on the supplied 2026 CV. No build step or dependencies. The scientific SVG illustrations are conceptual, not experimental results.

## Local preview

Run `python3 -m http.server 8000` from this folder, then open http://localhost:8000.

## GitHub Pages

Push this folder's contents to the `main` branch of a GitHub repository. In repository Settings → Pages, select **GitHub Actions** as the source. The included workflow deploys automatically on pushes to `main`, or can be run manually from Actions. The published URL is shown by the deployment job.

All asset paths are relative, supporting both user and project Pages sites. Google Fonts is optional; system fonts are used when offline. Contact and CV download links work without JavaScript; research panels use native HTML details elements.

## Update content

Edit `index.html` for content, `styles.css` for appearance, and `script.js` for email copying and navigation state. Replace `assets/Yihan_Li_CV_2026.pdf` when updating the CV.

## Nanopore research pages

The overview is `nanopore.html`. Detail pages are `reference-quantification.html`, `enzyme-mediated-rna-detection.html` and `solid-state-nanopores.html`. Research styling is confined to `research.css`; the main homepage is preserved.

Edit content in `data/nanopore.json` and shared components in `tools/render_research.py`, then run `python3 tools/build_research.py`. The build uses Python’s standard library and reuses audited, versioned figure exports. It does not generate molecular artwork. All pages and navigation work as static HTML, with optional section highlighting and legacy hash routing in `research.js`.

`data/figure-audit.md` records figure decisions. `data/figure-sources.json` records source slides, export bounds, resolution and modifications. Three high-resolution PNGs were exported from editable elements in the user-supplied project presentation. The RNA mechanism is a conceptual HTML scheme; the unverified molecular drawings have been removed. No source decks or experimental datasets are included. Scientific figures preserve their full aspect ratio and can be viewed at full size; narrow viewports scroll detailed images rather than crop or compress their labels.
