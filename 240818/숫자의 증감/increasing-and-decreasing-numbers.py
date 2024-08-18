info = input("").split(" ")
c = info[0]
n = int(info[1])

if c == 'A':
    for x in range(1, n+1):
        print(x, end=' ')
else:
    for x in range(n, 0, -1):
        print(x, end=' ')