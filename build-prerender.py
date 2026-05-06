#!/usr/bin/env python3
"""
OCGT static prerender — generates one HTML file per route from the master
SPA file, baking the correct <title>, <meta description>, canonical URL,
og:url and active-page CSS class into each variant.

This solves the "search-engine sees 23 competing H1s on /" SEO problem
without changing the source HTML or the SPA runtime: the SPA still works
identically client-side, but Google crawls each route's static prerender
and indexes it as a unique page.

Usage:
    python3 build-prerender.py                  # outputs to ./dist
    python3 build-prerender.py --out _site      # custom output dir

Workflow:
    1. Edit OCGT_website.html as before
    2. Run this script before deploy
    3. Upload contents of dist/ to the server (preserves /geotechnik, etc.)
"""

import argparse
import os
import re
import shutil
import sys
from pathlib import Path

# ── Source-of-truth route map. Mirror of ROUTES in OCGT_website.html. ──
ROUTES = {
    '':                        'home',
    'geotechnik':              'geotechnik',
    'bauueberwachung':         'a1',
    'vergabe':                 'a2',
    'grundwasser':             'a3',
    'beratung':                'a4',
    'reality-capture':         'rc',
    '3d-vermessung':           'b1',
    'baustellendokumentation': 'b2',
    'inspektionen':            'b3',
    'digitale-zwillinge':      'b4',
    'thermografie':            'b5',
    'multispektral':           'b6',
    'video-film':              'b7',
    'technologie':             'tech',
    'ueber-uns':               'about',
    'referenzen':              'refs',
    'kontakt':                 'contact',
    'impressum':               'impressum',
    'datenschutz':             'datenschutz',
}


def extract_meta_map(html: str) -> dict:
    """Pull the per-page META object out of OCGT_website.html so we can
    bake the right title/description into each prerendered file."""
    m = re.search(r'const META\s*=\s*\{(.*?)\n\};', html, re.DOTALL)
    if not m:
        raise SystemExit('Could not locate META = { ... } in source HTML')
    body = m.group(1)
    out = {}
    # Each entry looks like:  pageId: { de:{t:'...',d:'...'}, en:{t:'...',d:'...'} },
    pattern = re.compile(
        r"(\w+)\s*:\s*\{\s*de:\{t:'([^']*)',d:'([^']*)'\}\s*,\s*"
        r"en:\{t:'([^']*)',d:'([^']*)'\}\s*\}",
        re.DOTALL,
    )
    for pid, dt, dd, et, ed in pattern.findall(body):
        out[pid] = {'de_t': dt, 'de_d': dd, 'en_t': et, 'en_d': ed}
    return out


def html_escape(s: str) -> str:
    return (s.replace('&', '&amp;')
             .replace('"', '&quot;')
             .replace('<', '&lt;')
             .replace('>', '&gt;'))


def prerender_one(html: str, page_id: str, slug: str, meta: dict) -> str:
    """Return a copy of html with the requested page set as active and
    its title / description / canonical baked in."""
    info = meta.get(page_id, meta['home'])
    title = info['de_t']
    desc = html_escape(info['de_d'])
    canonical = 'https://ocgt.de/' + slug if slug else 'https://ocgt.de/'

    # 1) replace <title>
    html = re.sub(
        r'<title id="pg-title">.*?</title>',
        f'<title id="pg-title">{html_escape(title)}</title>',
        html, count=1)

    # 2) replace meta description
    html = re.sub(
        r'<meta id="pg-desc" name="description" content="[^"]*">',
        f'<meta id="pg-desc" name="description" content="{desc}">',
        html, count=1)

    # 3) replace canonical
    html = re.sub(
        r'<link rel="canonical" href="[^"]*">',
        f'<link rel="canonical" href="{canonical}">',
        html, count=1)

    # 4) replace og:url
    html = re.sub(
        r'<meta property="og:url" content="[^"]*">',
        f'<meta property="og:url" content="{canonical}">',
        html, count=1)

    # 5) replace og:title + twitter:title
    og_title = html_escape(title)
    html = re.sub(
        r'<meta property="og:title" content="[^"]*">',
        f'<meta property="og:title" content="{og_title}">',
        html, count=1)
    html = re.sub(
        r'<meta name="twitter:title" content="[^"]*">',
        f'<meta name="twitter:title" content="{og_title}">',
        html, count=1)

    # 6) replace og:description + twitter:description
    html = re.sub(
        r'<meta property="og:description" content="[^"]*">',
        f'<meta property="og:description" content="{desc}">',
        html, count=1)
    html = re.sub(
        r'<meta name="twitter:description" content="[^"]*">',
        f'<meta name="twitter:description" content="{desc}">',
        html, count=1)

    # 7) Mark the target page as active (.on) so it's visible without JS.
    #    First strip any existing .on class from `<div id="p-*" class="page on">`
    html = re.sub(
        r'(<div id="p-[a-z0-9-]+"\s+class="page) on(")',
        r'\1\2',
        html)
    #    Then add .on to the requested page
    html = re.sub(
        rf'(<div id="p-{re.escape(page_id)}"\s+class="page)("[ >])',
        r'\1 on\2',
        html, count=1)

    return html


