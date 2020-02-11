
age=25
print("Roxanne is  now %d years old" %(age))
print("Tasha is now %d years old" %(age + 4))
print("Stellie is %d, %s, %d, %s" %((age * 2 + 10), "years and ", 4, "months old"))

cal = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
c1 = "jfmaynlgsovd"

for c2 in range(0, len(c1)):
    if c1[c2] in "jmylgod":
        print("In month {0} which is {1} there are {2} days".format(c2 + 1, cal[c2], 31))
    else:
        if c1[c2] in "ansv":
            print("In month {0} which is {1} there are {2} days".format(c2 + 1, cal[c2], 30))
        else:
            print("In month {0} which is {1} there are {2} days".format(c2 + 1, cal[c2], 28))

for t1 in range(1, 31):
    for t2 in range(1, 13):
        print("{0} times {1} = {2}".format(t1, t2, t1 * t2), end = '\t')
    print()

for stnum in range(5, 15):
    print("die nommer is %1d en die nommer gemaal met 5 is %2d en dan is die nommer tot die mag 5 gelyk aan %3d" %(stnum, stnum * 5, stnum ** 5))
    print()
    st = stnum
    print("nom is {0} en x 3 is {1} en tot mag 7 is {2} ".format(st, st * 3, st ** 7))
    print()

name = input("Please enter your name :"); age = int(input("how old are you, {0}?".format(name))); print(age)
if age >= 18:
    print("you are " + str(age) + " and old enough to vote")
    print("Please go to your local vote box and cast your vote within 30 days from now")
else:
    print("Please come back in {0}".format(18 - age) + " years before you can vote")


print("Please guess a number between 20 and 50")
counter1 = 1
guess = int(input())
while guess != 31:
    if (guess < 20) or (guess > 50):
        print("I told you to guess a number HIGHER than 20 and LOWER than 50")
    if guess < 31:
        print("Sorry, your guess is incorrect, guess higher")
        counter1 += 1
        guess = int(input())
    else:
        if guess > 31:
            print("Sorry, your guess is incorrect, guess lower")
            counter1 += 1
            guess = int(input())
if counter1 == 1:
    print("Congratulations, your guess was correct the very 1st time")
else:
    print("Congratulations, your guess was correct at guess number " + str(counter1))

pumpkin = 'Peter Peter Pumpkin Eater'
letter = input("Please enter a character")
if letter in pumpkin:
    print("Give me the letter '{}' my friend".format(letter))
else:
    print("That letter does not appear in the pumpkin affair")

pumpkin = 'Peter Peter Pumpkin Eater'
letter = input("Please enter a character")
if letter not in pumpkin:
    print("That letter does not appear in the pumpkin affair Mr Pumpkin Patch")
else:
    print("Give me the letter '{}' my friend".format(letter))

x1 = ''
x2 = 'p'
if x1:
    print("x1 is true")
if x2:
    print("x2 = true")
input1 = input("Please enter some text")
if input1:
    print("You entered '{}'".format(input1))
else:
    print("You did not enter any text")
print(not True); print(not False)
print(True); print(False)

for pp in range(1, 20):
    if pp == 10:
        print("pp is now {0}".format(pp), end = '\n')
        continue
    print("pp is now {0}".format(pp), end = '\t')

number3 = "0,196,933,719,340,118,134,452,99"

for n1 in range(0, len(number3)):
    print(number3[n1])

for f2 in range(0, len(number3)):
    if number3[f2] in "0123456":
        print(number3 [f2], end = '\t')

for f in range(0, len(number3)):
    if number3[f] in "0123456789":
        print(number3 [f],end='')

cleanednum = ''
for f in range(0, len(number3)):
    if number3[f] in "0123456789":
        cleanednum = cleanednum + number3[f]
newnum = int(cleanednum)
print("  --  The numbers are: {} ".format(newnum))
for char in number3:
    if char in '0123456789':
        cleanednum = cleanednum + char
newnum = int(cleanednum)
print("The numbers are: {} ".format(newnum))

naam = input("wat is jou naampie my liewe mensie ?")
aandete = input("Wat wil jy eet vir aandete {} ".format(naam))
hoeveel = int(input("hoeveel borde van die {}".format(aandete) + " wil jy eet ? "))

t2 = 2
while t2 != 3:
    if hoeveel >= 3:
        print("Nou is jy baie vraatsig")
    else:
        if hoeveel >= 1:
            print("Jy eet gesond hoor")
        else:
            print("Jy eet te min hoor")
    t2 += 1
    naam = input("wat is jou naampie my liewe mensie ?")
    aandete = input("Wat wil jy eet vir aandete {} ".format(naam))
    hoeveel = int(input("hoeveel borde van die {}".format(aandete) + " wil jy eet ? "))


for vrug in ["peer", "lemoen", "nartjie", "perske", "koejawel"]:
    print("Nog 'n vrug waarvan johnny baie hou is " + vrug)
    print("Hy hou van : {}".format(vrug))
for x9 in range(0, 100, 15):
    print("x9 is : {}".format(x9))

quote = "Alright, but apart from the Sanitation, the Medicine, Education, Wine, Public Order, Irrigation, Roads, the Fresh-Water System, and Public Health, what have the Romans ever done for us?"
newchar = ''
for stellie in quote:
    if stellie in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        newchar = newchar + stellie
