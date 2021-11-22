# Multiplikationsfrågesport
from random import *
r=0
for n in range(1,11):
  i=randrange(2,10)
  j=randrange(2,10)
  svar=int(input('%d. %d*%d='%(n,i,j)))
  print(end=' '*12)
  if i*j==svar:
    print('Rätt!')
    r+=1
  else:
    print('Fel.')
print('%d rätt av 10.'%r)
