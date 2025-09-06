def saut(x, y):
    if x == y:
        if x % 2 == 0:
            return x*2
        else:
            return x*2-1
    elif x == y + 2:
        if y % 2 == 0:
            return y*2 + 2
        else:
            return y*2 + 1
    else:
        return None

x, y  = [int(x) for x in input().split()]

z = saut(x, y)
if z == None:
    print("JAMAIS")
else:
    print(z)