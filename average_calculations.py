#  average calculations

def average_Calc(arr):
    global d
    global e
    global f
    a = 0
    b = 0
    c = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            a += 1
        elif arr[i] == 0:
            c += 1
        else:
            b += 1
    d = (a / len(arr))
    e = (b / len(arr))
    f = (c / len(arr))
    return d, e, f
    
arr = list(map(int, input('Enter positive, negative and zeros on same line :  ').rstrip().split()))
average_Calc(arr)
print('Positive numbers average of overall numbers entered is : ' , d)
print('Negative numbers average of overall numbers entered is : ' , e)
print('Zero numbers average of overall numbers entered  is : ' , f)
