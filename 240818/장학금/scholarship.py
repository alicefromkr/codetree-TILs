numlist = input("")
n = numlist.split(" ")
mid = int(n[0])
final = int(n[1])

if mid >= 90:
    if final >= 95:
        print(100000)
    elif final >= 90:
        print(50000)
    else:
        print(0)
else:
    print(0)