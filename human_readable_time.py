# Human Readable Time 

def make_readable(seconds):
    if seconds > 86400:
        return "No such a time"
    msg = "Your Human readable Time is -> "
    ot, oth, otm, ots = 0,0,0,0
    ot = seconds // 60
    ots = seconds % 60
    if ot > 59:
        oth = ot // 60
        otm = ot % 60
    else:
        otm = ot
    return ('{:29s} {:02d}:{:02d}:{:02d}'.format(msg, oth,otm,ots))

x = int(input('Enter seconds smaller than 86401 : '))
print(make_readable(x))
