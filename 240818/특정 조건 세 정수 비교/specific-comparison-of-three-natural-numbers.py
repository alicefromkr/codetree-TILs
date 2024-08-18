numlist = input("")
n = numlist.split(" ")
nlist = [int(x) for x in n]
m = min(nlist)
print(int(m == nlist[0]), int(all(m == x for x in nlist)))