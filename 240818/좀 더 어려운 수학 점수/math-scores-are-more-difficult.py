studentA = input("")
ascore = studentA.split(" ")
aEng = int(ascore[1])
aMaths = int(ascore[0])

studentB = input("")
bscore = studentB.split(" ")
bEng = int(bscore[1])
bMaths = int(bscore[0])

if aMaths > bMaths:
    print("A")
elif bMaths > aMaths:
    print("B")
else:
    if aEng >= bEng:
        print("A")
    else:
        print("B")