def maximus(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
a=input('enter a: ')
b=input('enter b: ')
c=input('enter c: ')
print(f"max of {a},{b},{c} is {maximus(a,b,c)}")
