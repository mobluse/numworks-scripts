from math import *
from random import *
from time import *
def dhasimplebench():
  # Ahl's Simple Benchmark
  r=0
  s=0
  for n in range(1,101):
    a=n
    for i in range(1,11):
      a=sqrt(a); r=r+random()
    for i in range(1,11):
      a=a**2; r=r+random()
    s=s+a
  print(abs(1010-s/5))
  print(abs(1000-r))
  return (abs(1010-s/5),abs(1000-r))
def benchmark10():
  ran=0
  acc=0
  for i in range(10):
    t0=monotonic()
    b=dhasimplebench()
    acc+=b[0]
    ran+=b[1]
    print("%08.5f s"%(monotonic()-t0))
  return (acc,ran)
seed()
benchmark10()
t0=monotonic()
(acc,ran)=benchmark10()
print("Average of 10:")
print(acc/10)
print(ran/10)
print("%08.5f s"%((monotonic()-t0)/10))
