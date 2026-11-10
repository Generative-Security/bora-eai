# Illustrative Monte Carlo for BORA-EAI worked example (customer-service chatbot).
# All inputs are invented for illustration. Requires numpy. Run: python worked_example_simulation.py
import numpy as np
rng = np.random.default_rng(2026)
N = 200_000
def pert(lo, mo, hi, size, lamb=4):
    a = 1 + lamb*(mo-lo)/(hi-lo); b = 1 + lamb*(hi-mo)/(hi-lo)
    return lo + rng.beta(a, b, size)*(hi-lo)
p_prod = pert(0.60, 0.75, 0.90, N)
p_val  = pert(0.30, 0.55, 0.80, N)
gross  = pert(350_000, 700_000, 1_100_000, N)
value  = p_prod*p_val*gross
def scen(plo,pmo,phi,median,sigma):
    p = pert(plo,pmo,phi,N); ev = rng.random(N) < p
    return np.where(ev, rng.lognormal(np.log(median), sigma, N), 0.0)
b9 = scen(0.30,0.50,0.80, 15_000, 1.2)
b7 = scen(0.20,0.40,0.60, 25_000, 1.3)
b8 = scen(0.03,0.08,0.15, 400_000, 1.0)
gov = pert(60_000, 90_000, 150_000, N)
loss = b9+b7+b8
net = value - loss - gov
f=lambda x: f"{x:,.0f}"
print("value p10/50/90", [f(v) for v in np.percentile(value,[10,50,90])], "mean", f(value.mean()))
for n,s in [("B10",b9),("B8",b7),("B9",b8)]:
    print(n, "EAL", f(s.mean()), "P95", f(np.percentile(s,95)), "P(any)", round((s>0).mean(),3))
print("total loss EAL", f(loss.mean()), "P95", f(np.percentile(loss,95)))
print("gov mean", f(gov.mean()))
print("net p10/50/90", [f(v) for v in np.percentile(net,[10,50,90])], "mean", f(net.mean()), "P(net<0)", round((net<0).mean(),3))
print("cost of delay per quarter (median value/4)", f(np.median(value)/4), "p10/p90", f(np.percentile(value,10)/4), f(np.percentile(value,90)/4))
# pre-redesign: B10 limits only in prompt -> heavier tail and higher prob
b9_pre = scen(0.50,0.70,0.90, 40_000, 1.6)
net_pre = value - (b9_pre+b7+b8) - gov
print("PRE B10 EAL", f(b9_pre.mean()), "P95", f(np.percentile(b9_pre,95)))
print("PRE net p10/50/90", [f(v) for v in np.percentile(net_pre,[10,50,90])], "P(net<0)", round((net_pre<0).mean(),3))
