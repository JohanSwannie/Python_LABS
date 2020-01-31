#####     Lambda Functions Calculator     #####

add = lambda a, b: a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b
modulus = lambda a, b: a % b

i = 0
n = input("what is you name ? ")
print("Welcome", n, " - I hope you find my calculator useful")

while True:
    x = input("enter anything to exit or enter 'c' to Calculate :  ")
    if x == "c":
        op = input("Add(press a), Subtract(press s), Multiply(press m),\nDivide(press d), Modulus(press mo): ").strip().lower()
        if op == "a":
            print("  Sum: " + str(add(float(input("enter 1st number: ")), float(input("enter 2nd number: ")))))
        elif op == "s":
            print("  Subtracted: " + str(subtract(float(input("enter 1st number: ")), float(input("enter 2nd number: ")))))
        elif op == "m":
            print("  Multiplied: " + str(multiply(float(input("enter 1st number: ")), float(input("enter 2nd number: ")))))
        elif op == "d":
            print("  Divided: " + str(divide(float(input("enter 1st number: ")), float(input("enter 2nd number: ")))))
        elif op == "mo":
            print("  Modulus: " + str(modulus(float(input("enter 1st number: ")), float(input("enter 2nd number: ")))))
        else:
            print('Wrong Operation chosen - redo from start', n)
    else:
        print("\nThanks for using my Calculator", n, "\n\n Goodbye")
        break