def main():
    parser = argparse.ArgumentParser(description='Prerender OCGT SPA into per-route static HTML.')
    parser.add_argument('--src', default='OCGT_website.html',
                        help='Source SPA HTML file (default: OCGT_website.html)')
    parser.add_argument('--out', default='dist',
                        help='Output directory (default: dist)')
    parser.add_argument('--copy-assets', action='store_true', default=True,
                        help='Copy static assets (images, css, js, etc.) to output dir')
    args = parser.parse_args()

    root = Path(__file__).parent.resolve()
    src_path = root / args.src
    out_path = root / args.out

    if not src_path.exists():
        sys.exit(f'Source file not found: {src_path}')

    print(f'OCGT static prerender')
    print(f'  source:  {src_path.name}')
    print(f'  output:  {out_path.name}/')
    print()

    if out_path.exists():
        shutil.rmtree(out_path)
    out_path.mkdir(parents=True)

    html = src_path.read_text(encoding='utf-8')
    meta = extract_meta_map(html)
    print(f'Loaded {len(meta)} META entries\n')

    # Generate one HTML file per route
    for slug, page_id in ROUTES.items():
        rendered = prerender_one(html, page_id, slug, meta)
        if slug == '':
            target = out_path / 'index.html'
        else:
            (out_path / slug).mkdir(parents=True, exist_ok=True)
            target = out_path / slug / 'index.html'
        target.write_text(rendered, encoding='utf-8')
        size_kb = target.stat().st_size / 1024
        print(f'  ✓ /{slug or "(home)":<28} → {target.relative_to(root)}  ({size_kb:.1f} KB)')

    # Copy critical assets so the prerendered site is self-contained
    if args.copy_assets:
        print('\nCopying static assets...')
        asset_paths = [
            'Images', 'logos', 'icons', 'company_logos', 'marketing',
            '04 Videos', '250129_Logos für Kalle.svg',
            'sitemap.xml', 'robots.txt', 'manifest.webmanifest',
            'og-image.jpg', 'og-image-1200x630.jpg',
        ]
        for rel in asset_paths:
            src = root / rel
            if not src.exists():
                continue
            dst = out_path / rel
            if src.is_dir():
                shutil.copytree(src, dst, dirs_exist_ok=True)
                print(f'  ✓ {rel}/')
            else:
                shutil.copy2(src, dst)
                print(f'  ✓ {rel}')

        # Write a deployment-tuned .htaccess for dist:
        # - DirectoryIndex prefers the prerendered index.html (not the SPA file)
        # - SPA fallback rule still routes any unknown URL to the home prerender
        # - All security headers / caching / file blocks from the original
        src_ht = root / '.htaccess'
        if src_ht.exists():
            ht = src_ht.read_text(encoding='utf-8')
            # Prefer index.html first so each route's prerendered file wins
            ht = ht.replace(
                'DirectoryIndex OCGT_website.html index.html',
                'DirectoryIndex index.html OCGT_website.html')
            # Fall back to the home prerender, not the SPA master
            ht = ht.replace(
                'RewriteRule ^(.*)$ /OCGT_website.html [L]',
                'RewriteRule ^(.*)$ /index.html [L]')
            (out_path / '.htaccess').write_text(ht, encoding='utf-8')
            print('  ✓ .htaccess (deployment-tuned)')

    print(f'\nDone. {len(ROUTES)} prerendered routes written to {out_path.name}/')
    print(f'Deploy by uploading the contents of {out_path.name}/ to the web root.')


if __name__ == '__main__':
    main()
