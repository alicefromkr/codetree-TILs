numlist = input("")
num = numlist.split(" ")

def calc(n):
    n = int(n)
    if n %2 == 0:
        print("even")
    else:
        print("odd")
for x in num:
    calc(x)