import random

names = ['Stellie', 'Andries', 'Petra', 'Righard', 'Johan', 'Ida', 'Julie', 'Tasha', 'Roxanne']
sports = ['Tennis', 'Rugby', 'Cricket', 'Bowls', 'Golf', 'Athletics', 'Boxing', 'Wrestling']

def list_Gen(people):
    for x in range(people):
        person = {
                    'id': x,
                    'name': random.choice(names),
                    'sport': random.choice(sports)
                }
        yield person

list1 = list_Gen(3)
for z in list1:
    print(z)
print()

# Itertools

import itertools
import operator

# Count

cnt1 = itertools.count()
c = 0
for x in cnt1:
    if x < 100:
        c += x
    else:
        break
print(c)

data1 = [23, 45, 17, 93, 7, 28, 33, 12]
data2 = ['yes', 'no', 'yes', 'maybe', 'perhaps', 'yes', 'forsure', 'Oh yes']
data3 = list(zip(itertools.count(start=10, step=-1.5), data1, data2))
print(data3)

# Zip with range

data4 = list(zip(range(10), data1))
print(data4)

# Zip with longest(range)

data5 = list(itertools.zip_longest(range(13), data1 ))
print(data5)

# Next

cntr2 = itertools.cycle([3, 9, 11, 5])
print(((next(cntr2) * 2)) ** 8)

# Map

squares = map(pow, range(8), itertools.repeat(2))
print(list(squares))

# starmap

sq2 = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2)])
print(list(sq2))

letters = ['a', 'b', 'c', 'd']
numbers = [14, 22, 3, 18]
names = ['Chris', 'Johan', 'Gert', 'Piet']
booleans = [True, False, True, True]

# Combinations

result1 = itertools.combinations(letters, 2)
print(list(result1))

# Permutations

result2 = itertools.permutations(letters, 2)
print(list(result2))

# Product

result3 = itertools.product(numbers, repeat=4)
print(list(result3))

# Combinations with replacement

result4 = itertools.combinations_with_replacement(numbers, 4)
print(list(result4))

# Chain

combined = itertools.chain(letters, numbers, names)
for i in combined:
    print(i, '   ', end='')

# islice - range - stop

result5 = itertools.islice(range(15), 9)
print(list(result5))

# islice - range -start + stop

result6 = itertools.islice(range(15), 2, 11)
print(list(result6))

# islice - range -start + stop + step

result7 = itertools.islice(range(15), 2, 18, 3)
print(list(result7))

# islice with files

with open('test-itertools.txt', 'r') as f:
    reader = itertools.islice(f, 5)
    for x in reader:
        print(x)

# compress

result8 = itertools.compress(letters, booleans)
print(list(result8))

# Filter without itertools

def gt_15(n):
    if n > 15:
        return True
    else:
        return False

numbers2 = [2, 9, 19, 7, 15, 22, 11, 17, 6, 33, 20]

result9 = filter(gt_15, numbers2)
print(list(result9))

# Filterfalse with itertools

def gt_15(n):
    if n > 15:
        return True
    else:
        return False

numbers3 = [2, 9, 19, 7, 15, 22, 11, 17, 6, 33, 20]

result10 = itertools.filterfalse(gt_15, numbers3)
print(list(result10))

# Dropwhile with itertools

def gt_15(n):
    if n > 15:
        return True
    else:
        return False

numbers4 = [2, 9, 19, 7, 15, 22, 11, 17, 6, 33, 20]

result11 = itertools.dropwhile(gt_15, numbers4)
print(list(result11))

# Takewhile with itertools

def gt_15(n):
    if n > 15:
        return True
    else:
        return False

numbers5 = [2, 9, 19, 7, 15, 22, 11, 17, 6, 33, 20]

result12 = itertools.takewhile(gt_15, numbers5)
print(list(result12))

# Accumulate

result13 = itertools.accumulate(numbers)
print(list(result13))

# Accumulate with operator

result14 = itertools.accumulate(numbers, operator.mul)
print(list(result14))

# Groupby

def determine_Region(p):
    return p['region']

persons = [
    {
       'name': 'Estella Bella',
        'place': 'Tauranga',
        'region': 'Bay of Plenty'
    },
    {
        'name': 'Gunter Gatsby',
        'place': 'Tauranga',
        'region': 'Bay of Plenty'
    },
    {
        'name': 'Johny Jackson',
        'place': 'Tauranga',
        'region': 'Bay of Plenty'
    },
    {
        'name': 'Barnie Bester',
        'place': 'Tauranga',
        'region': 'Bay of Plenty'
    },
    {
        'name': 'Mary Poppins',
        'place': 'Targaville',
        'region': 'New York'
    },
    {
        'name': 'Neil Forrester',
        'place': 'Maryville',
        'region': 'Washington'
    },
    {
        'name': 'Trudi Ashton',
        'place': 'Kentsville',
        'region': 'Auckland'
    }
]

groups = itertools.groupby(persons, determine_Region)

for key, value in groups:
    print(key)
    for val in value:
        print(val)
    print()

# RANDOM

import random

names = ['Gert', 'Koos', 'Piet', 'Sarie', 'Stellie', 'Roxy', 'Sarel']

cnt1 = 0
for i in range(44):
    if random.choice(names) == 'Stellie':
        cnt1 += 1
print('Stellie has been chosen :', cnt1, 'Times')


# Iterables + Iterators

list1 = [12, 9, 'Yes', 3.33, False, 14]
list2 = iter(list1)
for i in range(len(list1)):
    print(next(list2), '   ', end='')
print()

list3 = [73, 29, 'No', 13.54, True, 18]
list4 = iter(list3)

while True:
    try:
        item = next(list4)
        print(item, '   ', end='')
    except StopIteration:
        break
print()

class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= (self.end + 1):
            raise StopIteration
        current = self.value
        self.value += 1
        return current

nums = MyRange(1, 10)
while True:
    try:
        print(next(nums), '   ', end='')
    except StopIteration:
        break
print()

# Generators in general

def newRange(startpoint, endpoint):
    current_point = startpoint
    while current_point <= (endpoint):
        yield current_point
        current_point += 1

nbrs1 = newRange(1, 20)

for x in nbrs1:
    print(x, '   ', end='')
print()

def toPowerCalc(x):
    for n in x:
        yield n**n

numbers1 = toPowerCalc([1, 2, 3, 4, 5, 6])
for y in numbers1:
    print(y, '   ', end='')
print()

# List Comprehension generator

i = [x * x for x in [1, 3, 5, 7, 9, 11]]

for j in i:
    print(j, '   ', end='')

