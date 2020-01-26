#  Staircase - Running from left to upwards right    

def staircase(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '#' * i)

n = int(input())
staircase(n)

#  Staircase - Running from right to upwards left   

def staircase(n):
    for i in range(1, n + 1):
        print( '#' * i + ' ' * (n - 1))

n = int(input())
staircase(n)

# Christmas Tree 

def ChristmasTree(n):
    a = n - 1
    b = 1
    for i in range(1, n + 1):
        print(' ' * a + '#' * b)
        a -= 1
        b += 2

n = int(input())
ChristmasTree(n)



