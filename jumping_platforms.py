# Jumping Platforms - 1st input = how many Platforms - 2nd input 0 for each save Platform & 1 for each unsafe Platform
# Jumping the Platforms to the last safe Platform can only happen in either 1 or 2 jumps
# The following algorithm will work out the amount of safe jumps to get to the last safe Platform - last Platform always a safe one

def jumpingPlatforms(c):
    c.append(2)
    c.append(2)
    j = 0
    l = len(c)
    i = 0
    while i < l:
        if c[i] == 0:
            if c[i + 2] == 2:
                if c[i] == c[i + 1]:
                    i += 1
                    j += 1
                else:
                    i += 1
            elif c[i] == c[i + 2]:
                i += 2
                j += 1
            elif c[i] == c[i + 1]:
                i += 1
                j += 1
            else:
                i += 1
        else:
            i += 1
    return j

n = int(input())
c = list(map(int, input().rstrip().split()))
j = jumpingPlatforms(c)
print(j)
