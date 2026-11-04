"""Three concept figures, with corresponding mobile compositions of the same science."""
def build_overview_figures(api):
 svg,text,line,rect,circle,arrow,strand=[api[k] for k in ['svg','text','line','rect','circle','arrow','strand']]
 G,B,R,V,INK,M,PALE=[api[k] for k in ['G','B','R','V','INK','M','PALE']]
 ENZYME='#c4b185'
 def pore(x,y,solid=False):
  s=rect(x-70,y,52,28,'#a6b6bd' if solid else '#c5d1bb')+rect(x+18,y,52,28,'#a6b6bd' if solid else '#c5d1bb')
  if not solid:
   s+=f'<path d="M{x-31} {y-13}Q{x-46} {y-39} {x-19} {y-33}L{x-9} {y+45}H{x-25}Z M{x+31} {y-13}Q{x+46} {y-39} {x+19} {y-33}L{x+9} {y+45}H{x+25}Z" fill="{G}"/>'
  s+=f'<path d="M{x} {y-61}Q{x-14} {y-44} {x} {y-27}T{x} {y+53}" fill="none" stroke="{G}" stroke-width="3"/>'
  return s
 def barcodes(x,y):
  s=text(x,y-30,'B1 · target',18,G)+strand(x,y,95,G)+text(x,y+42,'B3 · reference',18,B)+strand(x,y+67,95,B)
  return s
 def hybrid(x,y,w=120):
  return strand(x,y,w,B)+strand(x,y+24,w,R)+''.join(line(a,y+4,a,y+15,'#9eafa1',1) for a in range(x+8,x+w,12))+text(x+w+12,y+7,'3′',14,B)+text(x-24,y+31,'3′',14,R)+text(x+w+12,y+31,'5′',14,R)
 def probe(x,y):return strand(x,y,54,G)+strand(x+54,y,64,B)
 def enzyme(x,y):return rect(x-54,y-13,108,27,ENZYME,12)+text(x,y+6,'Duplex DNase',14,INK,'middle')
 # DNA overview: target + reference -> protein pore -> two sequence identities -> relative count ratio
 s=barcodes(30,91)+text(151,106,'+',22,M,'middle')+arrow(164,121,207,121)+pore(290,120)+text(290,217,'ONT sequencing',18,INK,'middle')+arrow(373,121,416,121)
 s+=text(444,76,'Sequence identity',18,INK)+text(444,118,'…ACGT…   B1',17,G,extra='font-family="monospace"')+text(444,153,'…TGCA…   B3',17,B,extra='font-family="monospace"')+arrow(633,121,676,121)
 s+=text(751,112,'B1 / B3',22,INK,'middle')+text(751,146,'read ratio',17,M,'middle')+text(751,217,'Relative quantification',16,INK,'middle')
 svg('overview-quantification',860,255,s,'Reference-based DNA barcode quantification','B1 target and B3 internal reference enter the same ONT protein pore sequencing workflow. Sequence-based identity supports separate read counts and relative quantification. Calibration is required; no concentration or experimental results are shown.')
 s=barcodes(59,63)+arrow(192,85,239,85)+pore(325,86)+text(325,171,'ONT sequencing',17,INK,'middle')
 s+=arrow(219,193,219,224)+text(220,253,'Sequence identification',18,INK,'middle')+text(220,285,'…ACGT… B1     …TGCA… B3',16,G,'middle',extra='font-family="monospace"')+arrow(219,310,219,341)+text(219,374,'B1 / B3 read ratio',22,INK,'middle')+text(219,403,'Relative quantification · calibration required',15,M,'middle')
 svg('overview-quantification-mobile',440,428,s,'Reference-based DNA barcode quantification','Target barcode B1 and reference barcode B3 enter ONT sequencing. Sequence identification precedes separate read counting and calibrated relative quantification.')
 # RNA overview: three molecular panels and a separate dashed same-target loop; no exponential branch.
 s=text(127,28,'Probe + target RNA',18,INK,'middle')+text(420,28,'DNA–RNA hybrid',18,INK,'middle')+text(715,28,'Proposed DNA reporter',18,INK,'middle')
 s+=probe(64,95)+text(40,101,'5′',13,G)+text(195,101,'3′',13,B)+text(64,124,'Barcode',13,G)+text(156,124,'Recognition',13,B,'middle')+strand(118,165,64,R)+text(96,172,'3′',13,R)+text(195,172,'5′',13,R)+text(148,202,'Target RNA',15,R,'middle')
 s+=arrow(229,106,278,106)+strand(306,95,54,G)+text(282,102,'5′',13,G)+hybrid(360,95,115)+enzyme(419,174)
 s+=arrow(521,106,570,106)+text(544,82,'Cleavage',13,M,'middle')+strand(604,95,54,G)+line(658,95,695,95,M,3,'5 5')+text(708,101,'?',20,M)+text(652,140,'Unknown endpoint',14,M,'middle')+strand(694,186,81,R)+text(673,192,'3′',13,R)+text(786,192,'5′',13,R)+text(735,221,'Same RNA',14,R,'middle')
 s+=f'<path d="M734 240V274H145V222" fill="none" stroke="{R}" stroke-width="1.6" stroke-dasharray="6 5"/><path d="M141 228L145 222L149 228" fill="none" stroke="{R}" stroke-width="1.6"/>'+rect(261,258,349,31,'#f0f3eb')+text(436,279,'Potential RNA recycling · proposed',16,R,'middle')
 svg('overview-rna',860,309,s,'Duplex DNase-mediated recognition and proposed reporter generation','A DNA probe contains a barcode and RNA recognition region. Complementary RNA forms an antiparallel hybrid with DNA. Duplex DNase acts on DNA in the hybrid. A proposed barcode reporter has an unspecified endpoint. A separate dashed loop denotes possible reuse of the same RNA, not replication. Reporter integrity and recycling are unverified.')
 s=text(220,25,'Probe + RNA',18,INK,'middle')+probe(70,70)+text(45,76,'5′',13,G)+text(201,76,'3′',13,B)+text(78,98,'Barcode',13,G)+text(181,98,'Recognition',13,B)+strand(260,70,100,R)+text(240,76,'3′',13,R)+text(371,76,'5′',13,R)+text(311,98,'Target RNA',13,R,'middle')
 s+=arrow(220,121,220,151)+text(220,183,'Antiparallel DNA–RNA hybrid',18,INK,'middle')+strand(105,219,54,G)+text(81,226,'5′',13,G)+hybrid(159,219,142)+enzyme(236,287)
 s+=arrow(220,314,220,344)+text(220,377,'Proposed barcode reporter',18,INK,'middle')+strand(112,413,92,G)+line(204,413,243,413,M,3,'4 4')+text(255,420,'?',21,M)+strand(303,413,71,R)+text(340,446,'Same RNA',13,R,'middle')
 s+=f'<path d="M338 463V493H30V69H42" fill="none" stroke="{R}" stroke-width="1.6" stroke-dasharray="6 5"/><path d="M36 65L42 69L36 73" fill="none" stroke="{R}" stroke-width="1.6"/>'+rect(76,478,278,30,'#f0f3eb')+text(215,499,'Potential RNA recycling · proposed',15,R,'middle')
 svg('overview-rna-mobile',440,526,s,'Duplex DNase-mediated RNA recognition','DNA probe and RNA form an antiparallel hybrid. The DNA recognition strand is cleaved by Duplex DNase. A barcode-containing reporter is proposed with unknown endpoint. The same RNA may recycle through the dashed pathway; no RNA replication or validated amplification is claimed.')
 # Solid-state overview: artificial aperture, molecule, voltage, and an illustrative current event.
 s=rect(45,45,330,176,'#e8efea')+rect(63,121,116,35,'#a6b6bd')+rect(217,121,139,35,'#a6b6bd')+circle(198,76,11,R)+arrow(198,93,198,192,R)
 s+=text(81,197,'Electrolyte',15,M)+text(56,28,'Artificial membrane + nanopore',18,INK)+text(293,79,'−',22,B)+text(293,204,'+',22,B)+text(303,102,'Applied',13,M)+text(303,119,'potential',13,M)
 s+=arrow(402,136,460,136)+text(506,48,'Electrical event',18,INK)+line(509,193,807,193,'#bbc8b9',1)+f'<path d="M514 93H604V159H681V93H801" fill="none" stroke="{B}" stroke-width="2.5"/>'+text(510,220,'Illustrative current blockade · time →',16,M)
 svg('overview-solid-state',860,255,s,'Solid-state nanopore sensing','A molecule passes through an artificial membrane aperture under an applied potential in electrolyte. An illustrative current blockade represents the electrical sensing principle, not a result or a specific Zhejiang experiment.')
 s=rect(40,34,360,160,'#e8efea')+rect(59,107,139,32,'#a6b6bd')+rect(237,107,145,32,'#a6b6bd')+circle(217,60,10,R)+arrow(217,76,217,169,R)+text(65,23,'Artificial membrane + pore',18,INK)+text(329,69,'−',20,B)+text(329,172,'+',20,B)+text(271,95,'Applied potential',13,M)
 s+=arrow(220,217,220,248)+text(220,281,'Electrical readout',18,INK,'middle')+line(74,389,369,389,'#bbc8b9',1)+f'<path d="M81 324H175V370H242V324H361" fill="none" stroke="{B}" stroke-width="2.5"/>'+text(220,418,'Illustrative current blockade · time →',15,M,'middle')
 svg('overview-solid-state-mobile',440,442,s,'Solid-state nanopore sensing','Molecular translocation through a generic artificial membrane pore under applied voltage creates an illustrative electrical event. No material, fabrication method or particular target is assigned.')
 print('Built three overview schematics with mobile compositions.')
