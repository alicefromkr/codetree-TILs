count = 0

for i in range(0, 3):
    plist = input("").split(" ")
    if plist[0] == 'Y' and float(plist[1]) >= 37:
        count+=1
if count >=2:
    print("E")
else:
    print("N")