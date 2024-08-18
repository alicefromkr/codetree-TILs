a = int(input(""))

def calc(a):
    if a%2 == 0:
        return(a//2)
    else:
        return((a+1)//2)

b = calc(a)
c = calc(b)
print(c)