print("The capital letters in quote are: {} ".format(newchar))
for i in range(0, 100, 7):
    print("numbers are : {}".format(i))

shopping_list = ["milk", "pasta", "bread", "Butter", "Jam", "peanuts", "lemons"]
for item in shopping_list:
    if item in("peanuts", "milk"):
       continue
    print("Buy a healthy item called :  " + item)

groceries = ["milk", "pudding", "jam", "potatoes", "guavas", "butter", "eggs"]
bad_food = ''
for item2 in groceries:
    if item2 in("potatoes", "pudding"):
        bad_food = item2
        print(" {} is a bad food for you - stay away from it ".format(item2)); print()
    else:
        print("a good product to buy is {}".format(item2)); print()

for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break

for i in range(0, 100, 7):
    if (i > 0) and (i % 11 == 0):
        break
    else:
        print (i)
for number in range(0, 20):
    if (number > 0 and ((number % 3 == 0) or (number % 5 == 0))):
        continue
    print("number is : {}".format(number))

x = 23; x += 1; print(x); x -= 4; print(x); x *= 5; print(x); x //= 4; print(x); x **=2; print(x); print(x % 70); print (x)
x %= 70; print(x); greeting = "Good "; greeting += "morning "; print(greeting); greeting *= 5; print(greeting)

ipAddr = input("Please enter an IP address: ")
if ipAddr[-1] != '.':
    ipAddr += '.'
segment = 1
segLength = 0
#char5 = ""
for char5 in ipAddr:
    if char5 == '.':
        print("segment {} contains {} characters".format(segment, segLength))
        segment += 1
        segLength = 0
    else:
        segLength += 1

b = 0
while b < 10:
    print("b is now {}".format(b))
    b += 1

available_exits = ["east", "north east", "south"]
chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit == "quit":
        print("Game Over")
        break
else:
    print("aren't you glad you got out of there!")

money = [821617, 723880, 412177, 299543, 194515, 12]

for dollars in money:
    if dollars == 821617:
        print("This is the bank of Roxanne Vorster with $ {} in it".format(dollars)); print()
    elif dollars == 723880:
        print("This is the bank of Estelle Vorster with $ {} in it".format(dollars)); print()
    elif dollars == 412177:
        print("This is the bank of Natasha Vorster with $ {} in it".format(dollars)); print()
    elif dollars == 299543:
        print("This is the bank of Johan Swan with $ {} in it".format(dollars)); print()
    elif dollars == 194515:
        print("This is the bank of Amanda Smit with $ {} in it".format(dollars)); print()
else:
    print("Hennie Smit wat nie net gedurig nie, maar permanent werkloos is, het maar net $ {} in die bank".format(dollars))

for stellie7 in range(0, 30):
    if stellie7 % 3 != 0 and stellie7 % 5 != 0:
        continue
    print(stellie7)

ipAddress = input("Please enter an IP address: ")
print(ipAddress.count(".e"))
parrot_list = ["non pinin'", "no more", "a stiff", "bereft of live"]

parrot_list.append("A Norwegian Blue")

for state in parrot_list:
    print("This parrot is " + state)

stellie = [4, 15, 21, 26, 30, 39, 45]; swannie = [12, 29, 33, 40, 41, 50, 56]

numbers = stellie + swannie
numbers.sort()
print(numbers)
ordered_numbers = (sorted(numbers))
print(ordered_numbers)

if numbers == ordered_numbers:
    print("The lists are equal")
else:
    print("The lists are not equal")

if ordered_numbers == sorted(numbers):
    print("The lists are equal")
else:
    print("The lists are not equal")

list_1 = []
list_2 = list()
print("List 1: {}".format(list_1))
print("List 2: {}".format(list_2))
if list_1 == list_2:
    print("The lists are equal")
print(list("The lists are equal"))

even1 = [2, 4, 6, 8, 10]
even2 = even1
even2.sort(reverse=True)
print(even1)
print(even2 is even1)

even = [2, 4, 6, 8, 10, 12, 14]
odd = [1, 3, 5, 7, 9, 11, 13, 15]
numbers2 = [even, odd]
print(numbers2)

for number_set in numbers2:
    print(number_set)
    for value in number_set:
        print(value)

another_even = even
another_even = sorted(even, reverse=True)
print(another_even is even)

menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["lekker worsies", "Biltong", "Boerbeskuit"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam", "lekker"])
#print(menu)

for meal in menu:
    if not "spam" in meal:
        print(meal)
        for ingredient in meal:
            print(ingredient)

numb1 = [1, 2, 3, 8, 10, 19, 27]; numb2 = [4, 6, 11, 20, 29, 31]
numb3 = numb1 + numb2
print(numb3); print()
numb4 = (sorted(numb3))
print(numb4)
print()

nommer1 = [5, 8, 11, 23, 43, 45, 56, 91]; nommer2 = [15, 21, 28, 37, 41, 47, 55, 88]
nommer3 = nommer1 + nommer2
print(nommer3); print()
nommer3.sort()
print(nommer3)

small_decimals = range(0, 10)
print(small_decimals)
print(small_decimals.index(3))
