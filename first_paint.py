# First Paint
from ion import *
from kandinsky import *
import time
def first_paint():
  x=160
  y=100
  while 1:
    if keydown(KEY_LEFT):
      x=x-1
    if keydown(KEY_UP):
      y=y-1
    if keydown(KEY_RIGHT):
      x=x+1
    if keydown(KEY_DOWN):
      y=y+1
    set_pixel(x,y,color(0,255,0))
    time.sleep(0.1)
first_paint()
