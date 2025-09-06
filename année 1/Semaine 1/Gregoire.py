def saut(x, y, z, a):
    a = 0
    x = 4
    y = 2
    while z != 6:
        x=x+1
        y=y+1
        x=x+1
        y=y-1
        x=x+1
        y=y+1
        x=x-1
        y=y+1
        a += 1
        z += 4

    if (x == 7 and y == 7) :
        z = a*4
        print (z)

    else:
        print("Never")