a = int(input(""))
numlist = input("")
num = numlist.split(" ")
nlist = [int(x) for x in num]
for n in nlist:
    print(int(a>n))