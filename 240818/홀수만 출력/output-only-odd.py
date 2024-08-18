nlist = input("").split(" ")
a = int(nlist[0])
b = int(nlist[1])

for x in range(a, b+1):
    if x%2 == 1:
        print(x, end=' ')