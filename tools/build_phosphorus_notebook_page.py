# -*- coding: utf-8 -*-
from pathlib import Path
import json,html,zipfile
from render_research import document,scientific_figure
R=Path(__file__).resolve().parents[1];D=R/'research/phosphorus'
figinfo={1:('figure-1-overall.svg',1260,625,900,'Literature-relevant overall transformation; no project yield or isolation of P(SPh)₃ is claimed. Et₃N and KHMDS hypotheses are distinguished below.'),2:('figure-2-base-hypotheses.svg',1420,1570,1100,'Notebook pp. 1–2 and 6–9: candidate sulfur activation and direct P attack. Et₃N and KHMDS give different formal charge models. A reported N–S assignment is not an established isolated intermediate.'),3:('figure-3-initial-p4.svg',1580,620,1150,'Notebook pp. 2–4: proposed electrophilic sulfur transfer, then thiolate capture and P–P opening. The highlighted bond is a local reconstruction; a global historical atom map is unavailable.'),4:('figure-4-cleavage-network.svg',1450,1370,1100,'Notebook p. 4, continuing on p. 5: alternative numbered choices and a/b motifs. Ambiguous internal bonds are retained as unresolved branches, not silently filled in. No endpoint is a validated computed or isolated intermediate.'),5:('figure-5-later-transformations.svg',1900,1050,1400,'Notebook pp. 3–6: later ring, open-chain, P₂ and P₁ motifs. Dashed arrows relate hypotheses; they are not balanced elementary equations. Unassigned transfer partners and ambiguous atom mappings remain explicit.'),6:('figure-6-computational.svg',1450,650,1050,'Conceptual reconstruction of the computational research cycle. Gaussian calculations were part of the project; no new calculations, validated transition states or numerical conclusions were generated.'),7:('figure-7-experimental.svg',1450,975,1050,'Experimental questions are linked to evidence and limitations. NMR monitoring is project-reported; the photographed record specifically preserves control lists, GC–MS notes and a background-exchange caution.')}
def fig(i):
 n,w,h,mw,cap=figinfo[i];f=dict(type='image',src='research/phosphorus/figures/'+n+'?v=notebook-2',width=w,height=h,min_width=mw,alt=cap,caption=f'Figure {i}. '+cap)
 return scientific_figure(f)+f'<p class="svg-download"><a href="research/phosphorus/figures/{n}" download>Download editable SVG ↓</a></p>'
def detail(label,body):return f'<details class="notebook-detail"><summary>{label}</summary><div>{body}</div></details>'
controls=[
 ('(p-ClC₆H₄S)₂ + KHMDS','p. 1: listed control in deuterated MeCN notation; individual run details absent','Disulfide/base activation without phosphorus'),
 ('PhSSPh + KHMDS','pp. 1, 8–9: listed; N–S assignment reported without raw identification data','Possible sulfur-transfer species and thiolate'),
 ('Both disulfides + KHMDS','p. 1 mixture (3): GC–MS note records five peaks','Distinguishable exchange / N–S candidates'),
 ('Both disulfides, no base','p. 1 entry (4) ticked; p. 9 exchange caution; no chromatogram supplied','Whether mixed-disulfide formation is base-specific'),
 ('P₄ + PhSSPh ± KHMDS','pp. 1, 8: overall notation and explicit plan; “slow” is not a measured rate','Base contribution versus background reaction'),
 ('Et₃N / PhSSPh / P-containing species','pp. 6–7: hypotheses; individual control execution not documented in photos','Sulfur activation versus direct phosphorus interaction'),
 ('P₄ + proposed N–S / thiolate pair','p. 8: plan; partner notation partly unclear','Whether putative activation species transfer reactivity to P₄')]
