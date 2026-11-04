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

`nanopore.html` is the concise overview. The three static detail routes are `reference-quantification.html`, `enzyme-mediated-rna-detection.html` and `solid-state-nanopores.html`. The two ONT directions are parallel strategies, not sequential stages.

Scientific content and references live in `data/nanopore.json`. Reusable page layouts are in `tools/render_research.py`; overview schematics in `tools/overview_figures.py`; original detail schematics in `tools/build_research.py`. Run `python3 tools/build_research.py` to regenerate all four pages and SVGs. Styles and navigation enhancement remain in `research.css` and `research.js`. Every page works without JavaScript; legacy article hashes redirect to the relevant detail page when JavaScript is available.

Overview figures have dedicated mobile compositions to keep molecular labels legible. Detailed figures support horizontal scrolling and full-size viewing. Original source presentations remain outside the public repository. No unpublished experimental results or numerical performance claims are included.
