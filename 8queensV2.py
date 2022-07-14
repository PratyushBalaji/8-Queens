# Success rate (8 coordinates) = 38/51 ≈ 74.5%

import random

# Declaring every variable for x an y position of corresponding queens. 
# Given them a value that isn't on the board : (0,0) [Board starts at (1,1) for (a1)]
x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

# declaring queen 1s position
x1 = random.randint(1,8)
y1 = random.randint(1,8)
print(f'1st coordinate : ({x1},{y1})')

# comparing 2nd set of random values (x,y) with 1st
while x2 == x1 or y2 == y1 or (y2 - y1)**2 == (x2 - x1)**2 or x2 == 0 or y2 == 0:
    x2 = random.randint(1,8)
    y2 = random.randint(1,8)
print(f'2nd coordinate : ({x2},{y2})')

# comparing 3rd set of random values (x,y) with 1st and 2nd
while x3 == x1 or y3 == y1 or (y3 - y1)**2 == (x3 - x1)**2 or x3 == 0 or y3 == 0 or x3 == x2 or y3 == y2 or (y3 - y2)**2 == (x3 - x2)**2 or x3 == 0 or y3 == 0:
    x3 = random.randint(1,8)
    y3 = random.randint(1,8)
print(f'3rd coordinate : ({x3},{y3})')

# comparing 4th set of random values (x,y) with 1st, 2nd and 3rd
while x4 == x1 or y4 == y1 or (y4 - y1)**2 == (x4 - x1)**2 or x4 == 0 or y4 == 0 or x4 == x2 or y4 == y2 or (y4 - y2)**2 == (x4 - x2)**2 or x4 == 0 or y4 == 0 or x4 == x3 or y4 == y3 or (y4 - y3)**2 == (x4 - x3)**2 or x4 == 0 or y4 == 0:
    x4 = random.randint(1,8)
    y4 = random.randint(1,8)
print(f'4th coordinate : ({x4},{y4})')

while x5 == x1 or y5 == y1 or (y5 - y1)**2 == (x5 - x1)**2 or x5 == 0 or y5 == 0 or x5 == x2 or y5 == y2 or (y5 - y2)**2 == (x5 - x2)**2 or x5 == 0 or y5 == 0 or x5 == x3 or y5 == y3 or (y5 - y3)**2 == (x5 - x3)**2 or x5 == 0 or y5 == 0 or x5 == x4 or y5 == y4 or (y5 - y4)**2 == (x5 - x4)**2 or x5 == 0 or y5 == 0:
    x5 = random.randint(1,8)
    y5 = random.randint(1,8)
print(f'5th coordinate : ({x5},{y5})')

while x6 == x1 or y6 == y1 or (y6 - y1)**2 == (x6 - x1)**2 or x6 == 0 or y6 == 0 or x6 == x2 or y6 == y2 or (y6 - y2)**2 == (x6 - x2)**2 or x6 == 0 or y6 == 0 or x6 == x3 or y6 == y3 or (y6 - y3)**2 == (x6 - x3)**2 or x6 == 0 or y6 == 0 or x6 == x4 or y6 == y4 or (y6 - y4)**2 == (x6 - x4)**2 or x6 == 0 or y6 == 0 or x6 == x5 or y6 == y5 or (y6 - y5)**2 == (x6 - x5)**2 or x6 == 0 or y6 == 0:
    x6 = random.randint(1,8)
    y6 = random.randint(1,8)

# comparing 8th set of random values (x,y) with 1st, 2nd, 3rd, 4th, 5th, 6th and 7th
while x8 == x1 or y8 == y1 or (y8 - y1)**2 == (x8 - x1)**2 or x8 == 0 or y8 == 0 or x8 == x2 or y8 == y2 or (y8 - y2)**2 == (x8 - x2)**2 or x8 == 0 or y8 == 0 or x8 == x3 or y8 == y3 or (y8 - y3)**2 == (x8 - x3)**2 or x8 == 0 or y8 == 0 or x8 == x4 or y8 == y4 or (y8 - y4)**2 == (x8 - x4)**2 or x8 == 0 or y8 == 0 or x8 == x5 or y8 == y5 or (y8 - y5)**2 == (x8 - x5)**2 or x8 == 0 or y8 == 0 or x8 == x6 or y8 == y6 or (y8 - y6)**2 == (x8 - x6)**2 or x8 == 0 or y8 == 0 or x8 == x7 or y8 == y7 or (y8 - y7)**2 == (x8 - x7)**2 or x8 == 0 or y8 == 0 or 7 == x1 or y7 == y1 or (y7 - y1)**2 == (x7 - x1)**2 or x7 == 0 or y7 == 0 or x7 == x2 or y7 == y2 or (y7 - y2)**2 == (x7 - x2)**2 or x7 == 0 or y7 == 0 or x7 == x3 or y7 == y3 or (y7 - y3)**2 == (x7 - x3)**2 or x7 == 0 or y7 == 0 or x7 == x4 or y7 == y4 or (y7 - y4)**2 == (x7 - x4)**2 or x7 == 0 or y7 == 0 or x7 == x5 or y7 == y5 or (y7 - y5)**2 == (x7 - x5)**2 or x7 == 0 or y7 == 0 or x7 == x6 or y7 == y6 or (y7 - y6)**2 == (x7 - x6)**2 or x7 == 0 or y7 == 0:
    x6 = random.randint(1,8)
    y6 = random.randint(1,8)
    x7 = random.randint(1,8)
    y7 = random.randint(1,8)
    x8 = random.randint(1,8)
    y8 = random.randint(1,8)
print(f'6th coordinate : ({x6},{y6})')
print(f'7th coordinate : ({x7},{y7})')
print(f'8th coordinate : ({x8},{y8})')