"""Build a static research page and original SVG figures. Run from any directory."""
from pathlib import Path
from html import escape
import json
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'research-assets'
OUT.mkdir(exist_ok=True)
G='#24594e'; B='#557f9a'; R='#b66b46'; V='#8b739f'; INK='#203b32'; M='#64746b'; PALE='#e7eee4'
def text(x,y,s,size=14,fill=INK,anchor='start',extra=''):
 return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" {extra}>{escape(s)}</text>'
def line(x1,y1,x2,y2,color=G,width=2,dash=None):
 return f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{color}" stroke-width="{width}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>'
def rect(x,y,w,h,color,rx=3):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{color}"/>'
def circle(x,y,r,color):return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}"/>'
def arrow(x1,y1,x2,y2,color=M,dash=None):
 return line(x1,y1,x2,y2,color,1.6,dash)+f'<path d="M{x2-5} {y2-4}L{x2} {y2}L{x2-5} {y2+4}" fill="none" stroke="{color}" stroke-width="1.6"/>' if y1==y2 else line(x1,y1,x2,y2,color,1.6,dash)+f'<path d="M{x2-4} {y2-5}L{x2} {y2}L{x2+4} {y2-5}" fill="none" stroke="{color}" stroke-width="1.6"/>'
def svg(name,w,h,body,title,desc):
 (OUT/(name+'.svg')).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc><g font-family="Arial, sans-serif">{body}</g></svg>')
def strand(x,y,w,color=G):
 return line(x,y,x+w,y,color,4)+''.join(line(x+i,y,x+i,y-7,color,2) for i in range(8,int(w),12))
def pore(x,y,solid=False):
 # Cross-section, aqueous spaces above and below. Pore stays visibly open.
 a=rect(x-135,y-70,270,168,'#eef3ef',0)
 if solid:
  a+=rect(x-130,y,104,33,'#a6b6bd',1)+rect(x+26,y,104,33,'#a6b6bd',1)
  a+=line(x-26,y,x-26,y+33,B,2)+line(x+26,y,x+26,y+33,B,2)
 else:
  for i in list(range(-126,-32,12))+list(range(42,130,12)):
   a+=circle(x+i,y+2,4,'#a9b99e')+circle(x+i,y+31,4,'#a9b99e')+line(x+i-2,y+7,x+i-2,y+26,'#b9c6b0',1.5)+line(x+i+2,y+7,x+i+2,y+26,'#b9c6b0',1.5)
  a+=f'<path d="M{x-36} {y-12}Q{x-48} {y-35} {x-25} {y-40}L{x-13} {y-24}L{x-10} {y+48}L{x-30} {y+48}Z M{x+36} {y-12}Q{x+48} {y-35} {x+25} {y-40}L{x+13} {y-24}L{x+10} {y+48}L{x+30} {y+48}Z" fill="{G}"/>'
 for dx,dy,c in [(-90,-43,G),(76,-29,B),(-64,66,B),(86,71,G)]:
  a+=circle(x+dx,y+dy,6,'#dae6dc')+text(x+dx,y+dy+3,'+' if c==G else '−',9,c,'middle')
 a+=arrow(x+57,y-26,x+57,y+58,B)+text(x+69,y+17,'ion flow',10,B)
 return a
# 01 dual-pore comparison
s=''
for x,solid,label in [(206,False,'Biological nanopore'),(638,True,'Solid-state nanopore')]:
 s+=text(x,32,label,20,INK,'middle')+text(x,57,'Engineered protein + lipid membrane' if not solid else 'Opening in an artificial membrane',12,M,'middle')+pore(x,166,solid)
 s+=f'<path d="M{x-4} 83C{x-45} 109 {x+18} 122 {x} 153S{x-12} 206 {x+3} 246" fill="none" stroke="{R}" stroke-width="3"/>'
 s+=text(x-119,93,'cis · electrolyte',10,M)+text(x-119,269,'trans · electrolyte',10,M)
 s+=text(x,302,'Applied potential → ionic current',12,M,'middle')
 s+=line(x-116,333,x+116,333,'#c5d0c5',1)+f'<path d="M{x-110} 320H{x-72}V345H{x-35}V320H{x+10}V337H{x+39}V320H{x+110}" fill="none" stroke="{G if not solid else B}" stroke-width="2"/>'
 s+=text(x,375,'Illustrative current modulation · time →',11,M,'middle')
