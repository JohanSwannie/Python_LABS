# TUPLES
# A tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Tuple Methods

tuple1 = ('tuple', True, 'yes', 13.45, 88, 3 + 1j, 55)

for x in tuple1:
    print(x)

print('print value of tuple1 from index 1 to index 3', tuple1[1:4])
print('print value of tuple1 in reverse order', tuple1[::-1])
print('print value of tuple1 from index -4 to index -2', tuple1[-4:-1])
print('tuple1 is:', tuple1, 'with length of :', len(tuple1))

a = ("Johan Swan", "Peter Murray", "Dan Pavihi")
b = list(a)
b[1] = "Gerald Hopkins"
a = tuple(b)
print('Tuple changed by means of list usage is now:', a)

print('Dan Pumpkin' in a)
if 'Gerald Hopkins' in a:
    print('TRUE')

tuple2 = ('football match',)
print('a tuple with 1 item followed by a comma is a:', type(tuple2))
tuple3 = ('soccer match')
print('a tuple with 1 item followed by no comma is a:', type(tuple3))
tuple4 = (True, 'Hello', 77.45)
tuple2 = tuple2 + tuple4
print(tuple2)

tuple5 = tuple((1, 18.55, 19, 36, 109, 19, 107, 1.33, 55, 19))
print('The values in tuple 5 is:', tuple5)
print('The value 19 occurs:', tuple5.count(19), 'times in tuple5')
print('The value 109 appears in index:', tuple5.index(109), 'in tuple5')

# SETS
# A set is a collection which is unordered and unindexed. No duplicate members.
# Set Methods

set1 = {15, 3, 19, True, "happy"}
for x in set1:
    print(x)

print(5 in set1)
if True in set1:
    print('True')
else:
    print('False')

set1.add('Tuesday')
print('The new values in set1 is now:', set1)
set1.update([1, 86, 'Auckland'])
print('The new values in set1 is now:', set1, 'with length of:', len(set1))
set1.remove(1)
print('The new values in set1 is now:', set1, 'with length of:', len(set1))
set1.discard('Tuesday')
print('The new values in set1 is now:', set1, 'with length of:', len(set1))
set1.pop()
print('The new values in set1 is now:', set1, 'with length of:', len(set1))

set2 = {14, 99.35, False, 'Fantastic'}
set3 = set1.union(set2)
print('The values in set3 is now:', set3, 'with a length of:', len(set3))
set1.update(set3)
print('The values in set1 is now:', set1, 'with a length of:', len(set1))

set4 = set((9, 119, 3,44, False))
print('set4 is now:', set4)

set5 = set1.copy()
print('set5 is now:', set5)

set6 = set1.difference(set2)
print('set1 values are:', set1, 'set2 values are:', set2)
print('Set6 shows what values in set1 differs from the values in set2 and are:', set6)

set7 = {1, 4, 10, 19, 33}
set8 = {18, 25, 10, 19, 34, 1, 12}
set9 = set7.intersection(set8)

set10 = {1, 8, 33, 40, 91, 12, 10}
set11 = {9, 13, 20, 12, 29, 44, 8, 1, 33, 10, 40, 91}


x = set10.isdisjoint(set11)
print('is there an intersection between set10 & set11:', x)
y = set10.issubset(set11)
print('is set10 a subset of set11:', y)
z = set10.issuperset(set11)
print('is set10 a superset of set11:', z)
w = set10.symmetric_difference(set11)
print('what is the symmetric difference between set10 & set11:', w)

print('set10 values are now:', set10)
print('set9 values are now:', set9)
(set7.difference_update(set8))
print('set7 values are now:', set7)

set1.clear()
print('set1 is now an empty set:', set1)

del set1

try:
    print(set1)
except Exception as d:
    print('The error with set1 is : ', d)
