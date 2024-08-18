num=input("")
numlist = num.split(" ")
n = [int(x) for x in numlist]
s = sum(n)
a = s//3
print(s)
print(a)