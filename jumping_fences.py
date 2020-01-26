# Jumping Fences

def jumpingFences(c):
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
j = jumpingFences(c)
print(j)
