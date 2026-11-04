"""Regenerate research HTML. Source exports are versioned, never redrawn during a build."""
from pathlib import Path
from render_research import render_site
ROOT=Path(__file__).resolve().parents[1]
for name in ['project-b1-b3.png','project-barcode-design.png','project-ont-readout.png']:
 if not (ROOT/'research-assets'/name).is_file():
  raise FileNotFoundError(f'Missing audited source figure: {name}')
render_site(ROOT)
