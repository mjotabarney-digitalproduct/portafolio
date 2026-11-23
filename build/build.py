#!/usr/bin/env python3
"""Static site generator: writes EN at / and ES at /es/. Run: python3 build/build.py"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from content_me import TEASER, ME, BENTO, EXPERIENCE
from content_home import SITE, NAV, HERO, STATS, STATS_ES_NUM, WORK, BEHANCE, PRINCIPLES, ABOUT, CONTACT
from content_cases import CASES, NDA, NDA_TQ

ASSETS = os.path.join(ROOT, 'assets')
missing = []

def t(x, lang): return x[lang] if isinstance(x, dict) else x
def has(rel): return os.path.exists(os.path.join(ASSETS, rel))
import hashlib
def v(rel):  # cache-busting suffix from file content
    p=os.path.join(ASSETS, rel)
    return rel + ('?v=' + hashlib.md5(open(p,'rb').read()).hexdigest()[:8] if os.path.exists(p) else '')
def num(n, lang):  # 95.7% -> 95,7% in Spanish
    if lang == 'es': n = STATS_ES_NUM.get(n, n.replace('.', ','))
    return n

def prefix(lang, depth):  # path to site root from a page
    return '../' * depth

def head(lang, title, desc, depth, alt_href, canonical_path):
    r = prefix(lang, depth)
    other = 'es' if lang == 'en' else 'en'
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#391212">
<link rel="alternate" hreflang="{other}" href="{alt_href}">
<link rel="icon" href="{r}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Instrument+Serif:ital@0;1&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/{v('css/style.css')}">
</head>
<body>
<a class="skip" href="#main">{'Skip to content' if lang=='en' else 'Saltar al contenido'}</a>
'''

def header(lang, depth, alt_href, home_href):
    links = ''.join(f'<a class="{"hide-s" if i in (1,2) else ""}" href="{home_href}{h}">{t(lbl, lang)}</a>' for i, (h, lbl) in enumerate(NAV))
    other = 'ES' if lang == 'en' else 'EN'
    return f'''<header class="site-head"><div class="wrap">
<a class="brand" href="{home_href}" aria-label="{SITE['name']}">María <em>José</em> Barney</a>
<nav class="nav" aria-label="{'Main' if lang=='en' else 'Principal'}">{links}<a class="lang" href="{alt_href}" hreflang="{other.lower()}" lang="{other.lower()}">{other}</a></nav>
</div></header>
'''

def contact(lang, depth):
    c = CONTACT
    return f'''<section class="contact" id="contact"><div class="wrap">
<span class="label">{t(c['label'], lang)}</span>
<h2>{t(c['h2'], lang)}</h2>
<div class="links">
<a class="btn solid" href="mailto:{SITE['email']}">{SITE['email']} ↗</a>
<a class="btn" href="{SITE['linkedin']}" target="_blank" rel="noopener">LinkedIn ↗</a>
<a class="btn" href="{SITE['behance']}" target="_blank" rel="noopener">Behance ↗</a>
<a class="btn" href="{prefix(None, depth)}assets/cv/{'Maria_Jose_Barney_CV_Product_Designer_Nu_ENG' if lang=='en' else 'Maria_Jose_Barney_CV_Product_Designer_2026_ESP'}.pdf" target="_blank" rel="noopener">{'CV (PDF)' if lang=='en' else 'Hoja de vida (PDF)'} ↓</a>
</div>
<div class="fine"><span>{t(c['fine_l'], lang)}</span><span>{t(c['fine_r'], lang)}</span></div>
</div></section>
'''

def foot(depth):
    return f'<script src="{prefix(None, depth)}assets/{v('js/main.js')}" defer></script>\n</body>\n</html>\n'

# ---------------------------------------------------------------- home
def home(lang):
    depth = 0 if lang == 'en' else 1
    r = prefix(lang, depth)
    alt = 'es/' if lang == 'en' else '../'
    home_href = './'
    title = f"{SITE['name']} | {t(SITE['role'], lang).replace('&amp;','&')}"
    h = head(lang, title, t(SITE['desc'], lang), depth, alt, home_href) + header(lang, depth, alt, home_href)
    meta = ''.join(f'<span>{t(m, lang)}</span>' for m in HERO['meta'])
    h += f'''<main id="main">
<section class="hero"><div class="wrap">
<div class="grid"><div>
<span class="label">{t(HERO['label'], lang)}</span>
<h1>{t(HERO['h1'], lang)}</h1>
</div><div>
<p class="dek">{t(HERO['dek'], lang)}</p>
<div class="cta"><a class="btn solid" href="#work">{t(HERO['cta1'], lang)}</a><a class="btn" href="mailto:{SITE['email']}">{t(HERO['cta2'], lang)}</a></div>
</div></div>
<div class="meta">{meta}</div>
</div></section>
'''
    B = BENTO
    tiles = ''.join(f'<div class="tile"><b>{n}</b><span>{t(l, lang)}</span></div>' for n, l in B['tiles'])
    pills = ''.join(f'<i style="--r:{rot}deg">{t(x, lang)}</i>' for x, rot in B['industries'])
    work = ''.join(f'<li>{t(x, lang)}</li>' for x in B['work_items'])
    ring = (t(B['badge'], lang) + ' · ') * 2
    h += f'''<section class="sec bento-sec" id="about"><div class="wrap"><div class="bento reveal">
<div class="b-intro"><span class="label">{t(B['label'], lang)}</span><h2>{t(B['h'], lang)}</h2><p>{t(B['p'], lang)}</p><div class="tiles">{tiles}</div></div>
<div class="b-photo"><img src="{r}assets/{v('img/me/portrait-home.jpg')}" alt="María José Barney" loading="lazy"><div class="toss">{pills}</div></div>
<div class="b-side"><div class="grp"><span class="k">{t(B['work'], lang)}</span><ul class="work">{work}</ul></div>
<div class="grp"><span class="k">{t(B['off'], lang)}</span><p class="off">{t(B['off_p'], lang)}</p></div>
<a class="badge" href="me/" aria-label="{t(B['badge'], lang)}"><svg viewBox="0 0 120 120" aria-hidden="true"><defs><path id="ring-{lang}" d="M60,60 m-44,0 a44,44 0 1,1 88,0 a44,44 0 1,1 -88,0"/></defs><text><textPath href="#ring-{lang}" textLength="272" lengthAdjust="spacing">{ring}</textPath></text></svg><i>↗</i></a></div>
</div></div></section>
'''
    cards = ''
    for i, c in enumerate(CASES, 1):
        tags = ''.join(f'<span class="pill">{t(x, lang)}</span>' for x in [c['year']] + c['tags'])
        if has(c['cover']):
            img = f'<div class="img"><img src="{r}assets/{v(c["cover"])}" alt="" loading="lazy"></div>'
        else:
            missing.append(c['cover']); img = '<div class="img ph" aria-hidden="true"></div>'
        cards += f'''<a class="card {c['color']} reveal" href="{r if lang=='en' else ''}work/{c['slug']}/">
<span class="num">0{i} / 0{len(CASES)}</span>
<div class="txt"><div class="tags">{tags}</div><h3>{t(c['title'], lang)}</h3><p>{t(c['card'], lang)}</p><span class="see">{t(WORK['see'], lang)} ↗</span></div>
{img}</a>
'''
    h += f'''<section class="sec cases" id="work"><div class="wrap">
<div class="sec-head"><span class="label">{t(WORK['label'], lang)}</span><p>{t(WORK['intro'], lang)}</p></div>
{cards}
<a class="behance reveal" href="{SITE['behance']}" target="_blank" rel="noopener">
<div><span class="label">{t(BEHANCE['label'], lang)}</span><h3>{t(BEHANCE['h'], lang)}</h3><p>{t(BEHANCE['p'], lang)}</p></div>
<span class="btn solid">{t(BEHANCE['cta'], lang)}</span>
</a>
</div></section>
'''
    slugs = {c['slug']: c for c in CASES}
    pr = ''
    for i, (ttl, body, slug) in enumerate(PRINCIPLES['items'], 1):
        ct = next(c for c in CASES if c['slug'] == slug)['title']
        see = 'See it in' if lang == 'en' else 'Verlo en'
        pr += f'''<a class="principle reveal" href="work/{slug}/"><span class="n">0{i}</span><h3>{t(ttl, lang)}</h3><p>{t(body, lang)}</p><span class="go">{see} “{t(ct, lang)}” →</span></a>'''
    h += f'''<section class="sec" id="approach"><div class="wrap">
<div class="sec-head"><span class="label">{t(PRINCIPLES['label'], lang)}</span><p>{t(PRINCIPLES['intro'], lang)}</p></div>
<div class="principles">{pr}</div>
</div></section>
'''
    E = EXPERIENCE
    yc = ''.join(f'<div class="yc{" hi" if hi else ""}"><span class="yr" aria-hidden="true">{y}</span><small>{t(w, lang)}</small><h3>{t(ro, lang)}</h3><b>{t(co, lang) if isinstance(co, dict) else co}</b><p>{t(d, lang)}</p></div>' for y, w, ro, co, d, hi in E['items'])
    h += f'''<section class="sec exp" id="experience"><div class="wrap">
<div class="exp-head"><div><span class="label">{t(E['label'], lang)}</span><h2>{t(E['h'], lang)}</h2></div></div>
<div class="ycs">{yc}</div>
</div></section>
</main>
'''
    h += contact(lang, depth) + foot(depth)
    return h

# ---------------------------------------------------------------- case
def render_block(b, lang, r):
    k = b[0]
    if k == 'p': return f'<p>{t(b[1], lang)}</p>'
    if k == 'pull': return f'<p class="pull">{t(b[1], lang)}</p>'
    if k == 'ul': return '<ul>' + ''.join(f'<li>{t(x, lang)}</li>' for x in b[1]) + '</ul>'
    if k == 'steps': return '<ol class="steps">' + ''.join(f'<li>{t(x, lang)}</li>' for x in b[1]) + '</ol>'
    if k == 'callout': return f'<div class="callout"><h4>{t(b[1], lang)}</h4>' + ''.join(f'<p>{t(x, lang)}</p>' for x in b[2]) + '</div>'
    if k == 'honest': return f'<div class="honest"><b>{t(b[1], lang)}</b>{t(b[2], lang)}</div>'
    if k == 'kpis': return '<div class="kpis">' + ''.join(f'<div class="kpi"><b>{num(n, lang)}</b><span>{t(l, lang)}</span></div>' for n, l in b[1]) + '</div>'
    if k == 'compare': return '<div class="compare">' + ''.join(f'<div><h4>{t(a, lang)}</h4><p>{t(p, lang)}</p></div>' for a, p in b[1:]) + '</div>'
    if k == 'fig':
        kind, imgs, cap = b[1], b[2], b[3]
        ok = [i for i in imgs if has(i)]
        for i in imgs:
            if not has(i): missing.append(i)
        if not ok: return ''
        frames = ''.join(f'<div class="frame"><img src="{r}assets/{v(i)}" alt="{t(cap, lang)}" loading="lazy"></div>' for i in ok)
        cls = ('combo pair' if kind == 'combo' else 'pair') if len(ok) > 1 and kind != 'bare' else kind
        inner = f'<div class="frames">{frames}</div>' if len(ok) > 1 and kind != 'bare' else frames
        return f'<figure class="{cls}">{inner}<figcaption>{t(cap, lang)}</figcaption></figure>'
    raise ValueError(k)

def case(c, idx, lang):
    depth = 2 if lang == 'en' else 3
    r = prefix(lang, depth)
    base = r + ('' if lang == 'en' else 'es/')
    alt = r + ('es/' if lang == 'en' else '') + f"work/{c['slug']}/"
    title = f"{t(c['title'], lang)} | {SITE['name']}"
    h = head(lang, title, t(c['card'], lang), depth, alt, base) + header(lang, depth, alt, base)
    tags = ''.join(f'<span class="pill">{t(x, lang)}</span>' for x in [c['year']] + c['tags'])
    facts = ''.join(f'<div><dt>{t(a, lang)}</dt><dd>{t(b, lang)}</dd></div>' for a, b in c['facts'])
    tldr = ''.join(f'<div><h4>{t(a, lang)}</h4><p>{t(b, lang)}</p></div>' for a, b in c['tldr'])
    hero_cls = c['color']
    hc = c.get('hero', c['cover'])
    cover = f'<div class="wrap"><figure class="case-cover"><div class="frame"><img src="{r}assets/{v(hc)}" alt="{t(c["title"], lang)}"></div></figure></div>' if has(hc) else ''
    back = 'All work' if lang == 'en' else 'Todos los casos'
    h += f'''<main id="main">
<section class="case-hero {hero_cls}"><div class="wrap">
<a class="back" href="{base}#work">← {back}</a>
<div class="tags">{tags}</div>
<h1>{t(c['title'], lang)}</h1>
<p class="dek">{t(c['dek'], lang)}</p>
<dl class="facts">{facts}</dl>
</div></section>
{cover}<div class="wrap"><div class="tldr">{tldr}</div></div>
<article class="article"><div class="wrap">
'''
    for i, s in enumerate(c['sections'], 1):
        body = ''.join(render_block(b, lang, r) for b in s['body'])
        h += f'''<section class="block reveal"><div class="side"><span class="n">0{i}</span>{t(s['side'], lang)}</div><div><h2>{t(s['title'], lang)}</h2>{body}</div></section>
'''
    if c['slug'] != 'xtam':
        note = NDA_TQ if c['slug'] == 'tqnet' else NDA
        h += f'<div class="block"><div></div><p class="nda">{t(note, lang)}</p></div>'
    h += '</div></article>\n'
    nxt = CASES[(idx + 1) % len(CASES)]
    nl = 'Next case' if lang == 'en' else 'Siguiente caso'
    h += f'''<a class="next" href="{base}work/{nxt['slug']}/"><div class="wrap"><span class="mono">{nl} →</span><h3>{t(nxt['title'], lang)}</h3></div></a>
</main>
'''
    h += contact(lang, depth) + foot(depth)
    return h

def me(lang):
    depth = 1 if lang == 'en' else 2
    r = prefix(lang, depth)
    base = r + ('' if lang == 'en' else 'es/')
    alt = r + ('es/' if lang == 'en' else '') + 'me/'
    title = f"{t(ME['title'], lang)} | {SITE['name']}"
    h = head(lang, title, t(ME['desc'], lang), depth, alt, base) + header(lang, depth, alt, base)
    facts = ''.join(f'<div><b>{t(a, lang)}</b><p>{t(b, lang)}</p></div>' for a, b in ME['facts'])
    now = ''.join(f'<div><span>{t(a, lang)}</span><p>{t(b, lang)}</p><small>{t(c, lang)}</small></div>' for a, b, c in ME['now'])
    ph = ''.join(f'<figure><div class="frame"><img src="{r}assets/{v("img/me/" + i + ".jpg")}" alt="{t(c, lang) if c else ""}" loading="lazy"></div>' + (f'<figcaption>{t(c, lang)}</figcaption>' if c else '') + '</figure>' for i, c in ME['photos'])
    h += f'''<main id="main">
<section class="me-hero"><div class="wrap"><div>
<a class="back" href="{base}#about">← {t(ME['back'], lang)}</a>
<h1>{t(ME['h1'], lang)}</h1>
<p>{t(ME['intro'], lang)}</p></div>
<figure class="polaroid"><img src="{r}assets/{v('img/me/portrait.jpg')}" alt="María José Barney"></figure>
</div></section>
<section class="me-sec reveal"><div class="wrap"><h2>{t(ME['facts_h'], lang)}</h2><div class="me-facts">{facts}</div></div></section>
<section class="me-now"><div class="wrap"><span class="label">{t(ME['now_label'], lang)}</span><div class="me-now-grid">{now}</div></div></section>
<section class="me-sec"><div class="wrap"><h2>{t(ME['photos_h'], lang)}</h2><p class="me-lede">{t(ME['photos_lede'], lang)}</p><div class="me-grid">{ph}</div></div></section>
<a class="next" href="{base}#work"><div class="wrap"><span class="mono">{t(ME['end_link'], lang)} →</span><h3>{t(ME['end'], lang)}</h3></div></a>
</main>
'''
    h += contact(lang, depth) + foot(depth)
    return h

def write(path, html):
    p = os.path.join(ROOT, path); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(html)

for lang in ('en', 'es'):
    pre = '' if lang == 'en' else 'es/'
    write(pre + 'index.html', home(lang))
    write(pre + 'me/index.html', me(lang))
    for i, c in enumerate(CASES):
        write(f"{pre}work/{c['slug']}/index.html", case(c, i, lang))
print('built. missing images:', sorted(set(missing)) or 'none')
