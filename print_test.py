def run():
  h=input("Unicode high byte? (0x00) ")
  if len(h)==0:
    h="0"
  h=int(eval(h))
  d=256
  chmin=h*d
  chmax=(h+9)*d # +10→out of memory
  ch=chmin
  s=" "*len("0x%04X:"%ch)
  for i in range(16):
    s+="%X"%i
  while True:
    for i in range(6):
      print()
    print(s)
    for r in range(8):
      print("0x%04X:"%ch,end="")
      for c in range(16):
        print(chr(ch),end="")
        ch+=1
      print(":%02X"%((ch-1)%256))
    if input(s)=="q": break
    if ch==chmax:
      ch=chmin
run()
