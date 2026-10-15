import pandas as pd, numpy as np
A='/tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad/analysis/'
T=pd.read_csv(A+'semis_leadership_returns.csv')
f=lambda x: f'{x:+.1f}' if pd.notna(x) else 'n/a'
print('| Group | Sym | Last | Since Jun 22 | Since Oct 6 | Since Oct 8 | 1w | 1m | 3m | YTD | From 52w high (close) | 52w high date | vs 50d | vs 200d |')
print('|---|---|---|---|---|---|---|---|---|---|---|---|---|---|')
for _,r in T.iterrows():
    print(f"| {r.group} | {r.sym} | {r['last']:.2f} | {f(r.jun22)} | {f(r.oct6)} | {f(r.oct8)} | {f(r.w1)} | {f(r.m1)} | {f(r.m3)} | {f(r.ytd)} | {f(r.dd52)} | {r.hi52d} | {f(r.vs50)} | {f(r.vs200)} |")
print()
num=['jun22','oct6','oct8','w1','m1','m3','ytd','dd52','vs50','vs200']
G=T[T.group!='ETFs/Index'].groupby('group',sort=False)[num].median()
print('| Group (median) | Since Jun 22 | Since Oct 6 | Since Oct 8 | 1w | 1m | 3m | YTD | From 52w high | vs 50d | vs 200d |')
print('|---|---|---|---|---|---|---|---|---|---|---|')
for g,r in G.iterrows():
    print(f"| {g} | "+' | '.join(f(r[c]) for c in num)+' |')
