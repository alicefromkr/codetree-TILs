po_list = input("")
po = po_list.split(" ")
po_age = int(po[0])
po_sex = po[1]

pt_list = input("")
pt = pt_list.split(" ")
pt_age = int(pt[0])
pt_sex = pt[1]

print(int(( pt_age >=19 and pt_sex == "M") or (po_sex == "M" and po_age >= 19)))