"""Notebook-led figures. No calculations; only readable candidate motifs are drawn."""
from pathlib import Path
import json,math,html
R=Path(__file__).resolve().parents[1];D=R/'research/phosphorus';A=D/'figures';A.mkdir(parents=True,exist_ok=True)
K='#191919';RED='#a04f45';GREEN='#4b7568'
def txt(x,y,s,cl='',anchor='start'):
 return f'<text x="{x}" y="{y}" class="{cl}" text-anchor="{anchor}">{html.escape(s)}</text>'
def ln(x,y,xx,yy,c=K,dash=False):return f'<path d="M{x},{y}L{xx},{yy}" fill="none" stroke="{c}" stroke-width="1.8"'+(' stroke-dasharray="5 4"' if dash else '')+'/>'
def ar(x,y,xx,yy,dash=False):return f'<path d="M{x},{y}L{xx},{yy}" class="arrow"'+(' stroke-dasharray="5 4"' if dash else '')+'/>'
def con(d,dash=False):return f'<path d="{d}" class="arrow"'+(' stroke-dasharray="5 4"' if dash else '')+'/>'
def bond(a,b,ma=14,mb=14,c=K,dash=False):
 dx=b[0]-a[0];dy=b[1]-a[1];le=math.hypot(dx,dy)
 return ln(a[0]+dx/le*ma,a[1]+dy/le*ma,b[0]-dx/le*mb,b[1]-dy/le*mb,c,dash)
