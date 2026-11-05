"""Publication-style SVGs rendered only after the audited connectivity table exists."""
from pathlib import Path
import json,math
R=Path(__file__).resolve().parents[1];A=R/'phosphorus-assets';D=json.loads((R/'data/phosphorus-connectivity.json').read_text());states={s['id']:s for s in D['states']}
INK='#171717';RED='#a24d42';GREEN='#477568'
def text(x,y,t,cls='',anchor='start',fill=None):
 return f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}" text-anchor="{anchor}"'+(f' fill="{fill}"' if fill else '')+f'>{t}</text>'
def line(x,y,xx,yy,color=INK,width=1.8,dash=False):
 return f'<path d="M{x:.1f},{y:.1f} L{xx:.1f},{yy:.1f}" fill="none" stroke="{color}" stroke-width="{width}"'+(' stroke-dasharray="5 4"' if dash else '')+'/>'
def arrow(x,y,xx,yy):return f'<path d="M{x},{y}L{xx},{yy}" class="arrow"/>'
def connector(d):return f'<path d="{d}" class="arrow"/>'
def bond(a,b,marginA=15,marginB=15,color=INK,dash=False):
 dx=b[0]-a[0];dy=b[1]-a[1];l=math.hypot(dx,dy);return line(a[0]+dx/l*marginA,a[1]+dy/l*marginA,b[0]-dx/l*marginB,b[1]-dy/l*marginB,color,dash=dash)
