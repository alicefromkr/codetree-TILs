numlist = input("")
num = numlist.split(" ")
h = int(num[0])
w = int(num[1])
b = (10000*w)//(h*h)
print(b)
if b >=25:
    print("Obesity")