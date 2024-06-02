# Multiplication table
u=10
print(' * ', end='')
for j in range(1, 9):
  print(end='%2d '%j)
for j in range(9, u):
  print(end='%3d '%j)
print()
for i in range(1, u):
  print(end='%2d:'%i)
  for j in range(1, 9):
    print(end='%2d ' % (i*j))
  for j in range(9, u):
    print(end='%3d ' % (i*j))
  print()
