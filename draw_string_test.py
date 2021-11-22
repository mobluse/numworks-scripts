from kandinsky import *
from time import *
def run():
  h=input("Unicode high byte? (0x00) ")
  if len(h)==0:
    h="0"
  h=int(eval(h))
  d=256
  chmin=h*d
  chmax=(h+9)*d # +10→out of memory
  ch=chmin
  while True:
    fill_rect(0,0,320,222,"red")
    for r in range(12):
      for c in range(32):
        p=320*(ch-chmin)//(chmax-chmin)
        fill_rect(0,220,p,2,"yellow")
        fill_rect(p,220,320-p,2,"green")
        draw_string(chr(ch),10*c,18*r+2,"white","blue")
        ch+=1
        if ch==chmax:
          ch=chmin
    sleep(1)
run()
