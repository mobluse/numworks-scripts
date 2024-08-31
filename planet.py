# Planetbana
from math import *
from turtle import *

# Konstanter
G=1.0
M=1.0
m=1.0
dt=0.01

def omvandla(x,y):
  xpl=101*x
  ypl=101*y-7
  goto(xpl,ypl)

def koordaxlar():
  penup()
  omvandla(-1.0,0.0)
  pendown()
  omvandla(1.0,0.0)
  penup()
  omvandla(0.0,1.0)
  pendown()
  omvandla(0.0,-1.0)

def planet(vx=1.0):
  # Initialtillstand
  t=0.0
  vy=0.0
  x=0.0;y=1.0
  r=sqrt(x*x+y*y)
  # Grafinit
  hideturtle()
  speed(0)
  pensize(1)
  color("green")
  koordaxlar()
  penup()
  setheading(0)
  goto(-162,91)
  color("blue")
  write("Planetbana v0=%.3f"%vx)
  omvandla(x,y)
  color("black")
  showturtle()
  speed(1)
  pendown()
  try:
   # Stegning
    while True:
      omvandla(x,y)
      Fx=-G*M*m*x/(r**3)
      Fy=-G*M*m*y/(r**3)
      ax=Fx/m
      ay=Fy/m
      vx=vx+ax*dt
      vy=vy+ay*dt
      x=x+vx*dt
      y=y+vy*dt
      r=sqrt(x*x+y*y)
      t=t+dt
      # Ta bort raden under om den ger undantag.
      setheading(degrees(atan2(vy,vx)))
  except:
    print("r=%.3f, t=%.3f."%(r,t))
    vx=float(input("v0? "))
    planet(vx)

vx=float(input("v0? "))
planet(vx)
