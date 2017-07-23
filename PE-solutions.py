"""
PROJECT EULER SOLUTIONS TO PROBLEMS #1-10, 11, 13, 14, 16
by Jose Dario Sanchez
"""

#Problem 1:
total = 0
for x in range(1000):
  if (x % 3 == 0) or (x % 5 == 0):
    total += x
print(total)

#Problem #2
prv = 1
nxt = 1
total = 0
dummy = 0
while (nxt <= 4000000):
  dummy = nxt
  nxt += prv
  prv = dummy
  if (nxt % 2 == 0 and nxt <= 4000000):
    total += nxt
print(total)

#Problem #3
factors = []
prime = False
number = 600851475143
root = int(number ** 0.5)
for x in range(2, root + 1):
  if (number % x == 0):
    factors = factors + [x]
for y in range(0, len(factors)):
  root = int(factors[y] ** 0.5)
  if (root > 2):
    for z in range(2, root + 1):
      if (factors[y] % z == 0):
        factors[y] = 0
factors = sorted(factors)
print(factors[len(factors)-1])

#Problem #4
a = 999
b = 999
palindromes = []
for x in range(a, 100, -1):
  for y in range(b, 100, -1):
    if (str(x*y) == str(x*y)[::-1]):
      palindromes += [x*y]
palindromes = sorted(palindromes)[::-1]
print(palindromes[0])

#Problem #5
number = 20
dummy = number
found = False
while (found == False):
  dummy = number
  for x in range(1, 21):
    if (number % x != 0):
      number += 20
  if (dummy == number):
    print(number)
    break

#Problem #6
sumOfSquares = 0
squareOfSums = 0
for x in range(1, 101):
  sumOfSquares += x**2
  squareOfSums += x
squareOfSums = squareOfSums**2
difference = squareOfSums - sumOfSquares
print(difference)

#Problem #7
primes = [2, 3, 5, 7, 13]
prime = False
number = 15
while (len(primes) < 10001):
  for x in range(0, len(primes), 1):
    if (number % primes[x] == 0):
      prime = False
      break
    else:
      prime = True
  if (prime == True):
    primes += [number]
  number += 2
print(primes[len(primes)-1])

#Problem #8
#number = ...
chunks = [1] * (len(str(number))-12)
product = 1
for x in range(0, len(str(number))-12):
  for y in range(x, x+13):
    chunks[x] = chunks[x] * int(str(number)[y])
print(sorted(chunks)[len(chunks)-1])

#Problem #9
for a in range(1, 1000):
  for b in range(1, 1000):
    for c in range(1, 1000):
      if (a+b+c==1000 and \
      a**2 + b**2 == c**2):
        print(a*b*c)

#Problem #10
def sumOfPrimes(n):
  total = 0
  primes = [True] * (n+1)
  primes[0] = False
  primes[1] = False
  for x in range(2, int(n**(0.5)+1)):
    for y in range(2, n):
      if(x*y > n):
        break
      else:
        primes[x*y] = False
  for z in range(0, n):
    if (primes[z] == True):
      total += z
  print(total)
sumOfPrimes(2000000)

#Problem #11:
#grid = ...
products = []
for x in range(0, 20):
  for y in range(0, 20):
    if (x+3 < 20):
      products += [grid[x][y]*grid[x+1][y]*grid[x+2][y]*grid[x+3][y]]
    if (y+3 < 20):
      products += [grid[x][y]*grid[x][y+1]*grid[x][y+2]*grid[x][y+3]]
    if  (x+3 < 20 and y+3 < 20):
      products += [grid[x][y]*grid[x+1][y+1]*grid[x+2][y+2]*grid[x+3][y+3]]
    if  (x-3 > 0 and y+3 < 20):
      products += [grid[x][y]*grid[x-1][y+1]*grid[x-2][y+2]*grid[x-3][y+3]]
print(sorted(products)[::-1][0])

#Problem #13
#matrix = ...
total = 0
for x in range(0, len(matrix)):
  total += matrix[x]
print(str(total)[0:10])

#Problem #14
n = 1
saved = 1
current = 1
ceiling = 1000000
for x in range(1, ceiling):
  a = x
  current = 1
  while (a != 1):
    if (a % 2 == 0):
      a = a / 2
      current += 1
    else:
      a = 3*a + 1
      current += 1
  if (current > saved):
    n = x
    saved = current
print(n, saved)

#Problem #16
number = str(2**1000)
total = 0
for x in range(0, len(number)):
  total += int(number[x])
print(total)
