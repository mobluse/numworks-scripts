# Multiplication Quiz
from random import *
mt=6
noe=10
r=0
for n in range(1,noe+1):
  f1=randint(2,mt)
  f2=randint(2,mt)
  error=1
  while error==1:
    try:
      ans=int(input('%2d. %d*%d='%(n,f1,f2)))
      error=0
    except:
      print('Input a number.')
  print(end=' '*12)
  if f1*f2==ans:
    print('Correct!')
    r+=1
  else:
    print('Wrong.')
print('%d correct of %d.'%(r,noe))
