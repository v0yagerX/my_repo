"""Narrow-leadership analog test: SPX near ATH while equal-weight (RSP) lags.
Usage: python3 -I spx_breadth_analog.py <gspc.json> <RSP.csv> <VIX.csv> <VIX3M.csv>
"""
import json, sys
import pandas as pd, numpy as np

j = json.load(open(sys.argv[1]))['chart']['result'][0]
ts = pd.to_datetime(j['timestamp'], unit='s').tz_localize('UTC').tz_convert('America/New_York').normalize().tz_localize(None)
spx = pd.Series(j['indicators']['quote'][0]['close'], index=ts).dropna()
spx = spx[~spx.index.duplicated(keep='last')]
rsp = pd.read_csv(sys.argv[2], parse_dates=['date']).set_index('date')['close']
vix = pd.read_csv(sys.argv[3], parse_dates=['date']).set_index('date')['close']
v3m = pd.read_csv(sys.argv[4], parse_dates=['date']).set_index('date')['close']
df = pd.concat({'spx': spx, 'rsp': rsp, 'vix': vix, 'v3m': v3m}, axis=1).dropna(subset=['spx'])
df = df['2003-05-01':]
df['ath'] = spx.cummax().reindex(df.index)
df['dd'] = df.spx / df.ath - 1
df['days_since_ath'] = (df.spx >= df.ath).astype(int)
# sessions since last ATH
cnt = []; k = 999
for v in df['days_since_ath']:
    k = 0 if v == 1 else k + 1; cnt.append(k)
df['since_ath'] = cnt
df['rsp_hi'] = df.rsp.rolling(252, min_periods=60).max()
df['rsp_dd'] = df.rsp / df.rsp_hi - 1
df['rsp50'] = df.rsp.rolling(50).mean()
df['spx200'] = df.spx.rolling(200).mean()
fwd = {}
for h in [20, 40, 60]:
    df[f'ret{h}'] = df.spx.shift(-h) / df.spx - 1
    df[f'mae{h}'] = df.spx[::-1].rolling(h, min_periods=1).min()[::-1].shift(-1) / df.spx - 1

def declust(mask, gap=20):
    idx = df.index[mask.fillna(False).values]; out = []; last = None
    for d in idx:
        if last is None or df.index.get_loc(d) - df.index.get_loc(last) >= gap:
            out.append(d); last = d
    return out

def report(label, dates):
    s = df.loc[dates]
    print(f'\n{label}: n={len(s)} (de-clustered 20d)')
    for h in [20, 40, 60]:
        r = s[f'ret{h}'].dropna() * 100; m = s[f'mae{h}'].dropna() * 100
        if len(r) == 0: continue
        print(f'  {h}d: median ret {r.median():+.1f}%, %pos {(r>0).mean()*100:.0f}%, median max-adverse {m.median():.1f}%, '
              f'25th pct MAE {m.quantile(0.25):.1f}%, worst {m.min():.1f}%, share MAE worse than -5%: {(m<-5).mean()*100:.0f}%, worse than -10%: {(m<-10).mean()*100:.0f}%')
    return s

base = (df.dd > -0.025) & (df.dd < -0.005) & (df.since_ath <= 10) & (df.spx > df.spx200)
narrow = base & (df.rsp_dd <= -0.04) & (df.rsp < df.rsp50 * 1.0 + 1e9)  # rsp lagging >=4% off 52w high
narrow2 = base & (df.rsp_dd <= -0.04) & (df.rsp < df.rsp50)
calm = base & (df.vix / df.v3m < 0.95) & (df.vix < 20)
s0 = report('BASE: SPX 0.5-2.5% below ATH, ATH within 10 sessions, >200d (2003-2026)', declust(base))
s1 = report('NARROW: BASE + RSP >=4% below its 52w closing high', declust(narrow))
print(s1[['spx', 'dd', 'rsp_dd', 'ret20', 'mae20', 'mae60']].assign(dd=lambda x: (x.dd*100).round(1), rsp_dd=lambda x: (x.rsp_dd*100).round(1), ret20=lambda x: (x.ret20*100).round(1), mae20=lambda x: (x.mae20*100).round(1), mae60=lambda x: (x.mae60*100).round(1)).to_string())
s2 = report('NARROW2: BASE + RSP >=4% off high AND RSP below its 50d', declust(narrow2))
print(s2[['spx', 'dd', 'rsp_dd', 'ret20', 'mae20', 'mae60']].assign(dd=lambda x: (x.dd*100).round(1), rsp_dd=lambda x: (x.rsp_dd*100).round(1), ret20=lambda x: (x.ret20*100).round(1), mae20=lambda x: (x.mae20*100).round(1), mae60=lambda x: (x.mae60*100).round(1)).to_string())
s3 = report('CALM-VOL: BASE + VIX<20 and VIX/VIX3M<0.95 (since 2006)', declust(calm & (df.index >= '2006-08-01')))
print('\nlatest row:', df.iloc[-1][['spx', 'dd', 'since_ath', 'rsp_dd', 'rsp', 'rsp50', 'vix', 'v3m']].round(4).to_dict())
