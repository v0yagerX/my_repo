"""SPX daily returns regressed on RSP + SOXX (and RSP + XLK); run from data/ dir: python3 -I ../scripts/spx_concentration.py"""
import pandas as pd, numpy as np
def ld(s):
    d=pd.read_csv(f'{s}.csv',parse_dates=['date']).set_index('date')['close']; return d[~d.index.duplicated(keep='last')]
px=pd.concat({k:ld(k) for k in ['_GSPC','RSP','SOXX','XLK']},axis=1).dropna()
r=px.pct_change().dropna()
for win in [63,126,252]:
    rr=r.iloc[-win:]
    for other in ['SOXX','XLK']:
        X=np.column_stack([np.ones(len(rr)),rr.RSP,rr[other]]); b=np.linalg.lstsq(X,rr._GSPC,rcond=None)[0]
        p=X@b; r2=1-((rr._GSPC-p)**2).sum()/((rr._GSPC-rr._GSPC.mean())**2).sum()
        print(f'{win}d: SPX = {b[1]:.2f}*RSP + {b[2]:.3f}*{other} (R2 {r2:.2f})')