s+=line(422,65,422,355,'#d7dfd2',1)+text(422,412,'Shared principle: molecules alter ionic transport through a nanoscale pore.',13,INK,'middle')
svg('pore-comparison',844,440,s,'Two routes to nanoscale sensing','Cross-sections of a protein pore in a lipid membrane and a pore in an artificial membrane. DNA moves through each opening under an applied potential. Ion flow and schematic current changes illustrate a shared electrical principle, not measured data.')
# 02 biomarker flow: molecular symbols plus pipeline
s=''
xs=[110,320,530,740]
for i,(x,head,sub) in enumerate(zip(xs,['Molecular change','Accessible biofluid','Recognition','Nanopore readout'],['Disease-associated processes','DNA · RNA · proteins','Select target molecules','Identify and quantify'])):
 s+=text(x,33,'0'+str(i+1),11,M,'middle')+text(x,190,head,16,INK,'middle')+text(x,215,sub,11,M,'middle')
 if i<3:s+=arrow(x+70,108,x+137,108)
s+=circle(110,105,40,'#e0e9db')+circle(110,105,15,G)+line(110,62,110,76,R,3)+line(140,85,128,94,R,3)+line(84,127,73,137,R,3)
s+=f'<path d="M320 63C320 63 285 103 285 122A35 35 0 0 0 355 122C355 103 320 63 320 63Z" fill="#e0e9eb" stroke="{B}" stroke-width="2"/>'
s+=strand(298,116,40,G)+circle(331,136,7,R)+f'<path d="M309 145q11-15 19-3" fill="none" stroke="{V}" stroke-width="3"/>'
s+=strand(490,102,85,G)+strand(511,126,43,R)+''.join(line(x,106,x,119,'#b9c7b9',1) for x in range(517,550,7))
s+=rect(695,91,31,34,'#a6b6bd')+rect(742,91,43,34,'#a6b6bd')+arrow(734,71,734,150,R)
s+=text(425,264,'Sensitivity, molecular identity and quantitative reliability are separate analytical requirements.',12,M,'middle')
svg('biomarker-workflow',850,288,s,'Biomarker detection workflow','Conceptual sequence: disease-associated molecular changes, DNA RNA and protein biomarkers in a biofluid, selective molecular recognition, and a nanopore readout. No clinical outcomes or experimental data are shown.')
# 03 ONT detailed schematic, sequence signal not per base
s=pore(185,190)+text(32,29,'01 / CONTROLLED TRANSPORT',12,M)+text(349,29,'02 / CURRENT',12,M)+text(650,29,'03 / SEQUENCE',12,M)
s+=f'<path d="M170 55Q210 71 182 99L184 244Q159 271 185 287" fill="none" stroke="{R}" stroke-width="4"/>'
s+=f'<path d="M139 120Q125 86 159 80Q189 61 211 85Q241 94 222 123Z" fill="#d6b78f" stroke="#a67b4c" stroke-width="1.5"/>'
s+=text(38,69,'Motor protein',13,INK)+line(121,74,147,88,M,1)+text(28,151,'Membrane',12,M)+line(94,153,110,186,M,1)+text(33,283,'Protein pore',12,M)+line(114,278,159,237,M,1)+text(237,102,'DNA',12,R)+line(230,105,193,109,R,1)
s+=arrow(283,198,339,198)+line(361,128,361,247,'#b6c7b7',1)+line(361,247,596,247,'#b6c7b7',1)
s+=f'<path d="M367 150H393V173H415V161H441V206H467V185H487V218H511V175H540V202H565V185H591" fill="none" stroke="{G}" stroke-width="2.5"/>'
s+=text(361,112,'Ionic current',12,M)+text(599,270,'time →',11,M,'end')+text(477,304,'Local sequence context',12,INK,'middle')+text(477,326,'affects each current level',12,M,'middle')
s+=arrow(607,198,645,198)+rect(656,167,150,62,PALE)+text(731,194,'BASECALLING',11,M,'middle')+text(731,218,'A C G T …',21,G,'middle')+text(731,272,'Sequence alignment',12,INK,'middle')+text(731,294,'Barcode identity',12,M,'middle')
s+=text(420,375,'Illustrative signal only. Current levels do not map independently to single bases.',12,M,'middle')
svg('ont-readout',844,402,s,'ONT: molecule to current to sequence','A motor protein regulates DNA movement through a protein pore in a lipid membrane. Local nucleotide context modulates ionic current. Basecalling converts the trace to a sequence, and sequence alignment assigns a barcode. All current traces are conceptual.')
# 04 barcodes architecture not exact unpublished sequences
s=''
for y,c,name in [(90,G,'B1 · target'),(245,B,'B3 · reference')]:
 s+=text(35,y-26,name,16,c)+text(35,y+9,'5′-P',12,M)+rect(87,y-6,130,12,'#a8b89a')+rect(217,y-6,326,12,c)+text(559,y+9,'3′',12,M)
 s+=text(152,y+82,'Common region · 15 nt',11,M,'middle')+text(380,y+32,'Barcode-specific region · 35 nt',11,c,'middle')
 s+=strand(84,y+55,130,'#a8b89a')+text(49,y+62,'3′-A',10,M)+text(225,y+62,'5′',10,M)+text(340,y+62,'Complementary C-strand',11,M)
 s+=''.join(line(x,y+10,x,y+45,'#c5cdbf',1) for x in range(94,211,12))
 s+=circle(84,y+55,3,'#a8b89a') # Overhang indicated in caption
