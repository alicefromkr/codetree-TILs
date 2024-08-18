numlist = input("")
n = numlist.split(" ")
nlist = [int(x) for x in n]
print(min(nlist))