import random

def shuffle(array):
  randrange=random.randrange
  for i in range(len(array)-1,0,-1):
    j=random.randrange(i+1)
    array[i],array[j]=array[j],array[i]

#arr=[2,11,37,42]
#shuffle(arr)
#print(arr)
