numlist = input("").split(" ")
a = int(numlist[0])
b = int(numlist[1])

if a%2 == 1:
    a-=1

while a >=b:
    print(a, end=' ')
    a-=2