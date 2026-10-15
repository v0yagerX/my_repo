import re, html, sys
s = open(sys.argv[1], encoding='utf-8', errors='ignore').read()
for k in ['datePublished', 'dateModified']:
    m = re.search(r'"' + k + r'"\s*:\s*"([^"]+)"', s); print(k, m.group(1) if m else None)
m = re.search(r'<title>(.*?)</title>', s, re.S); print('title', html.unescape(m.group(1)).strip() if m else None)
i = s.find('台北即時報導')
if i < 0: i = s.find('記者')
chunk = s[i:i+20000]
ps = re.findall(r'<p[^>]*>(.*?)</p>', chunk, re.S)
txt = '\n'.join(re.sub(r'<[^>]+>', '', html.unescape(p)).strip() for p in ps)
txt = txt.split('※ 歡迎用')[0]
print(re.sub(r'<[^>]+>', '', html.unescape(chunk[:600])).strip()[:400])
print(txt[:4000])
