#!/usr/bin/env python3
"""Small release check for metadata, local links, and public asset boundaries."""
from html.parser import HTMLParser
from pathlib import Path
import json
import re
import xml.etree.ElementTree as ET
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://kostia7alania.github.io/jardulik-companion-site/'


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.headings = []
        self.links = []
        self.images = []
        self.ids = set()
        self.canonical = []
        self.description = []
        self.noindex = False
        self.title = ''
        self.in_title = False
        self.json_ld = []
        self.in_json = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'html':
            assert attrs.get('lang') == 'ru', 'Expected Russian page language'
        if tag == 'title':
            self.in_title = True
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self.headings.append(int(tag[1]))
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, f'Duplicate ID {attrs["id"]}'
            self.ids.add(attrs['id'])
        if tag == 'meta' and attrs.get('name') == 'description':
            self.description.append(attrs.get('content', ''))
        if tag == 'meta' and attrs.get('name') == 'robots':
            self.noindex = 'noindex' in attrs.get('content', '')
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical.append(attrs['href'])
        for name in ['href', 'src']:
            if attrs.get(name):
                self.links.append(attrs[name])
        if tag == 'img':
            self.images.append(attrs)
        if tag == 'script' and attrs.get('type') == 'application/ld+json':
            self.in_json = True

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
        if tag == 'script':
            self.in_json = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self.in_json:
            self.json_ld.append(data)


pages = {}
for path in sorted(ROOT.glob('*.html')):
    page = Page()
    source = path.read_text()
    assert source.lower().startswith('<!doctype html>'), f'{path.name}: missing doctype'
    assert 'name="viewport"' in source, f'{path.name}: missing viewport'
    assert not re.search(r'tgWebAppData=|Bearer\s+[A-Za-z0-9]|\d{8,}:[A-Za-z0-9_-]{30,}', source), f'{path.name}: possible auth material'
    page.feed(source)
    assert page.title.strip(), f'{path.name}: missing title'
    assert page.headings.count(1) == 1, f'{path.name}: expected one H1'
    previous = 0
    for heading in page.headings:
        assert heading <= previous + 1, f'{path.name}: skipped heading level'
        previous = heading
    if not page.noindex:
        expected = BASE if path.name == 'index.html' else BASE + path.name
        assert page.canonical == [expected], f'{path.name}: bad canonical'
        assert len(page.description) == 1 and page.description[0], f'{path.name}: missing description'
    for image in page.images:
        assert 'alt' in image and 'width' in image and 'height' in image, f'{path.name}: image missing alt/dimensions'
    if page.json_ld:
        json.loads(''.join(page.json_ld))
    pages[path.name] = page

assert len({page.title for page in pages.values()}) == len(pages), 'Page titles must be unique'
for name, page in pages.items():
    for link in page.links:
        parsed = urlsplit(link)
        if parsed.scheme or parsed.netloc:
            continue
        target = (ROOT / unquote(parsed.path or name)).resolve()
        assert target.is_relative_to(ROOT), f'{name}: link outside project'
        if target.is_dir():
            target /= 'index.html'
        assert target.is_file(), f'{name}: broken local link {link}'
        if parsed.fragment and target.suffix == '.html':
            assert parsed.fragment in pages[target.name].ids, f'{name}: broken anchor {link}'

ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
locations = [x.text for x in ET.parse(ROOT / 'sitemap.xml').findall('s:url/s:loc', ns)]
expected_locations = {BASE if name == 'index.html' else BASE + name for name, page in pages.items() if not page.noindex}
assert set(locations) == expected_locations, 'Sitemap does not match indexable pages'
assert (ROOT / '.nojekyll').exists(), 'Missing .nojekyll'
assert (ROOT / 'assets/fonts/OFL.txt').exists(), 'Missing font license'
print(f'OK: {len(pages)} HTML pages, local links/anchors, metadata, JSON-LD, sitemap, asset boundaries')
