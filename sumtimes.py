# Sum times in list
from math import *
# Sexagesimal: hh.mmss
ts=[17.00,-7.45,17.00,-8.50,
    15.50,-8.45,14.50,-8.50,
    15.50,-8.50]
def sumtimes(ts):
  sum_s=0
  for t in ts:
    ta=abs(t)
    s=3600*int(ta)
    s+=60*int(100*(ta%1))
    s+=60*((100*ta)%1)
    sum_s+=copysign(s,t)
  sum_sa=abs(sum_s)
  hh_mmss=sum_sa//3600
  temp=round(sum_sa%3600,10)
  minu=temp//60
  temp=temp%60
  hh_mmss+=minu/100+temp/10000
  hh_mmss=copysign(hh_mmss,sum_s)
  return hh_mmss
print("%.6f"%sumtimes(ts))
