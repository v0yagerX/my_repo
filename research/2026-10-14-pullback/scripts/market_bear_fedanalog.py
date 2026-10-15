"""Analog: SPX near ATH while the Fed is hiking and/or 10y yield rising fast.
Usage: python3 -I market_bear_fedanalog.py <gspc.json> <FEDFUNDS.csv> <DGS10.csv>
"""
import json, sys
import pandas as pd, numpy as np

j = json.load(open(sys.argv[1]))['chart']['result'][0]
ts = pd.to_datetime(j['timestamp'], unit='s').tz_localize('UTC').tz_convert('America/New_York').normalize().tz_localize(None)
spx = pd.Series(j['indicators']['quote'][0]['close'], index=ts).dropna()
spx = spx[~spx.index.duplicated(keep='last')].sort_index()
ff = pd.read_csv(sys.argv[2], parse_dates=['observation_date']).set_index('observation_date')['FEDFUNDS']
ff = pd.to_numeric(ff, errors='coerce').dropna()
y10 = pd.read_csv(sys.argv[3], parse_dates=['observation_date']).set_index('observation_date')['DGS10']
y10 = pd.to_numeric(y10, errors='coerce').dropna()

df = pd.DataFrame({'spx': spx})
df['ath'] = df.spx.cummax()
df['dd'] = df.spx / df.ath - 1
k = 999; cnt = []
for a, b in zip(df.spx, df.ath):
    k = 0 if a >= b else k + 1; cnt.append(k)
df['since_ath'] = cnt
df['sma200'] = df.spx.rolling(200).mean()
# monthly fed funds: use the latest *completed* month known (lag 1 month to avoid look-ahead)
ffm = ff.copy(); ffm.index = ffm.index + pd.offsets.MonthEnd(1)  # value known at end of the month
df['ff'] = ffm.reindex(df.index, method='ffill')
df['ff_chg3m'] = df['ff'] - ffm.shift(3).reindex(df.index, method='ffill')
df['y10'] = y10.reindex(df.index).ffill()
df['y10_chg63'] = df['y10'] - df['y10'].shift(63)
for h in [20, 40, 60]:
    df[f'ret{h}'] = df.spx.shift(-h) / df.spx - 1
    df[f'mae{h}'] = df.spx[::-1].rolling(h, min_periods=1).min()[::-1].shift(-1) / df.spx - 1

def declust(mask, gap=20):
    idx = df.index[mask.fillna(False).values]; out = []; last = None
    for d in idx:
        if last is None or df.index.get_loc(d) - df.index.get_loc(last) >= gap:
            out.append(d); last = d
    return out

def report(label, dates, show=False):
    s = df.loc[dates]
    print(f'\n{label}: n={len(s)}')
    for h in [20, 40, 60]:
        r = s[f'ret{h}'].dropna() * 100; m = s[f'mae{h}'].dropna() * 100
        if len(r) == 0: continue
        print(f'  {h}d: n={len(r)} median ret {r.median():+.1f}%, %pos {(r>0).mean()*100:.0f}%, median MAE {m.median():.1f}%, '
              f'MAE<-5%: {(m<-5).mean()*100:.0f}%, MAE<-10%: {(m<-10).mean()*100:.0f}%, worst {m.min():.1f}%')
    if show:
        print(s[['spx','dd','ff','ff_chg3m','y10_chg63','ret60','mae60']].assign(dd=lambda x:(x.dd*100).round(1), ret60=lambda x:(x.ret60*100).round(1), mae60=lambda x:(x.mae60*100).round(1)).round(2).to_string())

base = (df.dd > -0.025) & (df.dd <= -0.005) & (df.since_ath <= 10) & (df.spx > df.sma200)
s = df.index >= '1962-03-01'
report('BASE 1962+: SPX 0.5-2.5% below ATH, ATH within 10 sessions, >200d', declust(base & s))
hike = base & (df.ff_chg3m >= 0.20) & s
report('HIKING: BASE + fed funds up >=20bp vs 3 months earlier', declust(hike), show=True)
yld = base & (df.y10_chg63 >= 0.50) & s
report('YIELD SHOCK: BASE + 10y up >=50bp over 63 sessions', declust(yld), show=True)
both = base & (df.ff_chg3m >= 0.20) & (df.y10_chg63 >= 0.50) & s
report('BOTH', declust(both), show=True)
print('\nlatest:', df.iloc[-1][['spx','dd','since_ath','ff','ff_chg3m','y10','y10_chg63']].to_dict())
