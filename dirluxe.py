from kandinsky import *
def ds(s,x,y,i=0):
  if i:
    draw_string(s,x,y,"blue","yellow")
  else:
    draw_string(s,x,y,"yellow","blue")
def run(ins="input"):
  ms=["builtins","math","cmath","matplotlib.pyplot","turtle","random","kandinsky","ion","time"]
  for m in ms:
    exec("import "+m)
  ms.extend(["set","dict","list","tuple","str","int","float","1j"])
  if ins=="input":
    ins=input("Module/type: [all] ")
  if ins=="" or ins=="all":
    ins=ms
  elif ins.startswith("import "):
    ins=[ins[7:]]
  else:
    ins=[ins]
  for m in ins:
    s=m+": "
    for i in eval("dir("+m+")"):
      s+=i+" "
    s=s[:-1]+"!"
    print(s)
    first=True
    cs=""
    x=0
    for i in range(0,len(s),32):
      y=3
      fill_rect(0,0,320,240,"blue")
      for c in s[i:i+384]:
        if c=="!":
          ds(cs,x,y)
          cs=""
          i=-1
          break
        cs+=c
        if len(cs)>=32:
          ds(cs,x,y)
          cs=""
          y+=18
          if y>12*18:
            y=3
            time.sleep(.2)
            if first:
              time.sleep(4)
              first=False
      if i<0:
        break
    time.sleep(1)
    p="Press OK!"
    ds(p,23*10,11*18+3,1)
    while ion.keydown(ion.KEY_OK) or ion.keydown(ion.KEY_EXE):
      time.sleep(0.05)
    while not (ion.keydown(ion.KEY_OK) or ion.keydown(ion.KEY_EXE)):
      time.sleep(0.05)
  input(p[:-1]+" or EXE!")
run()
