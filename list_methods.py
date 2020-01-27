# LISTS
# A list is a collection which is ordered and changeable. It allows duplicate members
#
# LIST METHODS
#
list1 = [12, True, "yellow", 31.342, False, 1 + 1j, 18]

for x in list1:
    print(x, end = '       ')

print()
print('element at index 3 in list1 is : ', list1[3])
print('elements in list1 from index 1 to index 4 are : ', list1[1:5])
print('elements in list1 from last 1 backward to index 4 are : ', list1[-1:3:-1])
print('elements in list1 from index 1 to index 4 are : ', list1[1:5])
print('elements in list1 from index 0 in steps of 5 are : ', list1[::5])
print('elements in list1 from index 4 to the end 4 are : ', list1[4:])
print('elements in list1 from index 0 to index 3 are : ', list1[:4])
print('elements in list1 from index -6 to index -3 are : ', list1[-6:-2])

list1[4] = True

print('False in list1 now changed to True : ', list1)
print(False in list1)

if "yellow" in list1:
    print("Yes 'yellow' is indeed in list1 and the length of list 1 is : ", len(list1))
else:
    print("No, 'yellow' is not in list1")

list11 = ['Johan Swan', 'Peter Hepburn', 'Mary Laidlaw', False, 323.55]

for x in list11:
    list1.append(x)
print(list1)

list7 = [14, 18, 3, 14, 9, 11, 18, 2, 21, 3, 37, 40, 18, 14]
list8 = []

for number in list7:
    if number not in list8:
        list8.append(number)

print(sorted(list8))

list12 = [2, 4, 6, 8, 10, 12, 14, 16]

for y in range(8):
    list1.insert(y, ((y + 2)*list12[y]))
print(list1, "list 1 is now a length of ", len(list1))

list9 = [15, 'lst10 details', 14.23, True, 'Hello', 18, None, 81.88, False]
print('User will be able to insert 10 chosen values and 10 chosen index locations to update the list')

cnt1 = 0

while True:
    val1 = int(input("Please enter the location in the list where value needs to be inserted : "))
    val2 = input("Please enter the value to be inserted into the list")
    list9.insert(val1, str(val2))
    cnt1 += 1
    if cnt1 == 10:
        break

print(list9)

list1.remove(list1[13])
list1.remove('Johan Swan')
list1.pop()
del list1[4]
print(list1)

list2 = list1.copy()
list3 = list(list1)
list4 = list2 + list3
list2.extend(list4)

if len(list1) == len(list3):
    print(len(list1) == len(list3), " - their length = ",  len(list1))
    print("list1 = : ", list1)
    print("list3 = : ", list3)
else:
    print(len(list1) == len(list3))
    print('The length of list 1 is :', len(list1), list1)
    print('The length of list 3 is :', len(list3), listt3)


if len(list2) == len(list4):
    print(len(list2) == len(list4), " - their length = ",  len(list2))
    print("list2 = : ", list2)
    print("list4 = : ", list4)
else:
    print(len(list2) == len(list4))
    print('The length of list 2 is :', len(list2), list2)
    print('The length of list 2 is :', len(list4), list4)

list2.sort(key=str)
print("list2 sorted in string sequence is now:", list2)

print("The number 12 occurs", list2.count(12), "times in list2")
print("The name 'Peter Hepburn' occurs in index no :", list2.index('Peter Hepburn'))

list5 = ['John', 'Thomas', 'Ben', 'Charles', 'Estelle', 'Dorothy', 'Dan']
list5.reverse()
print("list5 reversed is:", list5)
list6 = [11, 2, 13, 4, 5, 16, 27, 18, 9, 110, 11, 22, 30]
print('list6 sorted in numerical sequence is now:', sorted(list6))
print("list6 reversed is:", list6[::-1])

list1.clear()
print('list1 is now and empty list:', list1)

del list1

try:
    print(list1)
except Exception as e:
    print('Error for list1 is : ', e)

# LISTS WITH FUNCTIONS

txns = [1.09, 23.56, 57.84, 4.56, 6.78]
tax_rate = .08

def get_price_with_tax(txn):
    return txn * (1 + tax_rate)

final_prices = map(get_price_with_tax, txns)
print(list(final_prices))

# OR

txns2 = [1.09, 23.56, 57.84, 4.56, 6.78]
tax_rate2 = .08

def get_price_with_tax2(txn):
    return txn * (1 + tax_rate2)

final_prices2 = [get_price_with_tax2(i) for i in txns2]
print(final_prices2)

# # LIST COMPREHENSIONS

squares = [i * i for i in range(10)]
print(squares)

sentence = 'the pocket is full of peanuts'
letters = [i for i in sentence if i in 'pocket']
print(letters)

sentence2 = 'The pockets of 3 millionaires are stacked with dollars'

def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels

consonants = [i for i in sentence2 if is_consonant(i)]
print(consonants)

original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 1.25 else 'oh goodness' for i in original_prices]
print(prices)

# OR

original_prices2 = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
def get_price2(price):
    return price if price > 0 else 'Richie Rich Bankrupt Rich'
prices = [get_price2(i) for i in original_prices2]
print(prices)

temps = []
highest = -100
temps = [[0.0 for h in range(24)] for d in range(31)]

temps[0][4] = 71.4; temps[5][8] = 82.5; temps[16][19] = 45.3; temps[20][21] = 88.75

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("The highest temperature recorded was : ", highest)
