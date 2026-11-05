from pathlib import Path
import json,xml.etree.ElementTree as E,zipfile
R=Path(__file__).resolve().parents[1];D=R/'research/phosphorus';S=D/'structures';S.mkdir(exist_ok=True)
def cml(name,atoms,bonds,label):
 root=E.Element('cml',xmlns='http://www.xml-cml.org/schema');mol=E.SubElement(root,'molecule',id=name,title=label);aa=E.SubElement(mol,'atomArray')
 for id,el,q,h in atoms:
  a={'id':id,'elementType':el,'formalCharge':str(q)}
  if h is not None:a['hydrogenCount']=str(h)
  E.SubElement(aa,'atom',a)
 ba=E.SubElement(mol,'bondArray')
 for n,(a,b,o) in enumerate(bonds,1):E.SubElement(ba,'bond',id=f'b{n}',atomRefs2=a+' '+b,order=str(o))
 E.SubElement(mol,'description').text='Connectivity-only editable chemical record. No 3D/optimised coordinates. Notebook candidate status and mapping limitations in reconstruction.'
 E.indent(root);(S/(name+'.cml')).write_text(E.tostring(root,encoding='unicode')+'\n')
def phenyl(atoms,bonds,prefix,connect):
 for i in range(6):atoms.append((prefix+str(i+1),'C',0,0 if i==0 else 1))
 bonds.append((connect,prefix+'1',1))
 for i in range(6):bonds.append((prefix+str(i+1),prefix+str((i+1)%6+1),2 if i%2==0 else 1))
M=json.loads((D/'notebook-connectivity.json').read_text())['models']
for name,m in M.items():
 ats=[(f'P{i}','P',m['q'].get(str(i),0),0) for i in range(1,len(m['S'])+1)];bs=[('P'+e[0],'P'+e[1],1) for e in m['PP']]
 for i,count in enumerate(m['S'],1):
  for j in range(count):
   sid=f'S{i}_{j}';ats.append((sid,'S',0,0));bs.append((f'P{i}',sid,1));phenyl(ats,bs,f'Ph{i}_{j}_',sid)
 cml('motif-'+name,ats,bs,'Notebook motif '+name+'; hypothetical / interpreted, local indices only')
for name,kind in [('diphenyl-disulfide','SS'),('phenylthiolate','Sminus'),('N-phenylthio-bis-trimethylsilylamine-candidate','NS'),('triethyl-sulfenylammonium-candidate','EtNS')]:
 ats=[];bs=[]
 if kind=='SS':
  ats=[('S1','S',0,0),('S2','S',0,0)];bs=[('S1','S2',1)];phenyl(ats,bs,'Ph1_','S1');phenyl(ats,bs,'Ph2_','S2')
 elif kind=='Sminus':ats=[('S1','S',-1,0)];phenyl(ats,bs,'Ph_','S1')
 else:
  ats=[('N1','N',1 if kind=='EtNS' else 0,0),('S1','S',0,0)];bs=[('N1','S1',1)];phenyl(ats,bs,'Ph_','S1')
  for i in range(3 if kind=='EtNS' else 2):
   if kind=='NS':
    si='Si'+str(i);ats.append((si,'Si',0,0));bs.append(('N1',si,1))
    for j in range(3):c=f'C{i}_{j}';ats.append((c,'C',0,3));bs.append((si,c,1))
   else:
    a=f'Et{i}a';b=f'Et{i}b';ats.extend([(a,'C',0,2),(b,'C',0,3)]);bs.extend([('N1',a,1),(a,b,1)])
 cml(name,ats,bs,name+'; use candidate status for N–S species')
(S/'README.md').write_text('# Editable chemical connectivity files\n\nCML files contain explicit P/S/N/Si/C connectivity and formal charges, with phenyl groups expanded. They have no calculated coordinates. `motif-*` files are notebook topology readings or hypothetical structures; they are not real optimised/isolated species. Atom IDs are local editing identifiers, not a recovered notebook atom map. N–S candidate files do not imply chemical identification. These files can be edited in CML-capable chemical software; SVGs remain the publication-layout source.\n')
with zipfile.ZipFile(D/'Research_03_notebook_package.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in D.rglob('*'):
  if p.is_file() and p.suffix in ['.md','.json','.svg','.cml'] and 'source-notes' not in p.parts and p.name!='source-manifest.json':z.write(p,p.relative_to(D))
 for f in ['phosphorus-connectivity.md','phosphorus-connectivity.json','phosphorus-connectivity.csv']:z.write(R/'data'/f,'earlier-conceptual-model/'+f)
 z.writestr('README.txt','Nine notebook photographs were confirmed as the intended corpus. Raw photos are excluded. Main figures and reconstruction derive from the notebook; ambiguous branches remain unassigned. The earlier conceptual model is supplementary and is not a reconstruction of Gaussian results or experimental intermediates. No new calculations were run. No definitive mechanism is claimed.')
print('Created editable CML records and a public package excluding all raw photographs.')
