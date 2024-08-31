n = int(input(""))
arr = []
for i in range(n):
    num = int(input(""))
    if num%3==0 and num%2==1:
        arr.append(num)

arr = sorted(arr)
for x in arr:
    print(x)