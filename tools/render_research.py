"""Reusable static layouts for the overview and research detail pages."""
from html import escape
import json,re

def document(title,description,body,kind):
 return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)} | Yihan Li</title><meta name="description" content="{escape(description)}"><meta name="theme-color" content="#183e36"><link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="styles.css"><link rel="stylesheet" href="research.css"><script src="research.js" defer></script></head>
<body class="research-page {kind}"><a class="skip" href="#main">Skip to content</a><header class="header wrap"><a class="wordmark" href="index.html" aria-label="Yihan Li, home">Yihan Li<span> / </span></a><nav aria-label="Main navigation"><a href="nanopore.html" aria-current="page">Research</a><a href="index.html#about">About</a><a href="index.html#contact">Contact ↗</a></nav><a class="cv-link" href="assets/Yihan_Li_CV_2026.pdf" download>Download CV ↓</a></header>
<main id="main">{body}</main><footer class="wrap"><a class="wordmark" href="index.html">Yihan Li<span> / </span></a><a href="nanopore.html">Research overview</a><a href="#main">Back to top ↑</a></footer></body></html>'''

def detail_figure(f,number):
 caption=re.sub(r'<span>Figure \d+</span>',f'<span>Figure {number:02}</span>',f[2])
 return f'<figure class="science-figure"><a href="research-assets/{f[0]}.svg" target="_blank" rel="noopener" aria-label="Open full-size figure: {escape(f[1])}"><img src="research-assets/{f[0]}.svg" alt="{escape(f[1])}" loading="lazy"></a><figcaption>{caption}</figcaption></figure>'

def overview_entry(entry):
 n=entry['number'];name=entry['figure'];title=escape(entry['title'])
 return f'''<article class="research-entry" id="{entry['id']}" aria-labelledby="entry-{n}"><header class="entry-heading"><span class="entry-number">{n}</span><div><p class="eyebrow">{escape(entry['institution'])}</p><h2 id="entry-{n}">{title}</h2></div></header><div class="entry-layout"><figure class="overview-figure"><a href="{entry['route']}" aria-label="Explore {title}"><picture><source media="(max-width: 600px)" srcset="research-assets/{name}-mobile.svg"><img src="research-assets/{name}.svg" alt="{escape(entry['alt'])}" {'fetchpriority="high"' if n=='01' else 'loading="lazy"'}></picture></a><figcaption>{entry['caption']}</figcaption></figure><div class="entry-copy"><p>{entry['description']}</p><a class="explore-research" href="{entry['route']}" aria-label="Explore Research: {title}">Explore Research <span aria-hidden="true">→</span></a><p class="research-status">{entry['status']}</p></div></div></article>'''

def references(page,data):
 refs=[r for r in data['references'] if r['id'] in page['refs']]
 items=''.join(f'<li id="ref-{r["id"]}" value="{r["id"]}"><a href="{r["url"]}">{r["title"]} ↗</a><p>{r["detail"]}</p></li>' for r in refs)
 return f'''<section class="research-topic references" id="references"><p class="eyebrow">SOURCES & ATTRIBUTION</p><h2>Sources and research context</h2><p>{page['provenance']}</p><details class="research-detail"><summary>Supplied presentation sources</summary><div><p>Yihan Li, <cite>Nanopore-Based DNA Barcode Quantification Towards Early Disease Detection</cite>, MSci project presentation, Imperial College London (2026).</p><p>Minghui Qi, <cite>Multiplexed and Multimodal Liquid Biopsy for Early-Stage Disease (Cancer) Detection Using the Oxford Nanopore Platform</cite>, viva presentation, Imperial College London (2026), supervisor Joshua Edel. Broader group concepts and proposals are not attributed as Yihan Li’s individual experimental contributions.</p></div></details><ol>{items}</ol><p class="source-note">All scientific schematics are original conceptual illustrations. No unpublished experimental data or numerical performance results are reproduced.</p></section>'''

def render_site(root):
 data=json.loads((root/'data/nanopore.json').read_text());overview=data['overview']
 body=f'''<header class="overview-heading wrap"><a class="back-link" href="index.html#research">← Research portfolio</a><p class="eyebrow">RESEARCH OVERVIEW</p><h1>{overview['title']}</h1><p class="research-focus">{overview['focus']}</p><p class="parallel-note">Two independent ONT research directions, alongside a separate solid-state sensing experience.</p></header><div class="overview-entries wrap">'''+''.join(overview_entry(e) for e in overview['entries'])+'</div>'
 (root/'nanopore.html').write_text(document(overview['title'],overview['focus'],body,'research-overview'))
 for page in data['pages']:
  nav=''.join(f'<a href="#{s["id"]}"><span>{i:02}</span>{s["nav"]}</a>' for i,s in enumerate(page['sections'],1))
  sections=[];figcount=0
  for i,s in enumerate(page['sections'],1):
   figs=''
   for f in s['figures']:figcount+=1;figs+=detail_figure(f,figcount)
   lead=f'<p class="topic-lead">{s["lead"]}</p>' if s['lead'] else ''
   sections.append(f'<section class="research-topic" id="{s["id"]}" aria-labelledby="{s["id"]}-title"><header class="topic-header"><p class="eyebrow">{i:02} / {escape(page["title"])}</p><h2 id="{s["id"]}-title">{s["title"]}</h2>{lead}</header>{s["body"]}{figs}{s["after"]}</section>')
  other=''.join(f'<a href="{e["route"]}">{escape(e["title"])} ↗</a>' for e in overview['entries'] if e['route']!=page['route'])
  body=f'''<header class="detail-heading wrap"><a class="back-link" href="nanopore.html">← Back to Research</a><p class="eyebrow">{page['kicker']}</p><h1>{page['title']}</h1><p>{page['intro']}</p></header><div class="research-layout wrap"><aside class="research-contents"><p class="eyebrow">ON THIS PAGE</p><nav aria-label="Research contents">{nav}</nav><a class="contents-reference" href="#references">Sources & attribution ↗</a></aside><div class="research-article">'''+''.join(sections)+references(page,data)+f'''<nav class="detail-return" aria-label="Research pages"><a class="explore-research" href="nanopore.html">← Back to Research</a><div>{other}</div></nav></div></div>'''
  (root/page['route']).write_text(document(page['title'],page['intro'],body,'research-detail-page'))
 print('Rendered research overview and three detail pages.')
