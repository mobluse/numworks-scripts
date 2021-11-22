# Multiplication table
print('* ', end='')
for j in range(1, 10):
  print(end='%2d '%j)
print()
for i in range(1, 10):
  print(end='%1d:'%i)
  for j in range(1, 10):
    print(end='%2d ' % (i*j))
  print()
