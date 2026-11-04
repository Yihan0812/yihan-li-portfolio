"""Crop original PDF figures at 288 dpi; coordinates recorded from 108 dpi page review."""
from pathlib import Path
import json,hashlib
import pypdfium2 as pdf
R=Path(__file__).resolve().parents[1];A=R/'medchem-assets';A.mkdir(exist_ok=True)
sources={'docking':'/Users/fiee/Desktop/medchem report.pdf','lab':'/Users/fiee/Desktop/cmc lab report-3.pdf'}
# Bounding rectangles in reviewed 1.5x render pixels; entire structures and labels retained.
figures=[
('mpro-pose','docking',5,'Figure 6, Analogue 2 3D panel',(474,405,720,590),'MedChem overview and Mpro detail'),
('mpro-interactions','docking',5,'Figure 6, Analogue 2 interaction map',(195,407,430,574),'Mpro ligand evaluation'),
('mpro-designs','docking',1,'Figure 1, panel e',(531,845,830,922),'Mpro detail: three designed analogues'),
('mpro-redocking','docking',2,'Figure 4',(470,396,834,640),'Mpro modelling: co-crystal/redocking overlay'),
('mpro-proposed-route','docking',6,'Scheme 1',(64,571,439,737),'Mpro detail: proposed synthesis'),
('acyl-design','lab',2,'Figure 1',(452,209,833,299),'MedChem overview and acyl urea design; proposed para-Cl F2'),
('acyl-meta-product','lab',2,'Figure 2',(453,387,615,469),'Acyl urea detail: actually synthesised meta-Cl F2'),
('acyl-synthesis','lab',3,'Scheme 1',(62,451,832,692),'Overview full-width scheme; acyl urea synthesis'),
('acyl-acylation-mechanism','lab',3,'Figure 4',(62,789,730,973),'Acyl urea detail: source-proposed acylation mechanism'),
('acyl-substitution-mechanism','lab',4,'Figure 5',(62,96,797,527),'Acyl urea detail: source-proposed substitution mechanism')]
manifest=[]
for name,key,page,num,box,where in figures:
 doc=pdf.PdfDocument(sources[key]);im=doc[page-1].render(scale=4).to_pil();crop=im.crop(tuple(round(v*4/1.5) for v in box));out=A/(name+'.png');crop.save(out,optimize=True)
 manifest.append(dict(file=str(out.relative_to(R)),source=Path(sources[key]).name,page=page,figure=num,bounds_in_108dpi_review=box,resolution_dpi=288,width=crop.width,height=crop.height,location=where,sha256=hashlib.sha256(out.read_bytes()).hexdigest(),modifications='Rectangular crop only; original molecular geometry, arrows and scientific labels retained. No redrawing.'))
(R/'data/medchem-figure-inventory.json').write_text(json.dumps(manifest,indent=2)+'\n')
print([(f['file'],f['width'],f['height']) for f in manifest])
