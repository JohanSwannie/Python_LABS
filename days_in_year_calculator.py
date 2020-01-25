### LAB to use functions to determine the total amount of days for the year up to a given date ###

def isLeapy(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def DinM(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result = days[month -1]
    if month == 2 and isLeapy(year):
        result = 29
    return result

def DoY(year, month, day):
    days = 0
    for m in range(1, month):
        md = DinM(year,m)
        if md == None:
            return None
        days += md
    md = DinM(year, month)
    if day >= 1 and day <= md:
        return days + day
    else:
        return None

w = input("Enter 'Y' to test total amount of days in year for given Date, else enter anything to QUIT : ")

while w == "y" or w == "Y" or w == "Yes" or w == "yes" or w == "YES":
    x = int(input("Please enter a Year : "))
    while True:
        if x < 1582 or x > 2030:
            x = int(input("Please enter a correct Year : "))
        else:
            break
    y = int(input("Please enter a Month : "))
    while True:
        if y < 1 or y > 12:
            y = int(input("Please enter a correct Month : "))
        else:
            break
    z = int(input("Please enter a day : "))
    while True:
        if z < 1 or z > 31:
            z = int(input("Please enter a correct Day : "))
        else:
            break
    print("The TOTAL number of days in the year for the given date {0}-{1}-{2} is : ".format(x, y, z), DoY(x, y, z))
    w = input("Enter 'Y' to test total amount of days in year for given Date, else enter anything else to QUIT : ")

print("You have QUIT the process now - GOODBYE :-)")