def svg(name,w,h,title,desc,body):
 style='''<defs><marker id="arrow" markerWidth="9" markerHeight="7" refX="8" refY="3.5" orient="auto"><path d="M0,0L9,3.5L0,7Z" fill="#171717"/></marker></defs><style>text{font:22px Arial,Helvetica,sans-serif;fill:#171717}.atom{font-size:25px}.small{font-size:18px;fill:#555}.tiny{font-size:16px;fill:#626262}.heading{font-size:25px;font-weight:600}.status{font-size:18px;font-weight:600}.arrow{fill:none;stroke:#171717;stroke-width:1.6;marker-end:url(#arrow)}</style>'''
 (A/name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{title}</title><desc id="desc">{desc}</desc><rect width="{w}" height="{h}" fill="white"/>{style}{body}</svg>')
def phenyl(cx,cy,toward):
 # An attachment vertex faces the external sulfur. No aromatic atom is invented.
 ang=math.atan2(toward[1]-cy,toward[0]-cx);r=32
 vs=[(cx+r*math.cos(ang+i*math.pi/3),cy+r*math.sin(ang+i*math.pi/3)) for i in range(6)]
 s=''
 for i in range(6):s+=line(*vs[i],*vs[(i+1)%6])
 for i in [0,2,4]:
  a=vs[i];b=vs[(i+1)%6];a=(cx+(a[0]-cx)*.77,cy+(a[1]-cy)*.77);b=(cx+(b[0]-cx)*.77,cy+(b[1]-cy)*.77);s+=line(*a,*b,width=1.6)
 return s,vs[0]
def tetra(cx,cy,labelled=True,scale=1,red=None):
 coords={'1':(cx,cy-70*scale),'2':(cx-65*scale,cy+28*scale),'3':(cx+65*scale,cy+28*scale),'4':(cx,cy-3*scale)}
 s=''
 for e in ['12','13','14','23','24','34']:s+=bond(coords[e[0]],coords[e[1]],13,13,RED if e==red else INK,e=='23')
 for i,(x,y) in coords.items():s+=text(x,y+8,'P'+i if labelled else 'P','atom','middle')
 return s
# FIGURE 1: complete line structures and exact stoichiometric coefficients.
s=text(35,40,'01  Overall transformation','heading')
s+=tetra(140,245,False,1.1)+text(140,345,'White phosphorus','small','middle')
s+=text(270,247,'+')+text(325,247,'6','atom')
ss=[(440,237),(495,237)];s+=bond(ss[0],ss[1],14,14)
for (sx,sy),(cx,cy) in zip(ss,[(365,200),(570,274)]):
 ph,v=phenyl(cx,cy,(sx,sy));s+=ph+bond((sx,sy),v,15,0)+text(sx,sy+8,'S','atom','middle')
s+=text(468,345,'Diphenyl disulfide','small','middle')
s+=arrow(650,237,805,237)+text(727,200,'Et₃N','','middle')+text(727,274,'Project additive','tiny','middle')
s+=text(845,245,'4','atom')
p=(1000,220);s+=text(p[0],p[1]+8,'P','atom','middle')
for sulfur,ring in [((925,172),(855,128)),((1075,172),(1145,128)),((1000,307),(1000,385))]:
 ph,v=phenyl(*ring,sulfur);s+=ph+bond(p,sulfur,17,15)+bond(sulfur,v,15,0)+text(sulfur[0],sulfur[1]+8,'S','atom','middle')
s+=text(1000,453,'Tris(phenylthio)phosphine, P(SPh)₃','small','middle')
s+=text(35,505,'P₄ + 6 PhSSPh → 4 P(SPh)₃','status')
s+=text(35,541,'Literature-supported net thiolation; no project yield or product confirmation is implied.','small')
s+=text(35,574,'Scheme 2(a) uses KHMDS and a 4-chlorophenyl disulfide; Et₃N/PhSSPh is the specified project system.','tiny')
s+=text(35,601,'Literature context: Horsley Downie et al., ChemSusChem, DOI 10.1002/cssc.202401895.','tiny')
svg('figure-1-overall.svg',1260,625,'Overall white phosphorus thiolation','Balanced reaction with full P4, diphenyl disulfide and tris phenylthio phosphine structures. Et3N denotes the specified project additive; no yield is assigned.',s)
# FIGURE 2: formal connectivity graph candidates, not calculated structures.
coords={'1':(0,-70),'2':(-75,10),'3':(75,10),'4':(0,90)}
angles={'1':[-120,-60,-90],'2':[155,205,180],'3':[-25,25,0],'4':[60,120,90]}
def state(id,cx,cy,newPS=(),cut=None):
 r=states[id];s=''
 for a,b in r['PP']:
  k=a[1:]+b[1:];p=coords[a[1:]];q=coords[b[1:]]
  s+=bond((cx+p[0],cy+p[1]),(cx+q[0],cy+q[1]),18,18,RED if k==cut else INK,k=='23')
 for i,n in enumerate(r['thiophenoxy_counts'],1):
  x,y=coords[str(i)];x+=cx;y+=cy
  for j in range(n):
   a=math.radians(angles[str(i)][j]);end=(x+70*math.cos(a),y+70*math.sin(a));color=GREEN if (i,j) in newPS else INK
   s+=bond((x,y),end,19,25,color)+text(end[0],end[1]+7,'PhS' if math.cos(a)<0 else 'SPh','','middle',color)
 for i,(x,y) in coords.items():
  s+=text(cx+x,cy+y+7,'P'+i,'atom','middle')
  if r['formal_charges'].get(i):s+=text(cx+x+22,cy+y-11,'−','atom')
 return s
s=text(30,37,'02  Literature motif and hypothetical P₄ connectivity pathways','heading')
s+=text(30,70,'Structures below are formal connectivity hypotheses, not published intermediates or optimised geometries.','small')
s+=text(200,130,'P₄','status','middle')+text(700,130,'I1 · Hypothetical Intermediate','status','middle')+text(1200,130,'N1 · Hypothetical Intermediate','status','middle')
s+=tetra(200,285,True,1.2,red='12')+state('I1',700,285,newPS=[(1,0)])+state('N1',1200,285,newPS=[(2,0)])
s+=arrow(365,280,520,280)+text(440,215,'+ SPh⁻','small','middle')+text(440,325,'Attack at P1','tiny','middle')+text(440,352,'Break P1–P2','tiny','middle')
s+=arrow(870,280,1018,280)+text(940,215,'+ PhSSPh','small','middle')+text(940,325,'Form P2–SPh','tiny','middle')+text(940,352,'Release SPh⁻','tiny','middle')
s+=text(30,424,'Activation motif adapted from Scheme 2(c): thiolate attack → P–P cleavage → disulfide capture.','small')
s+=connector('M1200,405 V467 H400 V535')+connector('M1100,467 V535')
s+=text(400,575,'Candidate Pathway A · adjacent cleavage','status','middle')+text(1100,575,'Candidate Pathway B · opposite cleavage','status','middle')
s+=text(400,611,'Break P1–P3; form P1–SPh and P3–SPh (net)','small','middle')+text(1100,611,'Break P3–P4; form P3–SPh and P4–SPh (net)','small','middle')
s+=state('A2',400,775,newPS=[(1,1),(3,0)])+state('B2',1100,775,newPS=[(3,0),(4,0)])
s+=text(400,969,'A2 · Hypothetical Intermediate','status','middle')+text(1100,969,'B2 · Hypothetical Intermediate','status','middle')
s+=arrow(400,991,400,1071)+arrow(1100,991,1100,1071)
s+=text(430,1020,'Break P2–P3','small')+text(430,1049,'+ P2–SPh, P3–SPh (net)','tiny')
s+=text(1130,1020,'Break P1–P4','small')+text(1130,1049,'+ P1–SPh, P4–SPh (net)','tiny')
s+=state('A3',400,1235,newPS=[(2,1),(3,1)])+state('B3',1100,1235,newPS=[(1,1),(4,1)])
s+=text(400,1432,'A3 · Hypothetical Intermediate · star','status','middle')+text(1100,1432,'B3 · Hypothetical Intermediate · chain','status','middle')
s+=text(30,1490,'Each lower arrow repeats the two-step motif with one PhSSPh; it is not a single elementary step.','small')
s+=text(30,1524,'Symmetry: initial six edges equivalent. In N1, {13,14,23,24} are equivalent; {34} is distinct.','small')
s+=text(30,1558,'Only representative later branches shown. Neutral P: 3 bonds; I1 P2: 2 bonds, charge −1. SPh = S–phenyl.','small')
s+=text(30,1592,'Red: bond selected for cleavage. Green: newly installed P–S bond. Dashed P2–P3 is a P–P bond, not a missing edge.','tiny')
s+=text(30,1626,'Thiolate initiation under Et₃N and the existence of these labelled candidates remain unassigned.','tiny')
s+=text(30,1660,'Motif: Horsley Downie et al., DOI 10.1002/cssc.202401895, Scheme 2(c), CC BY 4.0; labelled graphs are new hypotheses.','tiny')
svg('figure-2-pathways.svg',1500,1695,'Candidate phosphorus connectivity pathways','P1 to P4 labels track a formal thiolate attack, anionic first-cleavage candidate and disulfide capture, then non-equivalent adjacent and opposite cleavage branches. Subsequent star and chain candidates are hypothetical, not proven intermediates.',s)
# FIGURE 3: research actions and limits only, no fabricated spectra or numerical results.
s=text(30,42,'03  Computational and experimental investigation','heading')
s+=text(30,80,'Research approach; a complete reaction mechanism was not established.','small')
s+=text(40,145,'COMPUTATIONAL INVESTIGATION','status')+line(40,163,650,163)
s+=text(40,211,'Candidate reaction pathway generation')+arrow(315,235,315,277)
s+=text(40,316,'Gaussian-based geometry optimisation')+arrow(315,340,315,382)
s+=text(40,422,'Evaluate alternative P-containing structures')+arrow(315,446,315,488)
s+=text(40,528,'Challenge: chemically plausible optimised geometries')
s+=text(40,565,'Connectivity and valence must be checked after optimisation.','small')+text(40,596,'No converged minima, energies or transition states are assigned here.','tiny')
s+=text(755,145,'EXPERIMENTAL INVESTIGATION','status')+line(755,163,1370,163)
s+=text(755,211,'Time-resolved NMR reaction monitoring')+arrow(1050,235,1050,277)
s+=text(755,316,'Controls: compare P₄ / PhSSPh / Et₃N combinations')+arrow(1050,340,1050,382)
s+=text(755,422,'Attempts to trap reactive intermediates')+arrow(1050,446,1050,488)
s+=text(755,528,'Subsequent chromatographic or MS analysis')+text(755,565,'Exact analytical technique remains unconfirmed.','small')
s+=text(755,596,'No trapped-intermediate assignment or experimental outcome implied.','tiny')
s+=line(40,654,1370,654)+text(40,703,'Interpretation: compare candidate structures with experimental evidence; retain unresolved assignments.','status')
svg('figure-3-investigation.svg',1420,750,'Computational and experimental investigation workflow','Parallel computational and experimental research streams. Candidate generation, Gaussian optimisation and chemical plausibility are compared with NMR monitoring, reagent controls, trapping attempts and analysis whose exact technique is unconfirmed. No mechanism is claimed established.',s)
print('Rendered three SVGs from the prior connectivity audit.')
