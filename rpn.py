# Simple RPN calculator
# Based on https://my.numworks.com/python/garycmartin/rpn
from math import *
from random import random

ops = {'+': [2, lambda x, y : x + y],
  '-': [2, lambda x, y : x - y],
  '*': [2, lambda x, y : x*y],
  '/': [2, lambda x, y : x/y],
  'sqr': [1, lambda x : x*x],
  '1/x': [1, lambda x : 1/x],
  '**': [2, lambda x, y : x**y],
  '**2': [1, lambda x : x**2],
  '!': [1, lambda x : fact(int(round(x)))],
  'deg': [1, lambda x : degrees(x)],
  'rad': [1, lambda x : radians(x)],
  'log': [1, lambda x : log(x)],
  'exp': [1, lambda x : exp(x)],
  'log10': [1, lambda x : log10(x)],
  'sqrt': [1, lambda x : sqrt(x)],
  'sin': [1, lambda x : sin(x)],
  'cos': [1, lambda x : cos(x)],
  'tan': [1, lambda x : tan(x)],
  'asin': [1, lambda x : asin(x)],
  'acos': [1, lambda x : acos(x)],
  'atan': [1, lambda x : atan(x)]}

def evaluate(tokens, stack):
  for t in tokens:
    if t[-2:]=="()":
      t=t[:-2]
    if t == 'pi':
      stack.append(pi)
    elif t == 'e':
      stack.append(e)
    elif t == 'rnd':
      stack.append(random())
    elif t == 'swap':
      try: a = stack.pop()
      except: return []
      try: b = stack.pop()
      except: return [a]
      stack.append(a)
      stack.append(b)
    elif t == 'roll':
      try: stack.insert(0, stack.pop())
      except: return []
    elif t == 'drop':
      try: stack.pop()
      except: return []
    elif t in ops:
      op = ops[t][1]
      if ops[t][0] == 1 and len(stack) >= 1:
        a = stack.pop()
        try: stack.append(op(a))
        except: print("Error"); stack.append(a)
      elif ops[t][0] == 2 and len(stack) >= 2:
        a = stack.pop()
        b = stack.pop()
        try: stack.append(op(b,a))
        except: print("Error"); stack.append(b); stack.append(a)
    elif set(t).issubset(set("0123456789.-e")):
      stack.append(float(t))
    else:
      print("Unknown token %s" % t)
  return stack

def fact(n):
  f = 1
  while n > 0:
    f *= n; n -= 1
  return f

stack = []
while True:
  expression = input('> ')
  expr = ''
  for ch in expression:
    if ch == ',':
      ch = ' '
    expr += ch
  expression = expr
  if expression is 'q':
    break
  elif expression is 'clr':
    stack = []
  elif expression is '?':
    print('Help:', end=' ')
    w = 0
    for o in sorted(list(ops.keys()) + ['rnd', '?', 'q', 'clr', 'pi', 'e', 'swap', 'roll', 'drop']):
      print(o, end=' ')
      w += 1
      if w > 5: print(); w = 0
    if w != 0: print()
    continue
  elif len(expression) == 0:
    continue
  else:
    stack = evaluate(expression.split(), stack)
  print(stack)
