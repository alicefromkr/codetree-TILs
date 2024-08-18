d = {"S":"Superior", "A": "Excellent", "B": "Good", "C":"Usually", "D":"Effort"}
c = input("")
if c in d.keys():
    print(d[c])
else:
    print("Failure")