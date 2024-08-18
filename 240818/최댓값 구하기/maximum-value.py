numlist = input("")
nlist = numlist.split(" ")
n = [int(x) for x in nlist if x != '']
print(max(n))