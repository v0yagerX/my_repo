"""Long-history S&P 500 pullback base rates for the shallow-pullback (bull) brief.
Usage: python3 -I spx_pullback_bull.py <gspc.json> <DGS10_full.csv>
Episodes = intervals between successive all-time-high CLOSES. Depth = min close / prior ATH close - 1.
"""
import json, sys
import pandas as pd, numpy as np

j = json.load(open(sys.argv[1]))['chart']['result'][0]
ts = pd.to_datetime(j['timestamp'], unit='s').tz_localize('UTC').tz_convert('America/New_York').normalize().tz_localize(None)
c = pd.Series(j['indicators']['quote'][0]['close'], index=ts).dropna()
c = c[~c.index.duplicated(keep='last')]
c = c['1950-01-01':]
print('range', c.index[0].date(), c.index[-1].date(), round(c.iloc[-1], 2))

sma200 = c.rolling(200).mean()
slope200 = sma200 / sma200.shift(20) - 1
ath = c.cummax()
dd = c / ath - 1

# build episodes
is_ath = c >= ath  # new ATH close (ties count)
ath_dates = c.index[is_ath.values]
eps = []
for i in range(len(ath_dates) - 1):
    a, b = ath_dates[i], ath_dates[i + 1]
    seg = c[a:b]
    if len(seg) <= 2:
        continue
    tr = seg.idxmin(); depth = seg.min() / c[a] - 1
    eps.append(dict(ath=a, trough=tr, depth=depth, d2t=c.index.get_loc(tr) - c.index.get_loc(a),
                    t2r=c.index.get_loc(b) - c.index.get_loc(tr), complete=True,
                    above200=c[a] / sma200[a] - 1 if not np.isnan(sma200[a]) else np.nan,
                    slope200=slope200[a]))
# current ongoing episode
a = ath_dates[-1]; seg = c[a:]
eps.append(dict(ath=a, trough=seg.idxmin(), depth=seg.min() / c[a] - 1, d2t=None, t2r=None, complete=False,
                above200=c[a] / sma200[a] - 1, slope200=slope200[a]))
E = pd.DataFrame(eps)
cur = E.iloc[-1]
print('current episode: ATH', cur.ath.date(), 'depth so far %.2f%%' % (cur.depth * 100),
      'ATH vs 200d %.1f%%, 200d 20d slope %.2f%%' % (cur.above200 * 100, cur.slope200 * 100))
E = E[E.complete]

# 10y yield change over prior 63 sessions at ATH date (FRED DGS10 since 1999)
y = pd.read_csv(sys.argv[2], parse_dates=['observation_date']).set_index('observation_date')['DGS10']
y = pd.to_numeric(y, errors='coerce').dropna()
y = y.reindex(c.index, method='ffill')
E['y10_3m_chg'] = [y.get(d, np.nan) - y.shift(63).get(d, np.nan) for d in E.ath]

def table(sub, label, thr):
    s = sub[sub.depth <= -thr]
    n = len(s)
    if n == 0:
        print(label, 'n=0'); return
    d = -s.depth * 100
    bins = [3, 5, 7.5, 10, 15, 20]
    out = {f'<{b}%': round((d < b).mean() * 100, 0) for b in bins}
    print(f'{label} | reached {thr*100:.2f}% | n={n} | median final {-d.median():.1f}% | mean {-d.mean():.1f}% | '
          f'pct ending shallower than {out} | median days ATH->trough {s.d2t.median():.0f} | median trough->new ATH {s.t2r.median():.0f}')
    return s

trend = E[(E.above200 >= 0.03) & (E.slope200 > 0)]
print('\n=== 1950-2026, all ATH-to-ATH episodes ===')
for thr in [0.0128, 0.02, 0.03, 0.05]:
    table(E, 'ALL', thr)
print('\n=== Trend-intact filter at the ATH: close >=3% above 200d AND 200d rising over 20d ===')
for thr in [0.0128, 0.02, 0.03, 0.05, 0.075]:
    table(trend, 'TREND', thr)
print('\n=== Since 1999 with 10y yield +40bp or more over prior 3 months at ATH (rates-headwind subset) ===')
sub = E[(E.ath >= '1999-01-01') & (E.y10_3m_chg >= 0.40)]
for thr in [0.0128, 0.03, 0.05]:
    table(sub, 'RATES-UP', thr)
sub2 = E[(E.ath >= '1999-01-01') & (E.y10_3m_chg >= 0.40) & (E.above200 >= 0.03) & (E.slope200 > 0)]
for thr in [0.0128, 0.03, 0.05]:
    table(sub2, 'RATES-UP+TREND', thr)

# list trend episodes that reached 1.28% and went >=10%
s = trend[trend.depth <= -0.10]
print('\nTREND episodes that became >=10% corrections:')
print(s[['ath', 'trough', 'depth', 'd2t', 'above200', 'slope200']].assign(depth=lambda x: (x.depth*100).round(1), above200=lambda x: (x.above200*100).round(1), slope200=lambda x: (x.slope200*100).round(2)).to_string(index=False))
# decade split for the trend + 1.28 condition
t = trend[trend.depth <= -0.0128].copy(); t['dec'] = (t.ath.dt.year // 10) * 10
print('\nBy decade (TREND, reached 1.28%): n, median depth, pct <5%, pct >=10%')
print(t.groupby('dec').apply(lambda g: pd.Series(dict(n=len(g), med=round(g.depth.median()*100,1), lt5=round((g.depth>-0.05).mean()*100), ge10=round((g.depth<=-0.10).mean()*100)))).to_string())
