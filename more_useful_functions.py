# Sorted Function 

print("Sorted Function")
fruits = ['lime', 'blueberry', 'plum', 'avocado']
print(sorted(fruits), end = '  ->  ')
print(sorted(fruits, reverse=True))
ages = [45, 11, 30, 20, 55]
print(sorted(ages), end = '  ->  ')
print(sorted(ages, reverse=True))

# Enumerate Function

print("Enumerate Function")
print(list(enumerate("hello")) )
for index, value in enumerate("hello"):
    print('index : ', index, 'value : ', value)

# Reversed Function

print("Reversed Function")
print(reversed([44, 11, -90, 55, 3]))
print(list(reversed([44, 11, -90, 55, 3])))
print(list(reversed((6, 1, 3, 9))))
print(list(reversed("hello")))

# Range Function  

print("Range Function")
print(range(5), end = '     ')
print(list(range(5)), end = '  ')
print(list(range(5, 10)))
print(list(range(-2, 2)), end = '     ')
print(list(range(-100, -95)))
print(range(1, 20, 3), end = '     ')
print(list(range(1, 20, 3)))
print(list(range(20, 10, -1)), end = '     ')
print(list(range(20, 10, -5)))

# Min, Max Functions 

print("Max + Min Functions")
print(max("c", "b", "a", "Y", "Z"), end = '   ')
print(max("c", "b", "a", "Y", "Z", key=str.lower))
print(min("c", "b", "a", "Y", "Z"), end = '    ')
print(min("c", "b", "a", "Y", "Z", key=str.lower))


# Chr Function   

print("chr Function")
print(chr(65))
print(chr(102))
print(chr(225))
print(chr(21325))
print(chr(128512))

# Any & All Functions

print("any & all Functions")
print(any([10, "", "one"]), end = '    ')
print(any(("", {})), end = '    ')
print(any([]), end ='    ')
gen = (i for i in [5, 0, 0.0, 4])
print(any(gen))
print(all(['alpha', 'beta', '']), end = '    ')
print(all(['one', 'two', 'three']), end = '    ')
print(all([]), end = '    ')
gen = (i for i in ['0', (), {}, 51, 89])
print(all(gen))