s+=arrow(648,165,707,165)+text(737,151,'ONT',17,INK,'middle')+text(737,176,'sequencing',12,M,'middle')
s+=line(35,355,808,355,'#d7dfd2',1)+text(35,391,'Sequence identification',15,INK)+arrow(239,386,293,386)+text(320,391,'B1 & B3 read counts',15,INK)+arrow(531,386,578,386)+text(608,391,'Relative abundance',15,INK)
s+=text(422,445,'B1: unknown concentration     /     B3: known reference concentration',13,M,'middle')
svg('barcode-reference',844,475,s,'B1 and B3 reference barcode architecture','Both phosphorylated DNA barcodes have a 15 nucleotide common region and a distinguishable 35 nucleotide region, oriented 5 prime to 3 prime. Complementary C strands are antiparallel and contain a 3 prime A overhang. Sequencing identifies each barcode so relative read counts can be compared. Not a library assembly protocol.')
# 05 probe architecture
s=text(30,34,'DNA PROBE / 83 nt DESIGN',12,M)+text(30,72,'5′-P',13,M)
parts=[('UNI code',20,G),('ID code',24,V),('LSP',5,'#99a291'),('RNA recognition',24,B),('Anchor',10,'#a8b3b6')]
x=83
for name,n,c in parts:
 w=n*8;s+=rect(x,60,w,16,c)+text(x+w/2,105,name,12,c,'middle')+text(x+w/2,126,f'{n} nt',11,M,'middle');x+=w
