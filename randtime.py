from time import *
t=monotonic()
print(t)
sleep(1)
print(monotonic()-t)
from random import *
#seed(1)
print(random())
print(uniform(1,6))
print(randint(1,6))
print(choice(range(1,7)))
print(randrange(1,7))
print(getrandbits(4))
