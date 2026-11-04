"""Self-contained conceptual tear sensing workflow; no measured data or performance."""
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def txt(x,y,s,cls=''):
 return f'<text x="{x}" y="{y}" class="{cls}">{s}</text>'
def path(d,cls='line',extra=''):
 return f'<path d="{d}" class="{cls}" {extra}/>'
def head(n,s):return txt(0,25,n,'num')+txt(35,25,s,'head')+path('M0 42H350','rule')
def drop(x,y):return f'<path d="M{x} {y}c-12 21-22 29-22 43a22 22 0 0 0 44 0c0-14-10-22-22-43Z" fill="none" stroke="#426883" stroke-width="2"/>'
stages=[]
s=head('01','Tear samples')+drop(52,72)+drop(52,172)+txt(100,105,'Dry eye disease')+txt(100,205,'Non-dry-eye controls')
s+=txt(0,270,'Complex molecular mixtures','small');stages.append(s)
s=head('02','Solid-state nanopore sensing')
s+=txt(0,75,'Electrolyte reservoirs','small')
s+=path('M20 145H140L157 170L140 195H20Z M330 145H205L188 170L205 195H330Z','membrane')
s+=txt(24,174,'Solid membrane','tiny')+path('M50 105V135 M50 205V232','electrode')+txt(20,120,'+')+txt(20,231,'−')
s+=path('M50 100H5V240H50','line')+txt(66,233,'Applied potential','small')
s+=path('M168 83C149 103 190 114 171 136','molecule')+path('M174 139V202','arrow')
for x,y in [(144,111),(210,109),(145,225),(215,217)]:s+=f'<circle cx="{x}" cy="{y}" r="3" fill="#777"/>'
s+=txt(0,270,'Ionic transport + molecular interactions','small');stages.append(s)
s=head('03','Ionic-current signals')
s+=path('M20 70V220H345','line')+txt(0,80,'I','small')+txt(310,244,'Time','small')
s+=path('M30 100H65V144H79V100H110L115 122L124 135L132 119L136 100H180V177H216V100H248V130H260V100H340','signal')
s+=txt(0,270,'Conceptual traces; not recordings','small');stages.append(s)
s=head('04','Signal fingerprinting')
s+=txt(0,89,'Signal processing')+path('M90 103V120','arrow')+txt(0,145,'Feature extraction')
s+=txt(0,177,'Amplitude · duration · shape','small')
s+=path('M20 222H75M20 240H105M20 258H56 M145 222H230M145 240H200M145 258H254','features')
s+=txt(0,293,'Collective features, not chemical identities','small');stages.append(s)
s=head('05','Machine learning')
s+=txt(0,77,'Pattern analysis')
s+=path('M38 98V244H330','line')
for x,y in [(70,211),(108,165),(148,206),(177,154),(210,181),(245,134),(282,172),(130,132)]:s+=f'<circle cx="{x}" cy="{y}" r="5" fill="#426883"/>'
for x,y in [(102,208),(138,176),(185,212),(198,137),(224,159),(261,200),(298,140),(164,159)]:s+=f'<circle cx="{x}" cy="{y}" r="5" fill="white" stroke="#7b6a5b" stroke-width="2"/>'
s+=txt(0,275,'● Dry eye     ○ Controls','small')+txt(0,303,'Illustrative feature space; groups overlap','small');stages.append(s)
s=head('06','Exploratory classification')
s+=txt(0,97,'Exploring disease-associated')+txt(0,130,'differences in molecular')+txt(0,163,'signal fingerprints')
s+=txt(0,229,'Research objective','small')+txt(0,259,'No diagnostic performance implied','small');stages.append(s)
style='''<defs><marker id="a" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8" fill="none" stroke="#777" stroke-width="1.2"/></marker></defs><style>text{font:20px Arial,Helvetica,sans-serif;fill:#252525}.head{font-size:21px;font-weight:600}.num{font-size:15px;fill:#777}.small{font-size:16px;fill:#626262}.tiny{font-size:13px;fill:#555}.line,.rule,.arrow{fill:none;stroke:#777;stroke-width:1.5}.rule{stroke:#ddd}.arrow{marker-end:url(#a)}.membrane{fill:#ececec;stroke:#888;stroke-width:1.5}.electrode{fill:none;stroke:#555;stroke-width:3}.molecule,.signal,.features{fill:none;stroke:#426883;stroke-width:2}.features{stroke-width:4}</style>'''
def write(name,w,h,body):
 (R/'research-assets'/name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">Tear-based solid-state nanopore fingerprinting</title><desc id="desc">Conceptual workflow: dry eye and control tear samples, solid membrane nanopore under applied potential, illustrative ionic-current events, feature extraction, overlapping feature-space patterns, and exploratory classification. No measured results or molecular identities.</desc><rect width="{w}" height="{h}" fill="white"/>{style}{body}</svg>')
s=''
for i,g in enumerate(stages):
 x=30+(i%3)*400;y=20+(i//3)*380
 s+=f'<g transform="translate({x} {y})">{g}</g>'
s+=path('M390 160H416','arrow')+path('M790 160H816','arrow')+path('M1005 314V350H205V390','arrow')+path('M390 540H416','arrow')+path('M790 540H816','arrow')
write('tear-fingerprinting.svg',1220,730,s)
s=''
for i,g in enumerate(stages):
 s+=f'<g transform="translate(25 {20+i*340})">{g}</g>'
 if i<5:s+=path(f'M200 {320+i*340}V{345+i*340}','arrow')
write('tear-fingerprinting-mobile.svg',400,2050,s)
