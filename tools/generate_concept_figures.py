from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
A=R/'research-assets'
def svg(name,w,h,content,title):
 (A/name).write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title"><title id="title">{title}</title><defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8" fill="none" stroke="#666" stroke-width="1.3"/></marker></defs><rect width="{w}" height="{h}" fill="white"/><style>text{{font-family:Arial,Helvetica,sans-serif;fill:#242424;font-size:18px}}.small{{font-size:15px;fill:#626262}}.heading{{font-size:21px;font-weight:600}}.dna{{stroke:#405a80;stroke-width:5;fill:none}}.rna{{stroke:#b56b30;stroke-width:5;fill:none}}.line{{stroke:#777;stroke-width:1.5;fill:none}}.arrow{{stroke:#777;stroke-width:1.5;fill:none;marker-end:url(#arrow)}}</style>{content}</svg>''')
def text(x,y,s,cls='',anchor='start'):
 return f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{s}</text>'
def line(x,y,xx,yy,cls='line',extra=''):
 return f'<path d="M{x} {y}L{xx} {yy}" class="{cls}" {extra}/>'
def strand(x,y,x2,kind='dna',ends=True):
 s=line(x,y,x2,y,kind)
 for xx in range(x+5,x2,12): s+=line(xx,y,xx,y+(-8 if kind=='rna' else 8),'line')
 if ends:s+=text(x-12,y+5,'5′' if kind=='dna' else '3′','small','end')+text(x2+12,y+5,'3′' if kind=='dna' else '5′','small')
 return s
# Intro: conceptual connections, not a claim of complete experimental assay.
s=''
for x,title,subtitle in [(50,'Biomarkers','Disease-associated molecules'),(400,'Molecular recognition','Target-selective interactions'),(770,'Nanopore readout','Identity · counts · calibration')]:
 s+=text(x,39,title,'heading')+text(x,220,subtitle,'small')
s+='<path d="M65 113C80 72 115 155 133 109S171 80 190 130" class="rna"/>'
s+='<circle cx="245" cy="112" r="23" fill="none" stroke="#777" stroke-width="2"/><circle cx="245" cy="112" r="9" fill="none" stroke="#777"/>'
s+=strand(405,102,590,ends=False)+strand(482,137,590,'rna',False)
for x in range(487,590,12):s+=line(x,111,x,128)
s+=line(310,118,365,118,'arrow')+line(660,118,725,118,'arrow')
s+='<path d="M780 90H850M880 90H980M780 150H850M880 150H980" stroke="#999" stroke-width="12" fill="none"/><path d="M865 65V177" class="arrow"/><path d="M918 188H935V169H948V188H985" class="line"/>'
svg('research-workflow.svg',1100,245,s,'Conceptual biomarker recognition and nanopore readout framework')
# Quantification: no concentrations, experimental counts or numerical performance.
s=text(28,32,'Sequence-distinguishable DNA barcodes','heading')
s+=text(28,82,'Target')+strand(150,77,510,ends=False)+text(28,132,'Reference')+strand(150,127,510,ends=False)
s+=line(330,155,330,192,'arrow')
s+='<rect x="240" y="208" width="180" height="63" fill="white" stroke="#bbb"/>'+text(330,246,'ONT sequencing','','middle')
s+=line(330,282,330,318,'arrow')+text(330,354,'Barcode identification &amp; counting','heading','middle')
s+='<path d="M146 384H187M146 399H212M146 414H178M382 384H411M382 399H438M382 414H418" stroke="#405a80" stroke-width="5"/>'
s+=text(250,445,'Target reads','small','middle')+text(470,445,'Reference reads','small','middle')
s+=line(330,429,330,464,'arrow')+text(330,498,'Concentration estimation','heading','middle')+text(330,529,'Relative readout + known reference + calibration','small','middle')
svg('reference-workflow.svg',660,550,s,'Target and internal reference DNA barcodes, ONT sequencing, barcode counting and concentration estimation')
# RNA: source architecture and antiparallel orientations retained, no assigned cleavage sites/products.
s=text(25,32,'PROPOSED RNA-DETECTION STRATEGY','small')
s+=line(715,25,750,25,'dna')+text(760,31,'DNA','small')+line(830,25,865,25,'rna')+text(875,31,'RNA','small')+'<ellipse cx="975" cy="25" rx="14" ry="9" fill="#627c78"/>'+text(997,31,'Enzyme','small')
for y,n,title in [(88,'01','Intact DNA probe'),(242,'02','Target RNA hybridisation'),(405,'03','Duplex DNase-mediated DNA cleavage'),(585,'04','Proposed reporter generation')]:
 s+=text(25,y,n,'small')+text(65,y,title,'heading')
# region labels and unified DNA structure
s+=text(280,124,'Barcode-containing region','small')+text(700,124,'Recognition region','small')+text(963,124,'Anchor','small')
s+=strand(280,150,1010)+line(680,150,940,150,'dna','stroke-dasharray="2 0"')
s+=line(280,174,660,174)+line(680,174,940,174)+text(280,200,'UNI + ID + LSP','small')
s+=strand(280,283,1010)+strand(680,325,940,'rna')
for x in range(685,940,12):s+=line(x,291,x,317)
s+=text(680,355,'Antiparallel DNA–RNA hybrid','small')
# no fragmented products; area-level indication, not exact cut markers
s+=strand(280,456,1010)+strand(680,498,940,'rna')
for x in range(685,940,12):s+=line(x,464,x,490)
s+='<rect x="669" y="437" width="282" height="76" fill="none" stroke="#627c78" stroke-dasharray="4 5"/><ellipse cx="1000" cy="385" rx="18" ry="12" fill="#627c78"/>'
s+=text(680,403,'DNA is the cleavage substrate','small')+line(999,404,951,440,'arrow')
s+=text(280,536,'Cleavage extent and positions are not assigned. RNA is not the cleavage substrate.','small')
# deliberate abstract products: no intact reporter implied
s+='<rect x="280" y="615" width="355" height="68" fill="white" stroke="#999" stroke-dasharray="5 5"/>'
s+=text(457,643,'Barcode-containing DNA?','','middle')+text(457,667,'Integrity and endpoints unverified','small','middle')
s+=strand(760,645,990,'rna')+text(760,681,'Potential released RNA','small')
s+='<path d="M1050 647H1080V300H1040" class="arrow" stroke-dasharray="5 5"/>'
s+=text(280,721,'Reporter generation, RNA release, productive reuse and amplification require validation.','small')
s+=text(1042,738,'Dashed return: potential RNA recycling','small','end')
svg('rna-mechanism.svg',1120,760,s,'Four-stage proposed RNA mechanism showing a five-prime to three-prime DNA probe, antiparallel RNA, DNA-specific cleavage and unverified reporter generation and RNA recycling')
# Solid-state: generic cross-section explicitly not Zhejiang device
s=text(30,38,'Solid-state nanopore · conceptual cross-section','heading')
s+='<path d="M35 130H215L240 175L215 220H35Z M430 130H285L260 175L285 220H430Z" fill="#e7e7e7" stroke="#888" stroke-width="1.5"/>'
s+=text(38,110,'Electrolyte','small')+text(38,254,'Electrolyte','small')+text(38,180,'Solid membrane','small')
s+='<path d="M248 58C230 79 270 87 248 108S270 139 249 157" class="dna"/>'+line(250,233,250,287,'arrow')
s+=text(300,291,'Molecular translocation','small')+text(485,111,'Ionic-current readout','heading')
s+='<path d="M485 140V266H720M500 171H555V220H580V171H700" class="line"/>'+text(600,299,'Time','small','middle')
s+=text(485,329,'Illustrative event; not experimental data','small')
svg('solid-state-principle.svg',760,355,s,'Generic solid membrane nanopore cross-section with molecular translocation and an illustrative ionic-current blockade')
