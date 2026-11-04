"""Render the existing overview and detail routes using restrained academic components."""
from html import escape
import json

def document(title,description,body,kind):
 return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)} | Yihan Li</title><meta name="description" content="{escape(description)}"><meta name="theme-color" content="#ffffff"><link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="styles.css"><link rel="stylesheet" href="research.css?v=figure-first-1"><script src="research.js" defer></script></head>
<body class="research-page {kind}"><a class="skip" href="#main">Skip to content</a><header class="header wrap"><a class="wordmark" href="index.html" aria-label="Yihan Li, home">Yihan Li<span> / </span></a><nav aria-label="Main navigation"><a href="nanopore.html" aria-current="page">Research</a><a href="index.html#about">About</a><a href="index.html#contact">Contact ↗</a></nav><a class="cv-link" href="assets/Yihan_Li_CV_2026.pdf" download>Download CV ↓</a></header>
<main id="main">{body}</main><footer class="wrap"><a class="wordmark" href="index.html">Yihan Li<span> / </span></a><a href="nanopore.html">Research overview</a><a href="#main">Back to top ↑</a></footer></body></html>'''

def scientific_figure(f,number=None):
 if not f:return ''
 label=f'<span class="figure-number">Figure {number:02}.</span> ' if number else ''
 if f['type']=='image':
  src=f['src'];alt=escape(f['alt']);w=f.get('min_width',640)
  equation='<p class="figure-equation">Relative readout: N<sub>B1</sub> / N<sub>B3</sub></p>' if f.get('equation') and number is None else ''
  return f'''<figure class="science-figure"><div class="figure-scroll" tabindex="0" role="region" aria-label="{alt}. Scroll horizontally on small screens."><img src="{src}" alt="{alt}" loading="lazy" width="{f['width']}" height="{f['height']}" style="--figure-min-width:{w}px"></div>{equation}<figcaption>{label}{f['caption']} <a class="figure-open" href="{src}" target="_blank" rel="noopener">Open full-size figure ↗</a></figcaption></figure>'''
 raise ValueError('Scientific figures must be self-contained images.')

def overview_entry(e):
 n=e['number'];title=escape(e['title'])
 heading=f'<header class="entry-heading"><span class="entry-number">{n}</span><div><p class="eyebrow">{escape(e["institution"])}</p><h2 id="entry-{n}">{title}</h2></div></header>'
 copy=f'<div class="entry-copy">{heading}<p class="entry-description">{e["description"]}</p><a class="explore-research" href="{e["route"]}" aria-label="Explore Research: {title}">Explore Research <span aria-hidden="true">→</span></a></div>'
 return f'<article class="research-entry direction-{n}" id="{e["id"]}" aria-labelledby="entry-{n}">{copy}{scientific_figure(e.get("figure"))}</article>'

def references(page,data):
 refs=[r for r in data['references'] if r['id'] in page['refs']]
 items=''.join(f'<li id="ref-{r["id"]}" value="{r["id"]}"><a href="{r["url"]}">{r["title"]} ↗</a><p>{r["detail"]}</p></li>' for r in refs)
 return f'''<section class="research-topic references" id="references"><h2>Sources and figure credits</h2><p>{page['provenance']}</p><details class="research-detail"><summary>Supplied presentation sources</summary><div><p>Yihan Li, <cite>Nanopore-Based DNA Barcode Quantification Towards Early Disease Detection</cite>, MSci project presentation, Imperial College London (2026).</p><p>Minghui Qi, <cite>Multiplexed and Multimodal Liquid Biopsy for Early-Stage Disease (Cancer) Detection Using the Oxford Nanopore Platform</cite>, viva presentation, Imperial College London (2026), supervisor Joshua Edel. Broader group concepts and proposals are not attributed as Yihan Li’s individual experimental contributions.</p></div></details><ol>{items}</ol><p class="source-note">Captions identify the source and modifications for presentation figure exports. The RNA strategy is represented conceptually without assigning molecular products or cleavage sites. No unpublished experimental datasets or numerical performance results are reproduced.</p></section>'''

def render_site(root):
 d=json.loads((root/'data/nanopore.json').read_text());o=d['overview']
 body=f'''<header class="overview-heading wrap"><a class="back-link" href="index.html#research">← Research portfolio</a><p class="eyebrow">RESEARCH</p><h1>{o['title']}</h1><p class="research-focus">{o['focus']}</p>{scientific_figure(o['intro_figure'])}</header><div class="overview-entries wrap">'''+''.join(overview_entry(e) for e in o['entries'])+'</div>'
 (root/'nanopore.html').write_text(document(o['title'],o['focus'],body,'research-overview'))
 for page in d['pages']:
  nav=''.join(f'<a href="#{s["id"]}">{s["nav"]}</a>' for s in page['sections'])
  sections=[];figcount=0
  for i,s in enumerate(page['sections'],1):
   figs=''
   for f in s['figures']:figcount+=1;figs+=scientific_figure(f,figcount)
   lead=f'<p class="topic-lead">{s["lead"]}</p>' if s['lead'] else ''
   sections.append(f'<section class="research-topic" id="{s["id"]}" aria-labelledby="{s["id"]}-title"><header class="topic-header"><h2 id="{s["id"]}-title">{s["title"]}</h2>{lead}</header>{s["body"]}{figs}{s["after"]}</section>')
  other=''.join(f'<a href="{e["route"]}">{escape(e["title"])} ↗</a>' for e in o['entries'] if e['route']!=page['route'])
  body=f'''<header class="detail-heading wrap"><a class="back-link" href="nanopore.html">← Back to Research</a><p class="eyebrow">{page['kicker']}</p><h1>{page['title']}</h1><p>{page['intro']}</p></header><div class="research-layout wrap"><aside class="research-contents"><p class="eyebrow">CONTENTS</p><nav aria-label="Research contents">{nav}</nav><a class="contents-reference" href="#references">Sources & figure credits</a></aside><div class="research-article">'''+''.join(sections)+references(page,d)+f'''<nav class="detail-return" aria-label="Research pages"><a class="explore-research" href="nanopore.html">← Back to Research</a><div>{other}</div></nav></div></div>'''
  (root/page['route']).write_text(document(page['title'],page['intro'],body,'research-detail-page'))
 print('Rendered four academic research pages.')
