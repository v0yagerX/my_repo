import pandas as pd, numpy as np
D = '/tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad/data/'
def ld(s):
    df = pd.read_csv(D + s + '.csv', parse_dates=['date'])
    df = df.drop_duplicates('date', keep='last').set_index('date').sort_index()
    return df
spx = ld('_GSPC'); rsp = ld('RSP'); spy = ld('SPY'); vix = ld('_VIX'); v3 = ld('_VIX3M'); hyg = ld('HYG')
c = spx['close']

# 1) VIX/VIX3M at SPX drawdown troughs (>=5% close basis) since 2021-10
ratio = (vix['close'] / v3['close']).reindex(c.index).ffill()
peak = c.cummax(); dd = c / peak - 1
eps = []; in_ep = False
for d, v in dd.items():
    if not in_ep and v <= -0.05:
        in_ep = True; start_peak = peak[d]
    if in_ep and v == 0:
        seg = dd[(dd.index <= d)]
        in_ep = False
# simpler: identify episodes between new highs
highs = c[c == peak]
idx = list(highs.index)
print('== SPX >=5% drawdown episodes since 2021-10 and max VIX/VIX3M within +/-5 sessions of trough ==')
prev = idx[0]
rows = []
for h in idx[1:] + [c.index[-1]]:
    seg = c[(c.index >= prev) & (c.index <= h)]
    if len(seg) > 2:
        tr = seg.idxmin(); depth = seg.min() / seg.iloc[0] - 1
        if depth <= -0.05:
            pos = c.index.get_loc(tr)
            win = ratio.iloc[max(0, pos - 5):pos + 6]
            rows.append((prev.date(), tr.date(), round(depth * 100, 1), round(win.max(), 3), round(vix['close'].reindex(c.index).ffill().iloc[max(0,pos-5):pos+6].max(), 1)))
    prev = h
for r in rows: print(r)
print('current VIX/VIX3M', round(ratio.iloc[-1], 3))

# 2) RSP structure
r = rsp['close']
print('\n== RSP ==')
print('Aug14 close', r.loc['2026-08-14'], 'Sep3 close', r.loc['2026-09-03'], 'Oct13 close', r.loc['2026-10-13'], 'Sep30', r.loc['2026-09-30'], 'last', r.iloc[-1])
print('RSP pct from Aug14 high', round((r.iloc[-1] / r.loc['2026-08-14'] - 1) * 100, 2))
print('SPX change Aug14->now', round((c.iloc[-1] / c.loc['2026-08-14'] - 1) * 100, 2), 'RSP', round((r.iloc[-1] / r.loc['2026-08-14'] - 1) * 100, 2))
rs = (rsp['close'] / spy['close']).dropna()
print('RSP/SPY last', round(rs.iloc[-1], 4), '1y low?', round(rs.iloc[-252:].min(), 4), rs.iloc[-252:].idxmin().date(), 'pct of 1y range', round((rs.iloc[-1]-rs.iloc[-252:].min())/(rs.iloc[-252:].max()-rs.iloc[-252:].min())*100,1))

# 3) Generals without soldiers: SPX within 2% of ATH but <35% of members above 50d
b = pd.read_csv(D + 'breadth_timeseries.csv', parse_dates=['date']).set_index('date')
j = b.join(dd.rename('dd'), how='inner')
j['fwd20'] = (c.shift(-20) / c - 1).reindex(j.index) * 100
j['fwd40'] = (c.shift(-40) / c - 1).reindex(j.index) * 100
fmin40 = pd.Series([c.iloc[i:i + 41].min() / c.iloc[i] - 1 if i + 1 < len(c) else np.nan for i in range(len(c))], index=c.index) * 100
j['mae40'] = fmin40.reindex(j.index)
sig = j[(j['dd'] >= -0.02) & (j['pct_above_50d'] < 35)]
print('\n== SPX within 2% of ATH & <35% above 50d (breadth since 2025-03; current constituents) ==')
print(sig[['dd', 'pct_above_50d', 'pct_above_200d', 'fwd20', 'fwd40', 'mae40']].round(2).to_string())
sig2 = j[(j['dd'] >= -0.02) & (j['pct_above_200d'] < 50)]
print('\n== SPX within 2% of ATH & <50% above 200d ==')
print(sig2[['dd', 'pct_above_50d', 'pct_above_200d', 'fwd20', 'fwd40', 'mae40']].round(2).to_string())
print('\nmin pct_above_200d on any day SPX within 1% of ATH, before Sep 2026:')
k = j[(j['dd'] >= -0.01) & (j.index < '2026-09-01')]
print(k['pct_above_200d'].min(), k['pct_above_200d'].idxmin() if k['pct_above_200d'].notna().any() else None)

# 4) HYG 1y low while SPX within 2% of 1y high
h = hyg['close'].reindex(c.index).ffill()
hlow = h.rolling(252).min(); shigh = c.rolling(252).max()
cond = (h <= hlow * 1.0005) & (c >= shigh * 0.98)
print('\n== Days HYG at 1y closing low while SPX within 2% of 1y high (since 2022-10) ==')
cd = cond[cond].index
print([d.date() for d in cd])
for d in cd:
    i = c.index.get_loc(d)
    f20 = c.iloc[i + 20] / c.iloc[i] - 1 if i + 20 < len(c) else np.nan
    f40 = c.iloc[i + 40] / c.iloc[i] - 1 if i + 40 < len(c) else np.nan
    m40 = c.iloc[i:i + 41].min() / c.iloc[i] - 1
    print(d.date(), round(f20 * 100, 1), round(f40 * 100, 1), round(m40 * 100, 1))

# 5) Sector-ETF regression to estimate effective SPY weights (last 60 sessions)
secs = ['XLK', 'XLC', 'XLY', 'XLF', 'XLV', 'XLI', 'XLE', 'XLP', 'XLU', 'XLB', 'XLRE']
R = pd.concat({s: ld(s)['close'] for s in secs + ['SPY']}, axis=1).pct_change().dropna().iloc[-60:]
X = R[secs].values; y = R['SPY'].values
w, *_ = np.linalg.lstsq(X, y, rcond=None)
print('\n== Effective SPY weights from 60d regression on sector ETFs (no intercept) ==')
print({s: round(x * 100, 1) for s, x in zip(secs, w)}, 'sum', round(w.sum() * 100, 1))
resid = y - X @ w
print('R2', round(1 - resid.var() / y.var(), 4))
# 6) Contribution: SPX Oct6->Oct14 vs RSP
print('\nOct6->Oct14: SPX', round((c.iloc[-1]/c.loc['2026-10-06']-1)*100,2), 'RSP', round((r.iloc[-1]/r.loc['2026-10-06']-1)*100,2))
for s in secs:
    x = ld(s)['close']; print(s, round((x.iloc[-1]/x.loc['2026-10-06']-1)*100,2), end='; ')
print()
# 7) SPX realized: largest 1d decline since Jul 29
dr = c.pct_change()*100
print('SPX Oct14 ret', round(dr.iloc[-1],2), 'largest decline since', dr[dr <= dr.iloc[-1]].index[-2].date())
