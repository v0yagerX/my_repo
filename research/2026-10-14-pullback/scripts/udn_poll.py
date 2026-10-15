import sys, re, html, os, urllib.request
seen_path = sys.argv[1]
seen = set(open(seen_path).read().split('\n')) if os.path.exists(seen_path) else set()
out = []
def get(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    return urllib.request.urlopen(req, timeout=20).read().decode('utf-8', 'ignore')
for u in ['https://money.udn.com/money/breaknews/1001/0/1', 'https://www.cna.com.tw/list/aall.aspx']:
    try:
        s = get(u)
        for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', s, re.S):
            t = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', html.unescape(m.group(2)))).strip()
            href = m.group(1).split('?')[0]
            if ('台積' in t or '魏哲家' in t or '黃仁昭' in t) and len(t) < 140 and href not in seen and '/story/' in href or ('/news/' in href and '台積' in t and href not in seen):
                seen.add(href); out.append(f'{t} | {href}')
    except Exception: pass
open(seen_path, 'w').write('\n'.join(seen))
for o in out: print(o, flush=True)