s+=text(x+14,74,'3′',13,M)+line(83,147,435,147,G,2)+text(259,170,'Signal encoding · UNI + ID',13,G,'middle')+line(475,147,667,147,B,2)+text(571,170,'Molecular recognition',13,B,'middle')
s+=text(35,213,'PROJECT TARGET RNA',11,M)+text(35,244,'5′-UAGCUUAUCAGACUGAUGUUGACU-3′',17,R,extra='font-family="monospace"')+text(35,275,'miR-21-5p · complementary to the DNA recognition region',12,M)
svg('rna-probe',844,301,s,'Functional architecture of the proposed RNA probe','An 83 nucleotide phosphorylated DNA probe comprises UNI code 20, ID code 24, LSP 5, RNA recognition region 24 and anchor 10 nucleotides in that 5 prime to 3 prime order. UNI and ID encode the signal. The target RNA sequence is shown 5 prime to 3 prime. No protective function is assigned to LSP or anchor.')
# 06 six step molecular scheme, vertical layout keeps sequence legible
s=''
rows=[(28,'Probe design','Separate sequence encoding from target recognition.'),(183,'Target recognition','Complementary DNA and RNA form an antiparallel hybrid.'),(382,'Enzymatic cleavage','Duplex DNase cleaves DNA within the hybrid substrate.'),(557,'Reporter generation','A barcode-containing fragment is proposed; endpoints are unknown.'),(712,'Potential RNA recycling','Released RNA may bind a fresh probe. Turnover remains unverified.'),(867,'Nanopore readout','Verify products and prepare a compatible library before sequencing.')]
for i,(y,title,sub) in enumerate(rows):
 s+=circle(32,y+4,16,'#e5ecdf')+text(32,y+9,str(i+1),13,G,'middle')+text(63,y+9,title,19,INK)+text(63,y+34,sub,12,M)
 if i<5:s+=line(32,y+28,32,rows[i+1][0]-20,'#d0dac9',1.5,'3 5')
# small probe line in step1
for x,w,c in [(110,100,G),(210,120,V),(330,25,'#99a291'),(355,190,B),(545,50,'#a8b3b6')]:s+=rect(x,94,w,10,c)
s+=text(71,105,'5′-P',12,M)+text(612,105,'3′',12,M)+text(225,137,'UNI + ID',12,G,'middle')+text(450,137,'Recognition',12,B,'middle')
# exact pairing, kept in one expanded panel
DNA='AGTCAACATCAGTCTGATAAGCTA';RNA='UAGCUUAUCAGACUGAUGUUGACU'[::-1]
s+=strand(111,272,142,G)+text(65,277,'5′-P',12,M)+text(712,277,'3′',12,M)+strand(662,272,32,'#a8b3b6')
for i,(d,r) in enumerate(zip(DNA,RNA)):
 x=279+i*16;s+=text(x,272,d,15,B,'middle',extra='font-family="monospace"')+line(x,282,x,298,'#aebfb5',1.2)+text(x,315,r,15,R,'middle',extra='font-family="monospace"')
