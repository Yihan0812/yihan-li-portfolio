from pathlib import Path
from itertools import permutations
import json,csv,io
R=Path(__file__).resolve().parents[1]
all_edges=['12','13','14','23','24','34']
states=[
 ('P4',all_edges,[0,0,0,0],{},'White phosphorus; established starting structure','none'),
 ('I1',['13','14','23','24','34'],[1,0,0,0],{'2':-1},'Hypothetical Intermediate: anionic first-cleavage connectivity','P1–P2 broken; P1–SPh formed; P2 bears −1'),
 ('N1',['13','14','23','24','34'],[1,1,0,0],{},'Hypothetical Intermediate: neutral disulfide-capture connectivity','P2–SPh formed; thiolate regenerated'),
 ('A2',['14','23','24','34'],[2,1,1,0],{},'Candidate Pathway A: adjacent second cleavage','P1–P3 broken; P1–SPh and P3–SPh formed (net)'),
 ('B2',['13','14','23','24'],[1,1,1,1],{},'Candidate Pathway B: opposite second cleavage','P3–P4 broken; P3–SPh and P4–SPh formed (net)'),
 ('A3',['14','24','34'],[2,2,2,0],{},'Hypothetical Intermediate: star connectivity','P2–P3 broken; P2–SPh and P3–SPh formed (net)'),
 ('B3',['13','23','24'],[2,1,1,2],{},'Hypothetical Intermediate: chain connectivity','P1–P4 broken; P1–SPh and P4–SPh formed (net)'),
 ('Target',[],[3,3,3,3],{},'Four disconnected P(SPh)3 molecules; literature-supported target connectivity','All six P–P bonds replaced; 12 P–S bonds total')]
rows=[]
for name,edges,ss,charge,status,change in states:
 pp=[['P'+e[0],'P'+e[1]] for e in edges];ps=[]
 for i,n in enumerate(ss,1):
  for j in range(n):ps.append([f'P{i}',f'SPh({i}{chr(97+j)})'])
 deg=[sum(str(i) in e for e in edges)+ss[i-1] for i in range(1,5)]
 assert all(n==(2 if charge.get(str(i),0)==-1 else 3) for i,n in enumerate(deg,1))
 assert len(ps)==sum(ss)
 rows.append(dict(id=name,PP=pp,PS=ps,thiophenoxy_counts=ss,formal_charges=charge,P_coordination=deg,status=status,change=change))
# Chemical graph comparison uses P vertices coloured by SPh count and charge.
def equivalent(a,b):
 ea={tuple(sorted(e)) for e in a['PP']};eb={tuple(sorted(e)) for e in b['PP']}
 for perm in permutations(range(4)):
  m={f'P{i+1}':f'P{perm[i]+1}' for i in range(4)}
  if any(a['thiophenoxy_counts'][i]!=b['thiophenoxy_counts'][perm[i]] for i in range(4)):continue
  if {tuple(sorted((m[x],m[y]))) for x,y in ea}==eb:return True
 return False
assert not equivalent(rows[3],rows[4]);assert not equivalent(rows[5],rows[6])
# Residual N1 edges fall into two orbits under decorated-graph automorphisms.
n1=rows[2];autos=[]
for pm in permutations('1234'):
 m=dict(zip('1234',pm))
 if any(n1['thiophenoxy_counts'][int(i)-1]!=n1['thiophenoxy_counts'][int(m[i])-1] for i in '1234'):continue
 if {''.join(sorted(m[x] for x in e)) for e in ['13','14','23','24','34']}==set(['13','14','23','24','34']):autos.append(m)
orbits=[];remaining=set(['13','14','23','24','34'])
while remaining:
 e=sorted(remaining)[0];o={''.join(sorted(m[x] for x in e)) for m in autos};orbits.append(sorted(o));remaining-=o
assert orbits==[['13','14','23','24'],['34']]
meta=dict(states=rows,symmetry={'initial_P4':'All six edges equivalent; P1–P2 is one representative only.','after_N1_edge_orbits':orbits,'A3_B3':'Non-isomorphic examples (star vs chain); not an exhaustive kinetic mechanism.'},assumptions=['All P–P and P–S bonds drawn are single.','SPh groups are neutral, two-coordinate sulfur ligands (one P–S and one S–C bond).','Neutral P centres have three bonds and one lone pair. I1 P2 has two bonds, two lone pairs and formal charge −1.','The source proposes a generic thiolate/disulfide sequence. P4-specific labelled candidates are new formal connectivity hypotheses, not published intermediates or computed minima.','Initiating thiolate generation under Et3N is not assigned. Et3N is the user-specified project additive, not the KHMDS/4-chlorophenyl demonstration in Scheme 2(a).'])
(R/'data/phosphorus-connectivity.json').write_text(json.dumps(meta,indent=2)+'\n')
lines=['# Phosphorus connectivity audit','', '| State | P–P bonds | P–S bonds | Formal charges | Status / change |','|---|---|---|---|---|']
for r in rows:
 def bonds(es):return ', '.join('–'.join(e) for e in es) or 'none'
 lines.append(f"| {r['id']} | {bonds(r['PP'])} | {bonds(r['PS'])} | {r['formal_charges'] or 'all P neutral'} | {r['status']}; {r['change']} |")
lines+=['','SPh(1a), etc., are bookkeeping labels for phenylthio groups; they do not assign sulfur isotope provenance.','',*meta['assumptions'],'','Symmetry: all initial P4 edges are equivalent. After N1, {13,14,23,24} is one edge class and {34} another. The two illustrated later graphs are star and chain, not symmetry duplicates.','', 'All diagrams are connectivity drawings, not optimised geometries. Stoichiometric checks: six net disulfide additions remove six P–P bonds and produce twelve P–S bonds. C, H, P and S balance in P4 + 6 PhSSPh → 4 P(SPh)3.']
(R/'data/phosphorus-connectivity.md').write_text('\n'.join(lines)+'\n')
with (R/'data/phosphorus-connectivity.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['state','P-P bonds','P-S bonds','P coordination P1-P4','formal charges','status','change'])
 for r in rows:w.writerow([r['id'],bonds(r['PP']),bonds(r['PS']),r['P_coordination'],r['formal_charges'],r['status'],r['change']])
print('\n'.join(lines[:13]));print('Formal coordination and symmetry checks passed. Table saved BEFORE SVG rendering.')
