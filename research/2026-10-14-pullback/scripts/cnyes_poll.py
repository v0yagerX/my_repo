import json, sys, datetime, urllib.request, os, ssl
cats = ['tw_stock', 'headline', 'wd_stock', 'tw_stock_news']
seen_path = sys.argv[1]
seen = set(open(seen_path).read().split()) if os.path.exists(seen_path) else set()
out = []
for c in cats:
    url = f'https://api.cnyes.com/media/api/v1/newslist/category/{c}?limit=40'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        d = json.load(urllib.request.urlopen(req, timeout=20))
    except Exception as e:
        continue
    for it in d.get('items', {}).get('data', []):
        nid = str(it.get('newsId'))
        title = it.get('title') or ''
        if nid in seen: continue
        if ('台積' in title or 'TSMC' in title or '魏哲家' in title or '黃仁昭' in title):
            seen.add(nid)
            t = datetime.datetime.fromtimestamp(it.get('publishAt', 0), datetime.UTC).strftime('%H:%M')
            out.append(f'{t} {nid} {title}')
open(seen_path, 'w').write(' '.join(seen))
for o in sorted(out): print(o, flush=True)
