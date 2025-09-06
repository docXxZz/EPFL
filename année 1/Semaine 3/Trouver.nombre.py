def trouver_nombre(a, b):
    m=(a+b)//2
    print(f"est-ce que c'est {m} ?")
    r=input()
    
    if r=="=":
        print("ok")
    elif r=="<":
        trouver_nombre(a, m-1)
    else:
        trouver_nombre(m+1, b)

trouver_nombre(0,1000)