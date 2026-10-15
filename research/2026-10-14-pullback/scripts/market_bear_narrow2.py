"""Robustness of narrow-leadership analog. Usage: python3 -I market_bear_narrow2.py <gspc.json> <RSP.csv>"""
import json, sys, pandas as pd, numpy as np
j = json.load(open(sys.argv[1]))['chart']['result'][0]
ts = pd.to_datetime(j['timestamp'], unit='s').tz_localize('UTC').tz_convert('America/New_York').normalize().tz_localize(None)
spx = pd.Series(j['indicators']['quote'][0]['close'], index=ts).dropna(); spx = spx[~spx.index.duplicated(keep='last')].sort_index()
rsp = pd.read_csv(sys.argv[2], parse_dates=['date']).set_index('date')['close']; rsp = rsp[~rsp.index.duplicated(keep='last')]
df = pd.concat({'spx': spx, 'rsp': rsp}, axis=1, sort=True).dropna()
df['ath'] = spx.cummax().reindex(df.index); df['dd'] = df.spx/df.ath-1
k=999; c=[]
for a,b in zip(df.spx, df.ath):
    k = 0 if a>=b else k+1; c.append(k)
df['since']=c; df['sma200']=df.spx.rolling(200).mean()
df['rsp_dd']=df.rsp/df.rsp.rolling(252,min_periods=60).max()-1
rs=df.rsp/df.spx; df['rs_lo']=rs<=rs.rolling(252,min_periods=120).min()*1.01
for h in [20,40,60]:
    df[f'ret{h}']=df.spx.shift(-h)/df.spx-1
    df[f'mae{h}']=df.spx[::-1].rolling(h,min_periods=1).min()[::-1].shift(-1)/df.spx-1
def declust(m,gap=20):
    idx=df.index[m.fillna(False).values]; out=[]; last=None
    for d in idx:
        if last is None or df.index.get_loc(d)-df.index.get_loc(last)>=gap: out.append(d); last=d
    return out
def rep(lbl,m):
    s=df.loc[declust(m)]
    print(f'\n{lbl}: n={len(s)}')
    for h in [20,40,60]:
        mm=s[f'mae{h}'].dropna()*100; r=s[f'ret{h}'].dropna()*100
        print(f'  {h}d n={len(mm)} median ret {r.median():+.1f}% median MAE {mm.median():.1f}% MAE<-5%: {(mm<-5).mean()*100:.0f}% MAE<-10%: {(mm<-10).mean()*100:.0f}% worst {mm.min():.1f}%')
    print(s[['spx','dd','rsp_dd','ret60','mae60']].assign(dd=lambda x:(x.dd*100).round(1),rsp_dd=lambda x:(x.rsp_dd*100).round(1),ret60=lambda x:(x.ret60*100).round(1),mae60=lambda x:(x.mae60*100).round(1)).to_string())
base=(df.dd>-0.025)&(df.dd<=-0.005)&(df.since<=10)&(df.spx>df.sma200)
rep('RSP >=3% off 52w high',base&(df.rsp_dd<=-0.03))
rep('RSP/SPY within 1% of 1y low',base&df.rs_lo)
