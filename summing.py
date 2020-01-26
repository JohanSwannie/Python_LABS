#  Summing the Digits of a long number 

print('Summing digits in a long number')
num = 123456789
sum1 = 0
for digit in str(num):
    sum1 += int(digit)
print(sum1,end = '   ')

# OR

num = 123456789
print(sum(int(digit) for digit in str(num)), end = '   ')

s1 = 123510981219981251432
print(sum(int(s2) for s2 in str(s1)))

# Summing the values in Lists, Tuples, Sets and Dictionaries     

print('Summing the values in Lists, Tuples, Sets & Dictionaries')
print('List', sum([1, 2, 3, 4, 5]), end = '   ') 
print('Tuple', sum((1, 2, 3, 4, 5)), end = '   ')
print('Set', sum({1, 2, 3, 4, 5}), end = '   ') 
print('Dictionary', sum({1: "one", 2: "two", 3: "three"}))
