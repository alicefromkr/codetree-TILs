numlist = input("")
nlist = numlist.split(" ")
n = [int(x) for x in nlist if x != '']
print(int(n[1] > n[0] and n[1] < n[2]))