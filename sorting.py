# LISTS

l1 = [9, 12, 3, 16, 22, 1, 5, 30, 20, 8, 11]

l2 = sorted(l1)
print('List l2 is now\t', l2)

# reverse

l3 = sorted(l1, reverse=True)
print('List l3 is now\t', l3)

# sort

l1.sort()
print('List l1 is now\t', l1)

# sorted

l4 = [-7, -4, -5, 0, 3, 2, 1]
l5 = sorted(l4)
print('List l5 is now\t', l5)

# key

l6 = sorted(l4, key=abs)
print('List l6 is now\t', l6)

# sort with classes

class customer():
    def __init__(self, person, birthyear, salary, points):
        self.cust = person
        self.birthy = birthyear
        self.salary = salary
        self.marks = points

    def __repr__(self):
        return('{},{},{},{}'.format(self.cust, self.birthy, self.salary, self.marks))

l7 = customer('J Swan', 1963, 120000, 414)
l8 = customer('P Knobbles', 1971, 95000, 903)
l9 = customer('G Terry', 1968, 105000, 567)
l10 = [l7, l8, l9]

# Use function to customize sort

def cust_Sort(cust):
    return cust.salary

all_Customers = sorted(l10, key=cust_Sort, reverse=True)

print('List all_Customers is now\t', all_Customers)

# Use lambda expression to customize sort

all_C2 = sorted(l10, key=lambda e: e.marks, reverse=True)

print('List all_Customers is now\t', all_C2)

# use sub module attrgetter from operator module to customize sort

from operator import attrgetter

all_C3 = sorted(l10, key=attrgetter('cust'))

print('List all_Customers is now\t', all_C3)

# TUPLES

tup1 = (12, 18, 10, 7, 14, 20, 3, 11, 19, 4)
tup2 = sorted(tup1)
print('Tuple tup2 is now\t', tup2)

# DICTIONARIES - will only sort the keys

d1 = {'akey':3, 'bkey':6, 'dkey':8, 'zkey':9, 'ckey':4, 'mkey':11,'fkey':13}
d2 = sorted(d1, reverse=True)
print('Dictionary d2 is now\t', d2)
