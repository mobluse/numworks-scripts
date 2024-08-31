n={0,8,9,10,13}
for i in sorted(list(n)):
  print(i,"["+chr(i)+"]")
for i in range(32):
  print(i//10,end="")
print()
for i in range(32):
  print(i%10,end="")  
for i in range(256):
  if i%32==0:
    print()
  if i in n:
    print(end="n")
  else:
    print(end=chr(i))
