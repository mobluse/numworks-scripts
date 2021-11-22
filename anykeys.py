import kandinsky as k
import time
import ion
def ds0(s,p):
  k.draw_string(s,p[0],p[1],"yellow","blue")
def ds1(s,p):
  k.draw_string(s,p[0],p[1],"blue","yellow")
def run():
  ks=dir(ion)
  del ks[:2]
  x,y=0,3
  cs=[]
  es=[]
  fr=k.fill_rect
  fr(0,0,320,240,"blue")
  for i in range(len(ks)):
    ks[i]=ks[i][4:]
    fr(x,y,20,19,"red")
    x+=1
    ds0(ks[i],(x,y))
    cs.append((x,y))
    es.append(eval("ion.KEY_"+ks[i]))
    if i<8:
      x+=320//8
      if i==7:
        x=0
        y+=20+10
    elif 26<=i:
      x+=320//5
      if (i-30)%5==0:
        x=0
        y+=20
    else:
      x+=320//6
      if (i-13)%6==0:
        x=0
        y+=20
        if i==25:
          y+=10
  ts=time.sleep
  ts(1)
  p="Press any keys!"
  ds1(p,((32-len(p))*10,11*18+3))
  ik=ion.keydown
  while 1:
    for i in range(len(ks)):
      if ik(es[i]):
        fr(0,11*18+3,170,18,"blue")
        ds1(ks[i],(0,11*18+3))
        ds1(ks[i],cs[i])
      else:
        ds0(ks[i],cs[i])
    ts(0.0001)
run()
