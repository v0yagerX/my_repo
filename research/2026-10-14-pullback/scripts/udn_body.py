import re, html, sys
s = open(sys.argv[1], encoding='utf-8', errors='ignore').read()
m = re.search(r'"datePublished"\s*:\s*"([^"]+)"', s); print('published', m.group(1) if m else None)
m = re.search(r'<title>(.*?)</title>', s, re.S); print('title', html.unescape(m.group(1)).strip() if m else None)
idx = [m.start() for m in re.finditer('即時報導', s)]
i = idx[-1] if idx else 0
chunk = s[i:i+15000]
t = re.sub(r'<script.*?</script>', '', chunk, flags=re.S)
t = re.sub(r'<style.*?</style>', '', t, flags=re.S)
t = re.sub(r'<[^>]+>', '\n', html.unescape(t))
t = re.sub(r'\n\s*\n+', '\n', t)
print(t.split('※ 歡迎用')[0].split('延伸閱讀')[0][:3000])
