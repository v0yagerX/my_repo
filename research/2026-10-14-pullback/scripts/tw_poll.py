import json, sys, datetime, urllib.request, os, re, html
seen_path = sys.argv[1]
seen = set(open(seen_path).read().split('\n')) if os.path.exists(seen_path) else set()
out = []
def get(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    return urllib.request.urlopen(req, timeout=20).read().decode('utf-8', 'ignore')
for c in ['tw_stock', 'headline']:
    try:
        d = json.loads(get(f'https://api.cnyes.com/media/api/v1/newslist/category/{c}?limit=40'))
        for it in d.get('items', {}).get('data', []):
            t = it.get('title') or ''
            key = 'cnyes' + str(it.get('newsId'))
            if key in seen or not ('台積' in t or '魏哲家' in t or '黃仁昭' in t): continue
            seen.add(key)
            ts = datetime.datetime.fromtimestamp(it.get('publishAt', 0), datetime.UTC).strftime('%H:%M')
            out.append(f'{ts} cnyes {it.get("newsId")} {t}')
    except Exception: pass
for u in ['https://tw.stock.yahoo.com/rss?category=tw-market', 'https://tw.stock.yahoo.com/rss?category=news']:
    try:
        s = get(u)
        for it in re.findall(r'<item>(.*?)</item>', s, re.S):
            t = re.search(r'<title>(.*?)</title>', it, re.S); l = re.search(r'<link>(.*?)</link>', it, re.S); d = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
            t = html.unescape(re.sub(r'<!\[CDATA\[|\]\]>', '', t.group(1))) if t else ''
            link = l.group(1).strip() if l else ''
            if link in seen or not ('台積' in t or '魏哲家' in t or '黃仁昭' in t): continue
            seen.add(link)
            out.append(f'{d.group(1)[17:22] if d else ""} yahoo {t} | {link}')
    except Exception: pass
open(seen_path, 'w').write('\n'.join(seen))
for o in sorted(out): print(o, flush=True)
