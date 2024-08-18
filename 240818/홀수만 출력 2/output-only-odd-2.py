nlist = input("").split(" ")
b = int(nlist[0])
a = int(nlist[1])

for x in range(b, a-1, -1):
    if x%2 ==1:
        print(x, end=' ')