def save(name,w,h,title,body):
 style='''<defs><marker id="a" markerWidth="8" markerHeight="7" refX="7" refY="3.5" orient="auto"><path d="M0 0L8 3.5L0 7Z" fill="#191919"/></marker></defs><style>text{font:22px Arial,Helvetica,sans-serif;fill:#191919}.head{font-size:27px;font-weight:600}.sub{font-size:22px;font-weight:600}.small{font-size:18px;fill:#555}.tiny{font-size:16px;fill:#666}.atom{font-size:25px}.arrow{fill:none;stroke:#191919;stroke-width:1.6;marker-end:url(#a)}</style>'''
 (A/name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title"><title id="title">{html.escape(title)}</title><rect width="{w}" height="{h}" fill="white"/>{style}{body}</svg>')
def charge(x,y,c):return txt(x,y,'+' if c==1 else '−','atom')
# Every phosphorus centre is counted locally, not atom-mapped through notebook pages.
models={
 'P4':dict(PP=['12','13','14','23','24','34'],S=[0,0,0,0],q={},source='p4 initial; established P4 structure'),
 'sulfenyl-cation':dict(PP=['12','13','14','23','24','34'],S=[0,0,1,0],q={'3':1},source='pp2–4: proposed electrophilic sulfur transfer'),
 'opened':dict(PP=['12','14','23','24','34'],S=[1,0,1,0],q={},source='p4 boxed opened P4 motif'),
 'p4-a':dict(PP=['12','14','23','24'],S=[1,0,2,1],q={},source='p4 (1) / a; triangle + pendant motif'),
 'p4-b':dict(PP=['12','14','23','34'],S=[1,1,1,1],q={},source='p4 (2) / b; four-membered ring, reprojected'),
 'P4-chain':dict(PP=['12','23','34'],S=[2,1,1,2],q={},source='p5 b → circled (2): interpreted open P4 motif; atom mapping unresolved'),
 'P3-ring':dict(PP=['12','13','23'],S=[1,1,1],q={},source='pp3–5 later P3 ring motif'),
 'P3-chain':dict(PP=['12','23'],S=[2,1,2],q={},source='pp3–5 later open P3 motif'),
 'P2':dict(PP=['12'],S=[2,2],q={},source='pp1–2 route 1; p6 P2 cleavage candidate'),
 'P1':dict(PP=[],S=[3],q={},source='literature target / notebook proposed P1 release')}
for id,m in models.items():
 m['PS']=[[f'P{i}',f'SPh({i}{chr(97+j)})'] for i,n in enumerate(m['S'],1) for j in range(n)]
 m['coordination']=[sum(str(i) in e for e in m['PP'])+s for i,s in enumerate(m['S'],1)]
 assert all(n==3+m['q'].get(str(i),0) for i,n in enumerate(m['coordination'],1)),(id,m)
(D/'notebook-connectivity.json').write_text(json.dumps(dict(policy='Local vertex indices are editorial graph bookkeeping only, not recovered notebook atom mapping. All motifs are hypotheses, not verified intermediates.',models=models,unresolved=['p4 a circled (2)/(3) internal edges','crossed-out N–S-retaining P4 adduct','p7 direct-base P4 charge localisation','p8 Lewis-pair/trap reagent','p9 potassium formula']),indent=2)+'\n')
lines=['# Notebook motif connectivity audit','','Local vertex indices are NOT a global notebook atom map. Every motif is a hypothesis or topology reading, not a computed/isolated intermediate. SPh counts per local P vertex follow the drawing. All bonds are single.','', '| Motif | P–P edges (local indices) | SPh counts | P charge | Source / limit |','|---|---|---|---|---|']
for id,m in models.items():lines.append(f'| {id} | {", ".join(m["PP"]) or "none"} | {m["S"]} | {m["q"] or "neutral"} | {m["source"]} |')
lines+=['','Initial S transfer: new P–S at a tetracoordinate P+, with [N(SiMe3)2]− proposed to depart. Subsequent thiolate capture opens one P–P bond. For a/b, the notebook distinguishes different sulfur-transfer/cleavage choices; uniquely recovered global atom identities are unavailable. Later graph relations are motif-level proposals, not balanced elementary steps.','', 'Previously generated I1/N1/A2/B2/A3/B3 examples remain separately identified in the older conceptual audit; they are not relabelled as notebook intermediates.']
(D/'notebook-connectivity.md').write_text('\n'.join(lines)+'\n')
# Ensure the connectivity record exists BEFORE figure generation.
def graph(id,cx,cy,cut=None,small=False):
 m=models[id];n=len(m['S']);sc=.85 if small else 1
 if n==4:
  if id=='P4' or id=='sulfenyl-cation':pos={'1':(0,-80),'2':(-80,40),'3':(80,40),'4':(0,0)}
  elif id=='p4-b':pos={'1':(0,-80),'2':(-80,0),'3':(0,80),'4':(80,0)}
  elif id=='P4-chain':pos={'1':(-125,25),'2':(-42,-25),'3':(42,25),'4':(125,-25)}
  else:pos={'1':(0,-80),'2':(-80,0),'3':(80,0),'4':(0,80)}
 elif n==3:
  pos={'1':(-80,35),'2':(0,-65),'3':(80,35)} if id=='P3-ring' else {'1':(-95,30),'2':(0,-30),'3':(95,30)}
 elif n==2:pos={'1':(-65,0),'2':(65,0)}
 else:pos={'1':(0,0)}
 pos={i:(cx+x*sc,cy+y*sc) for i,(x,y) in pos.items()};s=''
 for e in m['PP']:s+=bond(pos[e[0]],pos[e[1]],15,15,RED if cut==e else K,dash=(id in ['P4','sulfenyl-cation','opened'] and e=='24'))
 for i,count in enumerate(m['S'],1):
  x,y=pos[str(i)]
  if n==1:angles=[-150,-30,90]
  elif n==2:angles=[-135,135] if i==1 else [-45,45]
  elif id=='p4-b':angles={1:[-90],2:[180],3:[90],4:[0]}[i]
  elif id=='P4-chain':angles=[-160,150] if i==1 else ([-30,30] if i==4 else ([-90] if i==2 else [90]))
  elif n==3:angles=([-165,110] if i==1 else ([-120,-60] if i==2 else [-15,70]))
  else:angles={1:[-120,-60],2:[155,205],3:[-30,30],4:[60,120]}[i]
  for j in range(count):
   a=math.radians(angles[j]);end=(x+65*sc*math.cos(a),y+65*sc*math.sin(a));lab='PhS' if math.cos(a)<0 else 'SPh'
   s+=bond((x,y),end,17,25)+txt(round(end[0],1),round(end[1]+7,1),lab,'','middle')
  s+=txt(x,y+8,'P','atom','middle')
  if m['q'].get(str(i)):s+=charge(x+8,y-24,m['q'][str(i)])
 return s
# 1. Existing complete line structures retained; base roles explicitly separated.
old=(R/'phosphorus-assets/figure-1-overall.svg').read_text()
old=old.replace('Et₃N/PhSSPh is the specified project system.','Bases investigated separately in the notebook: Et₃N and KHMDS.')
old=old.replace('Et₃N','Net stoichiometry',1).replace('Project additive','not project conditions').replace('01  Overall transformation','01  Overall phosphorus functionalisation')
old=old.replace('Et3N denotes the specified project additive; no yield is assigned.','The bases were investigated separately; no project yield is assigned.')
(A/'figure-1-overall.svg').write_text(old)
# 2. Proper, distinct N/S ionic structures, not interchangeable bases.
def ns_pair(cx,cy,kind):
 s='';N=(cx,cy);S=(cx+110,cy);s+=bond(N,S)+txt(cx,cy+8,'N','atom','middle')+txt(cx+110,cy+8,'S','atom','middle')+bond(S,(cx+175,cy),15,17)+txt(cx+175,cy+7,'Ph','','middle')
 for a,lab in [(-125,'Et' if kind=='Et' else 'SiMe₃'),(125,'Et' if kind=='Et' else 'SiMe₃')]:
  aa=math.radians(a);e=(cx+73*math.cos(aa),cy+73*math.sin(aa));s+=bond(N,e,17,25)+txt(round(e[0],1),round(e[1]+7,1),lab,'','middle')
 if kind=='Et':s+=bond(N,(cx-90,cy),17,20)+txt(cx-90,cy+7,'Et','','middle')+charge(cx+18,cy-20,1)
 return s
s=txt(30,42,'02  Alternative activation hypotheses','head')+txt(30,78,'Different formal roles for Et₃N and KHMDS; none of these drawings establishes an elementary step.','small')
s+=txt(30,135,'Et₃N at sulfur · notebook p. 6','sub')+txt(65,233,'Et₃N + Ph–S–S–Ph')+ar(360,225,525,225)+ns_pair(725,225,'Et')+txt(1060,233,'+ Ph–S⁻')
s+=txt(30,354,'KHMDS at sulfur · pp. 1–2, 8–9','sub')+txt(35,465,'K⁺ [N(SiMe₃)₂]⁻ + Ph–S–S–Ph')+ar(440,457,575,457)+ns_pair(730,457,'HMDS')+txt(1060,465,'+ K⁺ Ph–S⁻')
s+=txt(30,570,'PhS–N(SiMe₃)₂ is a notebook-reported / tentative GC–MS assignment, not an established isolated intermediate.','small')
s+=txt(30,639,'Direct P attack · “route 1” (pp. 1–2) and Et₃N alternative (p. 6)','sub')
def pn(cx,cy,kind):
 s=txt(cx,cy+8,'P','atom','middle')+txt(cx+110,cy+8,'N','atom','middle')+bond((cx,cy),(cx+110,cy))
 for yy in [-60,60]:
  s+=bond((cx,cy),(cx-70,cy+yy),16,25)+txt(cx-70,cy+yy+7,'PhS','','middle')
 for yy in [-60,60]:
  lab='Et' if kind=='Et' else 'SiMe₃'
  s+=bond((cx+110,cy),(cx+185,cy+yy),17,25)+txt(cx+185,cy+yy+7,lab,'','middle')
 if kind=='Et':s+=bond((cx+110,cy),(cx+215,cy),17,20)+txt(cx+215,cy+7,'Et','','middle')+charge(cx+102,cy-25,1)
 return s
def p_anion(cx,cy):
 s=txt(cx,cy+8,'P','atom','middle')+charge(cx-28,cy-18,-1)
 for yy in [-58,58]:s+=bond((cx,cy),(cx+75,cy+yy),17,25)+txt(cx+75,cy+yy+7,'SPh','','middle')
 return s
s+=graph('P2',195,800,small=True)+txt(195,916,'+ KHMDS','small','middle')+ar(390,800,525,800)+pn(680,800,'HMDS')+txt(980,808,'+ K⁺')+p_anion(1180,800)
s+=graph('P2',195,1080,small=True)+txt(195,1196,'+ Et₃N','small','middle')+ar(390,1080,525,1080)+pn(680,1080,'Et')+txt(1010,1088,'+')+p_anion(1180,1080)
s+=txt(30,1272,'Additional sulfur-activation hypothesis · notebook p. 7','sub')
s+=txt(35,1395,'HO⁻ + Ph–S–S–Ph')+ar(370,1387,555,1387)
for x,lab in [(690,'Ph'),(790,'S'),(880,'O'),(970,'H')]:s+=txt(x,1395,lab,'atom','middle')
for a,b in [(690,790),(790,880),(880,970)]:s+=bond((a,1387),(b,1387),18,18)
s+=txt(1090,1395,'+ Ph–S⁻')
s+=txt(30,1490,'Direct Et₃N–P₄ and OH⁻ alternatives (p. 7): precise adduct connectivity unresolved; no unique structure assigned.','small')
s+=txt(30,1535,'Ph = C₆H₅; Et = CH₂CH₃; SiMe₃ = Si(CH₃)₃. Candidate structures only; no intermediates claimed isolated.','tiny')
save('figure-2-base-hypotheses.svg',1420,1570,'Notebook Et3N and KHMDS activation hypotheses',s)
# 3. Initial electrophilic sulfur transfer is notebook-derived, not the old thiolate-first generic sequence.
s=txt(30,43,'03  Initial P₄ functionalisation · notebook pp. 2–4','head')+txt(30,80,'Candidate electrophilic S transfer, followed by thiolate capture and P–P opening.','small')
s+=graph('P4',195,260)+txt(360,207,'+ PhS–N(SiMe₃)₂','small')+ar(365,260,575,260)+graph('sulfenyl-cation',765,260,cut='13')
s+=txt(760,434,'[P₄(SPh)]⁺ candidate','sub','middle')+txt(760,469,'+ [N(SiMe₃)₂]⁻ proposed to depart','small','middle')
s+=ar(955,260,1150,260)+txt(1050,207,'+ PhS⁻','small','middle')+graph('opened',1345,260)
s+=txt(1345,434,'Opened P₄ motif','sub','middle')+txt(30,548,'Red: the selected P–P edge in this local reconstruction. All structures remain hypotheses.','small')
s+=txt(30,585,'Notebook P atoms are unnumbered. No globally recovered atom map or optimised geometry is implied.','tiny')
save('figure-3-initial-p4.svg',1580,620,'Notebook initial P4 functionalisation candidates',s)
# 4. Featured network preserving source a/b and unresolved branches.
s=txt(30,42,'04  Alternative P–P cleavage pathways · notebook p. 4','head')+txt(30,78,'Readable topology endpoints are redrawn; ambiguous branches are retained as unresolved, not invented.','small')
s+=txt(355,134,'Notebook (1) → a','sub','middle')+txt(1080,134,'Notebook (2) → b','sub','middle')
s+=graph('opened',355,310,cut='34')+graph('opened',1080,310,cut='24')
s+=ar(355,475,355,560)+ar(1080,475,1080,560)
s+=txt(390,510,'S transfer /','small')+txt(390,541,'thiolate capture','small')+txt(1115,510,'Alternative site /','small')+txt(1115,541,'P–P cleavage','small')
s+=graph('p4-a',355,765)+graph('p4-b',1080,765)
s+=txt(355,952,'a · triangle + pendant P unit','sub','middle')+txt(1080,952,'b · four-membered P ring','sub','middle')
s+=con('M355,980 V1040 H190 V1100')+con('M355,1040 H600 V1100')+ar(1080,980,1080,1100)
s+=txt(190,1140,'p. 4 a → (1)','sub','middle')+txt(190,1180,'P₁ release + P₃ motif','small','middle')
s+=txt(600,1140,'p. 4 a → (2) / (3)','sub','middle')+txt(600,1180,'Open / branched sketches','small','middle')+txt(600,1215,'Internal edges unresolved','tiny','middle')
s+=txt(1080,1140,'p. 5 b → circled (2)','sub','middle')+txt(1080,1180,'Further open P₄ motif','small','middle')
s+=txt(30,1290,'All endpoints are notebook hypotheses. Local vertex placement is editorial; no historical P1–P4 mapping is asserted.','small')
s+=txt(30,1326,'Red edges distinguish the reconstructed cleavage choices; crowded intermediate charges are not silently repaired.','tiny')
save('figure-4-cleavage-network.svg',1450,1370,'Notebook a and b phosphorus cleavage network',s)
# 5. Distinct structural motifs, relationship arrows deliberately do not claim balanced elementary steps.
s=txt(30,43,'05  Later-stage phosphorus transformations · pp. 3–6','head')+txt(30,80,'Notebook motif relationships; not balanced elementary steps or observed intermediates.','small')
s+=txt(200,143,'P₃ ring candidate','sub','middle')+graph('P3-ring',200,320)
s+=ar(395,320,535,320,dash=True)+txt(465,230,'Opening alternatives','small','middle')
s+=txt(755,143,'Open P₃ candidate','sub','middle')+graph('P3-chain',755,320)
s+=ar(950,320,1090,320,dash=True)+txt(1020,230,'P₁ release','small','middle')
s+=graph('P1',1255,320,small=True)+txt(1420,328,'+')+graph('P2',1640,320,small=True)
s+=txt(30,525,'p. 4 a → (1): P(SPh)₃ plus a P₃ residue is one proposed fragmentation branch.','small')
s+=txt(270,620,'Open P₄ motif · p. 5 b / (2)','sub','middle')+graph('P4-chain',270,785,small=True)
s+=txt(900,620,'P₂ candidate · pp. 1–2, 6','sub','middle')+graph('P2',900,785)
s+=ar(1080,785,1300,785,dash=True)+txt(1190,710,'Further cleavage','small','middle')+txt(1415,793,'2','atom')+graph('P1',1570,785,small=True)
s+=txt(30,974,'Additional p. 4 (2)/(3) branches have ambiguous internal bonds and are documented instead of guessed.','small')
s+=txt(30,1010,'S-transfer partners / counterions are not assigned in these motif links. Dashed arrows denote unresolved relationships, not validated sequences.','tiny')
save('figure-5-later-transformations.svg',1900,1050,'Notebook later phosphorus motif and fragmentation alternatives',s)
# 6. Molecularly informed computational iteration; no energy plot.
s=txt(30,42,'06  Computational exploration','head')+txt(30,79,'Gaussian used in the project; no new calculations or validated stationary-point claims.','small')
s+=graph('P2',190,270,small=True)+txt(190,403,'Candidate structures','sub','middle')+ar(350,270,465,270)
s+=txt(510,219,'Gaussian investigations','sub')+txt(510,262,'Geometry optimisation attempts')+txt(510,304,'Possible transition-state exploration')+ar(915,270,1050,270)
s+=txt(1080,219,'Assess plausibility','sub')+txt(1080,262,'Expected connectivity?')+txt(1080,304,'Reasonable geometry?')
s+=con('M1230,360 V480 H190 V430')+txt(690,458,'Reconsider assumptions and candidate pathways','sub','middle')
s+=txt(30,562,'Some attempts did not give expected / chemically plausible structures; this does not prove a candidate impossible.','small')
s+=txt(30,602,'Page 2 energy annotations and p. 5 TS/IM labels are retained only as unverified notebook records.','tiny')
save('figure-6-computational.svg',1450,650,'Iterative Gaussian-based notebook investigation',s)
# 7. Question-linked experiments, not a forced successful sequence.
s=txt(30,42,'07  Experimental investigation of mechanistic hypotheses','head')+txt(30,80,'Parallel questions and evidence limits; not a sequence of conclusive results.','small')
for y,title,a,b in [
 (150,'NMR monitoring','Which mixtures change with time?','Project-level monitoring reported; nucleus, shifts and time points not recovered.'),
 (310,'Reagent controls','Does disulfide/base chemistry occur without P₄?','p. 1 compares phenyl / para-chlorophenyl disulfides ± KHMDS.'),
 (470,'Trapping strategies','Can a transient species be made distinguishable?','Mixed-disulfide strategy; bulky / Lewis-pair P₃ trapping plans remain incomplete.'),
 (630,'GC–MS investigation','Which candidate sulfur species could explain the peaks?','p. 1: five peaks, tentative names; no masses, spectra or definitive identities.'),
 (790,'Reassessment','Is a mixed disulfide unique evidence of an intermediate?','p. 9: background exchange / light may provide another explanation.')]:
 s+=txt(30,y,title,'sub')+txt(390,y,a)+ln(30,y+21,1390,y+21)+txt(390,y+58,b,'small')
s+=txt(30,930,'A reported PhS–N(SiMe₃)₂ assignment is not an established isolated intermediate or a complete mechanism.','tiny')
save('figure-7-experimental.svg',1450,975,'Question-linked NMR controls trapping and GCMS investigation',s)
print('Notebook audit saved first; seven SVGs generated. Ambiguous structures remain explicitly unresolved.')
