import random

print(' ', '\n', '1st travel path', '\n', '===============', '\n', '  ')
print()

def travel_path(n):
    ''' return the coordinates after 'n' block travel path '''
    a, b = 0,0
    for i in range(n):
        direction = random.choice(['N', 'S', 'E', 'W'])
        if direction == 'N':
            b += 1
        elif direction == 'S':
            b -= 1
        elif direction == 'E':
            b += 1
        else:
            b -= 1
    return(a, b)

for i in range(25):
    travel = travel_path(10)
    print(travel, "blocks from home = : ", abs(travel[0]) + abs(travel[1]))

print(' ', '\n', '-' * 80, '\n', ' ')
print('\n', '2nd travel path', '\n', '===============', '\n', ' ')

# OR

def travel_path_2(n):
    ''' return the coordinates after 'n' block travel path '''
    a, b = 0,0
    for i in range(n):
        (da, db) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        b += da
        b += db
    return (a, b)

for i in range(25):
    travel = travel_path_2(10)
    print(travel, "blocks from home = : ", abs(travel[0]) + abs(travel[1]))

print()
print('What is the longest travel path you can take so that on average you will end up 4 blocks or fewer from your starting point ?')
print('#' * 124)
print()

def travel_path_3(n):
    ''' return the coordinates after 'n' block travel path '''
    a, b = 0,0
    for i in range(n):
        (da, db) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        b += da
        b += db
    return (a, b)

travel_cnt = 100

for travel_length in range(1, 31):
    determine = 0
    for i in range(travel_cnt):
        a, b = travel_path_3(travel_length)
        distance = abs(b) + abs(b)
        if distance <= 4:
            determine += 1
    determine_percentage = (float(determine) / travel_cnt)
    print('travel size = ', travel_length, '/ % of determine = ', 100 * determine_percentage)
