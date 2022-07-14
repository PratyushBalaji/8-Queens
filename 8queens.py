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

# comparing 5th set of random values (x,y) with 1st, 2nd, 3rd and 4th
while x5 == x1 or y5 == y1 or (y5 - y1)**2 == (x5 - x1)**2 or x5 == 0 or y5 == 0 or x5 == x2 or y5 == y2 or (y5 - y2)**2 == (x5 - x2)**2 or x5 == 0 or y5 == 0 or x5 == x3 or y5 == y3 or (y5 - y3)**2 == (x5 - x3)**2 or x5 == 0 or y5 == 0 or x5 == x4 or y5 == y4 or (y5 - y4)**2 == (x5 - x4)**2 or x5 == 0 or y5 == 0:
    x5 = random.randint(1,8)
    y5 = random.randint(1,8)
print(f'5th coordinate : ({x5},{y5})')

# comparing 6th set of random values (x,y) with 1st, 2nd, 3rd, 4th and 5th
while x6 == x1 or y6 == y1 or (y6 - y1)**2 == (x6 - x1)**2 or x6 == 0 or y6 == 0 or x6 == x2 or y6 == y2 or (y6 - y2)**2 == (x6 - x2)**2 or x6 == 0 or y6 == 0 or x6 == x3 or y6 == y3 or (y6 - y3)**2 == (x6 - x3)**2 or x6 == 0 or y6 == 0 or x6 == x4 or y6 == y4 or (y6 - y4)**2 == (x6 - x4)**2 or x6 == 0 or y6 == 0 or x6 == x5 or y6 == y5 or (y6 - y5)**2 == (x6 - x5)**2 or x6 == 0 or y6 == 0:
    x6 = random.randint(1,8)
    y6 = random.randint(1,8)
print(f'6th coordinate : ({x6},{y6})')

# comparing 7th set of random values (x,y) with 1st, 2nd, 3rd, 4th, 5th and 6th
while x7 == x1 or y7 == y1 or (y7 - y1)**2 == (x7 - x1)**2 or x7 == 0 or y7 == 0 or x7 == x2 or y7 == y2 or (y7 - y2)**2 == (x7 - x2)**2 or x7 == 0 or y7 == 0 or x7 == x3 or y7 == y3 or (y7 - y3)**2 == (x7 - x3)**2 or x7 == 0 or y7 == 0 or x7 == x4 or y7 == y4 or (y7 - y4)**2 == (x7 - x4)**2 or x7 == 0 or y7 == 0 or x7 == x5 or y7 == y5 or (y7 - y5)**2 == (x7 - x5)**2 or x7 == 0 or y7 == 0 or x7 == x6 or y7 == y6 or (y7 - y6)**2 == (x7 - x6)**2 or x7 == 0 or y7 == 0:
    x7 = random.randint(1,8)
    y7 = random.randint(1,8)
print(f'7th coordinate : ({x7},{y7})')

# comparing 8th set of random values (x,y) with 1st, 2nd, 3rd, 4th, 5th, 6th and 7th
while x8 == x1 or y8 == y1 or (y8 - y1)**2 == (x8 - x1)**2 or x8 == 0 or y8 == 0 or x8 == x2 or y8 == y2 or (y8 - y2)**2 == (x8 - x2)**2 or x8 == 0 or y8 == 0 or x8 == x3 or y8 == y3 or (y8 - y3)**2 == (x8 - x3)**2 or x8 == 0 or y8 == 0 or x8 == x4 or y8 == y4 or (y8 - y4)**2 == (x8 - x4)**2 or x8 == 0 or y8 == 0 or x8 == x5 or y8 == y5 or (y8 - y5)**2 == (x8 - x5)**2 or x8 == 0 or y8 == 0 or x8 == x6 or y8 == y6 or (y8 - y6)**2 == (x8 - x6)**2 or x8 == 0 or y8 == 0 or x8 == x7 or y8 == y7 or (y8 - y7)**2 == (x8 - x7)**2 or x8 == 0 or y8 == 0:
    x8 = random.randint(1,8)
    y8 = random.randint(1,8)
print(f'8th coordinate : ({x8},{y8})')


# Notes : 
# 1. In the distance comparison for diagonals, I initially encountered some false positives as 
#    I was only checking if the distance between 2 points was the same, not the sqaure of the distance. 
#    So diagonals in the line : y = -x were not considered as hits, but diagonals in y = x were.
# 2. The program softlocks itself frequently as the random numbers are generated in order from 1 to 8,
#    meaning that if the first 5-6 generate with no problem, it doesn't guarantee that the 7th and 8th 
#    do so as well. This is because there can be certain 'impossible' combinations that the code can't
#    detect ahead of time. As of right now, I have no way of figuring out if a combination is possible
#    or not. I simply have to manually see if the 8th coordinate is outputted. If not, I know the code 
#    is looping.


# Explanation of the logic : 

# - The chess queen can attack anything it sees vertically, horizontally and diagonally.

# With this we know that
# - Vertical means that if the y coordinate is the same as any queen, a queen sees the other
# - Horizontal is the same as vertical but for the x axis
# A simple comparison checking whether xn and yn is the same as any other value of n returns true or false.
# If true, the x or y value generated is already taken by another queen and needs to be regenerated.
# If false, the x or y value is unique and can remain with the queen. The while loop breaks and the 
#   value is permanently attributed to said queen 

# Diagonals are a bit more complex. The logic for diagonals is derived from the Pythagorean Theorem
# Initially, I defined diagonal points as "Any 2 points, such that the x difference equals the y difference."
# Although I am not wrong, my code said otherwise. "if ya - yb == xa - xb:"
# This works in 2/4 cases. The other 2 cases are where; ya > yb but xa < xb, and ya < yb but xa > xb
# The Pythagorean theorem solves this issue by squaring and then taking the square root of these numbers.
# In mathematics, we know that all real numbers are positive when squared. As the integer itself in these
#   cases is the same number but negative (For example -2 and +2), we can square the numbers to get the 
#   same answer (+4 and +4). Now we can check if (ya - yb)^2 == (xa - xb)^2.
# I could've taken the absolute value of the equation to get the same results, but the standard abs() 
#   function had some issues running on one of my computers but not the other. I decided to go with the 
#   solution that worked across devices.

# With the absolute value of the distances now calculated, my original definition has been successfully 
#   translated into code and the program can now check for diagonals.


# Improvements : 
# 1. Remove softlock + increase success rate by generating all at once or stepping back to change one if 
#    softlock is detected
# 2. Remove unnecessary extra copy-pasted code by creating booleans that check whether certain 
#    conditions are true or not. Loop through these conditions every cycle and regenerate if necessary.
#    Some "while" parameters go one for 500+ columns and can be cut down.