s+=text(253,315,'3′',12,R,'end')+text(671,315,'5′',12,R)+text(704,315,'RNA',11,R)+text(470,349,'DNA · RNA base pairs, with opposite strand directions',11,M,'middle')
# cleavage shown as shaded region, no exact cleavage site
s+=strand(110,460,100,G)+strand(210,460,120,V)+strand(330,460,25,'#99a291')+line(357,460,560,460,B,3,'9 7')+strand(562,460,50,'#a8b3b6')
s+=strand(357,488,202,R)+rect(390,513,153,27,'#e0e9e8',13)+text(466,531,'Duplex DNase',12,G,'middle')+text(78,465,'5′',12,M)+text(630,465,'3′',12,M)+text(340,494,'3′',12,R,'end')+text(578,494,'5′',12,R)
# reporter unknown terminus and fragments
s+=text(74,643,'5′-P',12,M)+strand(113,637,100,G)+strand(213,637,120,V)+strand(333,637,25,'#99a291')+line(358,637,392,637,M,2,'3 4')+text(406,643,'?',19,M)+text(257,674,'Barcode retained? Verify integrity.',12,M,'middle')
s+=strand(510,627,23,B)+strand(549,638,18,B)+strand(584,623,28,B)+text(569,674,'DNA fragments',12,M,'middle')
s+=strand(113,792,170,R)+text(91,798,'3′',12,R)+text(303,798,'5′',12,R)+arrow(337,791,406,791,M,'5 5')+strand(441,792,100,G)+strand(541,792,120,B)+text(552,825,'Fresh probe · hypothetical next cycle',11,M,'middle')
s+=text(90,957,'Reporter',14,G)+arrow(173,952,214,952)+text(231,945,'Stop reaction',12,INK)+text(231,963,'Verify product',12,M)+arrow(333,952,371,952)+text(390,945,'Compatible',12,INK)+text(390,963,'ONT library',12,M)+arrow(487,952,526,952)+text(544,945,'Sequence',12,INK)+text(544,963,'Identify barcode',12,M)
s+=text(422,1013,'PROPOSED MECHANISM / No exact cleavage sites or validated reporter ends are assigned.',11,M,'middle')
svg('rna-reaction',844,1040,s,'Proposed RNA recognition and reporter generation in six steps','Step one probe design. Step two shows exact antiparallel pairing of DNA recognition sequence AGTCAACATCAGTCTGATAAGCTA from 5 prime to 3 prime with the supplied miR-21-5p RNA from 3 prime to 5 prime. Step three duplex DNA cleavage, with no exact cut sites. Step four a proposed barcode reporter with unknown terminal integrity. Step five potential unverified RNA recycling. Step six reaction stopping, product verification, compatible library preparation, nanopore sequencing and barcode identification.')
# 07 solid state with voltage and electrical circuit
s=pore(246,173,True)+text(30,31,'SOLID-STATE NANOPORE / CROSS-SECTION',12,M)
s+=circle(246,97,12,R)+circle(240,87,9,R)+circle(255,88,8,R)+arrow(246,118,246,232,R)+text(56,84,'Molecule',13,R)+line(122,88,224,95,R,1)
s+=text(48,171,'Solid membrane',12,M)+line(137,176,155,189,M,1)+text(282,148,'Pore',12,B)+line(279,151,265,173,B,1)+text(100,265,'Electrolyte on both sides',11,M)
s+=line(111,120,85,120,M,1.4)+line(85,120,85,309,M,1.4)+line(85,309,414,309,M,1.4)+line(414,309,414,248,M,1.4)+line(414,248,373,248,M,1.4)
s+=circle(246,309,22,'#f8f8f2')+text(246,315,'V',17,G,'middle')+text(207,314,'−',14,M,'middle')+text(284,314,'+',14,M,'middle')
s+=text(527,80,'Illustrative current blockade',16,INK)+line(529,117,529,237,'#b9c8b9',1)+line(529,237,798,237,'#b9c8b9',1)
s+=f'<path d="M539 147H615V204H678V147H790" fill="none" stroke="{B}" stroke-width="2.5"/>'+text(538,130,'Open-pore level',11,M)+text(648,223,'Event',11,B,'middle')+text(797,259,'time →',11,M,'end')
s+=text(531,299,'Depth: change in ionic current',12,M)+text(531,324,'Width: event duration',12,M)+text(422,379,'A conceptual blockade. Signals depend on the molecule, pore and solution conditions.',12,M,'middle')
svg('solid-state',844,407,s,'Solid-state nanopore and current blockade','A molecule moves through a nanoscale opening in an artificial solid membrane separating electrolytes. An applied potential drives ionic current. A generic event reduces current for a finite duration in this illustration. No specific membrane material or fabrication method is assigned to the Zhejiang work.')
print('Built seven original SVG figures.')

# Reusable static page components keep the public page usable without JavaScript.
data=json.loads((ROOT/'data/nanopore.json').read_text())
def figure(f):
 return f'<figure class="science-figure"><a href="research-assets/{f[0]}.svg" target="_blank" rel="noopener" aria-label="Open full-size figure: {escape(f[1])}"><img src="research-assets/{f[0]}.svg" alt="{escape(f[1])}" loading="lazy"></a><figcaption>{f[2]}</figcaption></figure>'
def section(item):
 return f'<section class="research-topic" id="{item["id"]}" aria-labelledby="{item["id"]}-title"><header class="topic-header"><p class="eyebrow">{item["number"]} / {item["label"]}</p><h2 id="{item["id"]}-title">{item["title"]}</h2><p class="topic-lead">{item["lead"]}</p></header>{item["body"]}'+''.join(figure(f) for f in item.get('figures',[]))+item.get('after','')+'</section>'
