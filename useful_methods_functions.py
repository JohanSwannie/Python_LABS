# FILTERING    

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
f = filter(is_even, [1, 3, 10, 45, 6, 50, 99])
for i in f:
     print(i, end = '    ')
print()

# ZIPPING

zippy = zip({1, 2, 3, 4, 5, 3, 9, 1}, "powerful")
print(list(zippy))

# ORD  - Ordinal Numbers

ascii = []
for i in ['a', 'b', 'c', 'd']:
    ascii.append(ord(i))
print(ascii)

# Mapping   

print("Mapping")
def twice(x):
    return x*2
print(list(map(twice, [11,22,33,44,55])), end = '   ')

def calc_sum(x1, x2):
    return x1+x2
result = list(map(calc_sum, [1, 2, 3, 4, 5], [10, 20, 30]))
print(result)
b = []
for a in range(10):
    x = int(input("Please enter an integer"))
    b.append(x)
print(b)

import math
def area(r):
    return math.pi * (r**2)
radii = [2, 7.4, 2+1j]
areas = []
for r in radii:
    areas.append(area(r))
print(areas)

#  OR

print(list(map(area, radii)))

temps = [('Johannesburg', 31), ('Cairo', 22), ('Auckland', 19), ('Sydney', 29)]
c_to_f = lambda data: (data[0], (9/5) * data[1] + 32)
print(list(map(c_to_f, temps)))

# LAMBDA Expressions 

a = lambda x: (3*x + (7 ** 3))
print(type(a))
print(a(15), a(19), a(21))

dict1 = dict({})
list1 = []

with open("C:\\Users\\Johan Swan\\Downloads\\lambda-names.txt") as f:
    for line in f:
        list1.append(line.strip().split())
    f.close()

print(list1)

for x, y, z in sorted(list1):
    dict1[x] = y + ' ' + z

print(dict1)

full_name = lambda fn, ln_age: fn.strip().title() + '  ' + ln_age.strip().title()

for fn, ln in dict1.items():
    print(full_name(fn, ln))

list2 = ['Banie Boek poep', 'Kosie Top stop', 'Tinus Dop sop', 'Tanya Otter scooter', 'Blikkies Grasman wasman']
try:
    list2.sort(key = lambda name: name.split(" ")[1].lower())
    for x in list2:
        print(x)
except IndexError as e:
    print(e)
else:
    print("Stellie very happy")
finally:
    print("Swannie also very happy")

def qfunc(a, b, c):
    return lambda x: a*x**2 + b*x + c

f = qfunc(2, 3, -5)
print(f(2), ' -> ', f(1), ' -> ', f(0), ' -> ')

# OR

for int1 in range(2, -1, -1):
    print(qfunc(2, 3, -5)(int1), ' -> ', end = ' ')

import statistics
data = [1.91, 4.45, 18.3, 16.93, 14.37]
avg = (statistics.mean(data))
print(avg)
print(list(filter(lambda x: x < avg, data)))

# REDUCE FUNCTION    

from functools import reduce
numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
multiplier = lambda x, y: x*y
print(reduce(multiplier, numbers))

#  OR

product = 1
for x in numbers:
    product = product * x
print(product)


from functools import reduce
def do_sum(x1, x2):
    return x1 + x2
print(reduce(do_sum, [1, 2, 3, 4, 8]))
