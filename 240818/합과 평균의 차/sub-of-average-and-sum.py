numlist = input("")
num = numlist.split(" ")
n = [int(x) for x in num]
s = sum(n)
a = s//3
print(s)
print(a)
print(s-a)