nav=''.join(f'<a href="#{x["id"]}"><span>{x["number"]}</span>{x["nav"]}</a>' for x in data['sections'])
refs=''.join(f'<li id="ref-{x["id"]}"><a href="{x["url"]}">{x["title"]} ↗</a><p>{x["detail"]}</p></li>' for x in data['references'])
page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Nanopore-Based Molecular Sensing | Yihan Li</title><meta name="description" content="Research principles and proposed molecular strategies in biological and solid-state nanopore sensing, DNA barcode quantification and RNA recognition."><meta name="theme-color" content="#183e36"><link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="styles.css"><link rel="stylesheet" href="research.css"><script src="research.js" defer></script></head><body class="research-page"><a class="skip" href="#main">Skip to content</a><header class="header wrap"><a class="wordmark" href="index.html" aria-label="Yihan Li, home">Yihan Li<span> / </span></a><nav aria-label="Main navigation"><a href="index.html#research" aria-current="page">Research</a><a href="index.html#about">About</a><a href="index.html#contact">Contact ↗</a></nav><a class="cv-link" href="assets/Yihan_Li_CV_2026.pdf" download>Download CV ↓</a></header><main id="main"><div class="research-masthead wrap"><a class="back-link" href="index.html#research">← Research portfolio</a><p class="eyebrow">RESEARCH EXPLORATION / 01</p><h1>Nanopore-Based<br><em>Molecular Sensing</em></h1><p class="masthead-subtitle">From single-molecule detection to early disease diagnostics</p><p class="masthead-intro">Exploring how molecular recognition becomes an electrical signal, and how that signal can support reliable molecular identification and measurement.</p><div class="affiliations"><span>Imperial College London<small>Biological nanopores · MSci research</small></span><span>Zhejiang University<small>Solid-state nanopores · Research experience</small></span></div></div><div class="research-layout wrap"><aside class="research-contents"><p class="eyebrow">ON THIS PAGE</p><nav aria-label="Research contents">'''+nav+'''</nav><a class="contents-reference" href="#references">Sources & attribution ↗</a></aside><div class="research-article">'''+''.join(section(x) for x in data['sections'])+'''<section class="research-topic references" id="references"><p class="eyebrow">SOURCES & ATTRIBUTION</p><h2>Scientific context</h2><p>The supplied presentations guide the research narrative. These original schematics explain concepts and do not reproduce experimental traces, concentration series or results.</p><div class="source-note"><strong>Research provenance</strong><p>Yihan Li, <cite>Nanopore-Based DNA Barcode Quantification Towards Early Disease Detection</cite>, supplied MSci project proposal (2026): source for the B1/B3 research exploration and proposed RNA integration.</p><p>Minghui Qi, <cite>Multiplexed and Multimodal Liquid Biopsy for Early-Stage Disease (Cancer) Detection Using the Oxford Nanopore Platform</cite>, supplied viva presentation (2026), supervisor Joshua Edel: source for broader group strategies and the RNA-probe architecture. Those strategies are credited to the group context, not presented as Yihan Li’s individual contributions.</p></div><ol>'''+refs+'''</ol><p class="source-note">Established principles are distinguished from proposed assay steps throughout. The RNA target sequence matches the supplied design and the linked miRBase entry. Zhejiang-specific experimental details await confirmation.</p></section></div></div><section class="research-end"><div class="wrap"><p class="eyebrow">CONTINUE THE CONVERSATION</p><h2>Molecules, mechanisms<br>and <em>measurement.</em></h2><a href="mailto:yl10023@ic.ac.uk">yl10023@ic.ac.uk ↗</a><a class="back-link" href="index.html#research">Explore the rest of my research →</a></div></section></main><footer class="wrap"><a class="wordmark" href="index.html">Yihan Li<span> / </span></a><p>Nanopore-based molecular sensing</p><a href="#main">Back to top ↑</a></footer></body></html>'''
(ROOT/'nanopore.html').write_text(page)
print('Built nanopore.html from data/nanopore.json.')