ct='<div class="connectivity-scroll" tabindex="0" role="region" aria-label="Experimental controls table"><table><thead><tr><th>System</th><th>Record / execution status</th><th>Question</th></tr></thead><tbody>'+''.join(f'<tr><th scope="row">{a}</th><td>{b}</td><td>{c}</td></tr>' for a,b,c in controls)+'</tbody></table></div>'
old=json.loads((R/'data/phosphorus-connectivity.json').read_text())
rows=[]
for s in old['states']:
 b=lambda es:', '.join('–'.join(e) for e in es) or 'none'
 rows.append(f'<tr><th>{s["id"]}</th><td>{b(s["PP"])}</td><td>{b(s["PS"])}</td><td>{html.escape(s["status"])}</td></tr>')
ot='<div class="connectivity-scroll" tabindex="0"><table><thead><tr><th>Earlier label</th><th>P–P bonds</th><th>P–S bonds</th><th>Conceptual status</th></tr></thead><tbody>'+''.join(rows)+'</tbody></table></div>'
oldbody='<p>This is the previously generated, literature-informed conceptual model. I1/N1/A2/B2/A3/B3 are not recovered notebook labels, verified Gaussian intermediates or experimental assignments.</p>'+ot+'<p><a href="data/phosphorus-connectivity.csv">Earlier conceptual audit (CSV) ↗</a> · <a href="phosphorus-assets/figure-2-pathways.svg">Earlier conceptual figure ↗</a></p>'
docs=['reconstructed-notes.md','reaction-systems.md','proposed-mechanisms.md','computational-exploration.md','experimental-exploration.md','research-narrative.md','website-content.md','uncertainties-and-questions.md','notebook-connectivity.md']
doclinks='<ul class="research-downloads">'+''.join(f'<li><a href="research/phosphorus/{n}">{n} ↗</a></li>' for n in docs)+'</ul>'
title='Computational and Experimental Investigation of White Phosphorus Activation'
intro='I investigated how interactions between white phosphorus, organic disulfides and bases might initiate phosphorus–sulfur bond formation and P–P cleavage. The project combined mechanistic hypotheses, Gaussian-based structural exploration and experimental investigation without establishing a definitive mechanism.'
body=f'''<header class="detail-heading wrap">
<a class="back-link" href="research.html">← Research areas</a>
<p class="eyebrow">RESEARCH 03 / PHOSPHORUS ACTIVATION</p>
<h1>{title}</h1>
<p>{intro}</p>
<p class="notebook-provenance">Reconstructed from nine notebook photographs, in the supplied order, with uncertainties retained.</p>
</header>
<div class="phosphorus-content wrap">
<nav class="figure-nav" aria-label="Research sections">
<a href="#overview">Overview</a>
<a href="#mechanisms">Mechanisms</a>
<a href="#computational">Computational</a>
<a href="#experimental">Experimental</a>
<a href="#reflection">Research Reflection</a>
</nav>
<section class="research-topic" id="overview">
<span id="figure-1">
</span>
<h2>A molecular-level mechanistic question</h2>
<p class="central-question">How can base-mediated interactions promote the transformation of white phosphorus into phosphorus–sulfur-containing compounds, and what intermediate structures and P–P cleavage pathways might be involved?</p>
<p>Published disulfide-mediated functionalisation supplies the context. The notebook explores different possible roles for organic and inorganic bases and several ways of opening or fragmenting the phosphorus framework.</p>{fig(1)}</section>
<section class="research-topic" id="mechanisms">
<span id="figure-2">
</span>
<h2>Alternative Activation Hypotheses</h2>
<p>The notebook considers Et₃N and KHMDS separately: candidate N–S species and thiolate formation, direct interactions with phosphorus-containing compounds, and additional OH⁻/base–P₄ hypotheses. The readable drawings are candidates; ambiguous charge or bond details are flagged.</p>
<div class="mechanism-explorer" aria-label="Mechanism explorer">
<div class="mechanism-tabs" role="tablist" aria-label="Mechanism views">
<button type="button" role="tab" id="tab-cleavage" aria-controls="panel-cleavage" aria-selected="true" data-panel="cleavage">P–P cleavage network</button>
<button type="button" role="tab" id="tab-et" aria-controls="panel-et" aria-selected="false" data-panel="et">Et₃N pathways</button>
<button type="button" role="tab" id="tab-k" aria-controls="panel-k" aria-selected="false" data-panel="k">KHMDS pathways</button>
</div>
<div role="tabpanel" id="panel-cleavage" aria-labelledby="tab-cleavage" data-view="cleavage">
<h3>The notebook’s a / b alternatives</h3>
<p>Page 4 distinguishes further functionalisation choices labelled (1) and (2), leading to a triangle-plus-pendant motif a and a four-membered-ring motif b. Later P₃/P₂/P₁ possibilities continue on pages 3–6. Crowded lower branches (2)/(3) remain unresolved, with no invented atom mapping.</p>{fig(4)}</div>
<div role="tabpanel" id="panel-et" aria-labelledby="tab-et" data-view="et">
<h3>Triethylamine-mediated pathways</h3>
<p>Page 6 proposes a cationic N–S/thiolate pair and alternative direct attack on a thiolated P–P candidate. Page 7 also sketches direct Et₃N–P₄ activation, whose exact adduct connectivity cannot be recovered uniquely. These are hypotheses, not detected adducts.</p>{fig(2)}</div>
<div role="tabpanel" id="panel-k" aria-labelledby="tab-k" data-view="k">
<h3>KHMDS-mediated pathways</h3>
<p>Pages 1–2 and 8–9 consider PhS–N(SiMe₃)₂ and phenylthiolate. The notebook reports a possible N–S assignment, but the supplied record does not establish isolation or an unambiguous identification. “Route 1” separately explores amide-anion attack at a P–P-containing candidate.</p>
<p>
<a href="research/phosphorus/figures/figure-2-base-hypotheses.svg">Open the Et₃N / KHMDS comparison ↗</a>
</p>{fig(3)}</div>
</div>{detail('Supporting scheme — initial P₄ functionalisation',fig(3))}{detail('Detailed scheme — later-stage phosphorus transformations',fig(5))}<p class="source-note">Phosphorus atoms are not consistently numbered in the notebook. Local graph indices in the audit are editorial bookkeeping, not a recovered global P1–P4 mapping. Formal valence consistency does not establish a real intermediate.</p>
</section>
<section class="research-topic" id="computational">
<span id="figure-3">
</span>
<h2>Computational Exploration of Reaction Pathways</h2>
<p>Gaussian was used to investigate candidate phosphorus-containing intermediates, alternative P–P cleavage pathways and possible transition-state structures. Several optimisation attempts did not give the expected connectivity or chemically plausible geometry. This motivated reassessment of structural hypotheses, without proving every unsuccessful candidate chemically impossible.</p>{fig(6)}{detail('Computational records and their limits','<p>Page 2 contains handwritten reactant/adduct/TS/IM energy annotations, while page 5 records TS3 / IM4 / IM5 / IM6. Units, reference conventions and validation outputs are unavailable. No barrier, energy ranking, functional, basis set or successful stationary-point validation is inferred.</p><p><a href="research/phosphorus/computational-exploration.md">Read the preserved unverified numerical annotations ↗</a></p>')}</section>
<section class="research-topic" id="experimental">
<h2>Experimental Investigation of Mechanistic Hypotheses</h2>
<h3>NMR reaction monitoring and controls</h3>
<p>The project included NMR monitoring and reagent controls. The photographed notes do not identify the nucleus, shifts or time points; the clearest surviving experimental list concerns phenyl/para-chlorophenyl disulfides with and without KHMDS. Listed controls and explicit plans are distinguished below.</p>{detail('Control mixtures, execution status and mechanistic questions',ct)}<h3>Intermediate-trapping strategies</h3>
<p>Mixed aryl disulfides were considered as distinguishable probes of sulfur-species exchange. Bulky/Lewis-pair approaches to P₃ trapping were also proposed, but the exact trapping reagent and a successfully isolated P₃ species are not established.</p>
<h3>GC–MS investigation</h3>
<p>Page 1 records five peaks for mixed-disulfide mixture (3), with tentative mixed-disulfide, N–S and parent-disulfide assignments. Page 8 reports an N–S species as “obtained”; no raw spectra or isolation evidence accompany the wording. Page 9 then recognises that background exchange, with light mentioned, limits the evidential value of mixed-disulfide detection.</p>{fig(7)}{detail('The five tentative GC–MS assignments','<ol><li>Mixed p-ClC₆H₄–S–S–Ph</li><li>p-ClC₆H₄–S–N(SiMe₃)₂</li><li>PhS–N(SiMe₃)₂</li><li>Bis(para-chlorophenyl) disulfide</li><li>Diphenyl disulfide</li></ol><p>No masses, retention times, fragmentation patterns or reference matches were supplied. These are notebook assignments, not definitive compound identifications or evidence of a phosphorus intermediate.</p>')}</section>
<section class="research-topic" id="reflection">
<h2>Research Reflection</h2>
<p>The work developed through mechanistic proposal, computational exploration, experimental comparison and reassessment. This is a conceptual research cycle, not an invented chronological log. The surviving notes show how apparently useful evidence—such as mixed-disulfide formation—can require a more discriminating control before supporting a mechanistic claim.</p>
<p>The detailed activation sequence and the identities of phosphorus-containing intermediates remained unresolved. The page therefore presents the questions, candidate structures and evidence limits that shaped the investigation.</p>
</section>
<section class="research-topic" id="supplement">
<h2>Notebook reconstruction and supplementary material</h2>
<p>
<a class="explore-research" href="research/phosphorus/Research_03_notebook_package.zip" download>Download reconstruction, seven SVGs and editable structures ↓</a>
</p>{detail('Page-by-page reconstruction and research documents',doclinks)}{detail('Notebook-derived motif audit','<p>The new motif audit distinguishes source-derived topology readings, ambiguous branches and local editorial indices.</p><p><a href="research/phosphorus/notebook-connectivity.md">Notebook motif audit ↗</a> · <a href="research/phosphorus/notebook-connectivity.json">Machine-readable connectivity ↗</a></p>')}{detail('Earlier conceptual connectivity model — not notebook reconstruction',oldbody).replace('<details ', '<details id="connectivity" ',1)}</section>
<section class="research-topic" id="source">
<h2>Literature and provenance</h2>
<p>The primary project source is the nine supplied notebook photographs and the accompanying project description. Raw photographs are retained locally; public downloads contain the English reconstruction and redrawn schemes. Neither the sketches nor the reconstruction establish a definitive mechanism.</p>
<p>Literature context: Horsley Downie et al., <cite>Closing the Loop: Low-Waste Phosphorus Functionalization Enabled by Simple Disulfides</cite>, ChemSusChem 18, e202401895. <a href="https://doi.org/10.1002/cssc.202401895">DOI ↗</a> · <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11960583/">Open-access article ↗</a>. The published generic thiolate/P–P-cleavage motif is separate from the notebook’s alternative hypotheses. Scheme 2(a)’s KHMDS/4-chlorophenyl example is not evidence of project yield or isolation.</p>
</section>
</div>'''
page=document(title,intro,body,'phosphorus-page notebook-page').replace('<script src="research.js"','<link rel="stylesheet" href="phosphorus.css?v=notebook-2"><script src="phosphorus.js" defer></script><script src="research.js"')
page=page.replace('href="nanopore.html" aria-current="page"','href="research.html" aria-current="page"').replace('<a href="nanopore.html">Research overview</a>','<a href="research.html">Research areas</a>')
(R/'white-phosphorus.html').write_text(page)
# Preserve historical build entry point; routine builds regenerate the updated page.
print('Updated existing Research 03 page with notebook-led narrative and progressive mechanism explorer.')
