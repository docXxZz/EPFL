def Syracuse(i):
    z = 0
    while i != 1:
        if i%2 ==0:
            i = i/2
        else:
            i = 3*i+1
        z += 1
    return z
    

z = Syracuse(int(input()))
print(z)
