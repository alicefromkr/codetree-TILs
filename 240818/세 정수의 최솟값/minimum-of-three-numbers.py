numlist = input("")
n = numlist.split(" ")
nlist = [int(x) for x in n if x!='']
print(min(nlist))