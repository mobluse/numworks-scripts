import time
from kandinsky import *
from turtle import *
n=""
def run():
  global n
  s="Rainbow Spiral"
  colors=("red","purple","blue","green","orange","yellow")
  print(s)
  d=""
  if len(n):
    d="("+n+") "
  ns=n
  n=input("Closed Caption: "+d)
  if not len(n):
    n=ns
  print("CC is \""+n+"\".")
  time.sleep(2)
  t0 = time.monotonic()
  reset()
  speed(0)
  pu()
  ht()
  fill_rect(0,0,320,222,"black")
  draw_string(n,5,200,colors[2],colors[5])
  p=pos()
  w=(-140,85)
  goto(w)
  write(s)
  goto(p)
  pd()
  for i in range(210):
    color(colors[i%6])
    width(i//50+1)
    fd(i)
    lt(59)
  pu()
  draw_string(n,5,200,colors[2],colors[5])
  goto(w)
  seth(0)
  write(s)
  pd()
  t1=time.monotonic()
  print(t1-t0)
run()
