marks ={
    "Kanishk" : 100,
    "Prince" : 85,
    "Avi raj" : 45,
}

d = {}                          # empty dictionary

print(marks.items())            # dict_items([('Kanishk', 100), ('Prince', 85), ('Avi raj', 45)])
print(marks.keys())             # dict_keys(['Kanishk', 'Prince', 'Avi raj'])
print(marks.values())           # dict_values([100, 85, 45])
marks.update({"Avi raj" : 44})
print(marks["Avi raj"])         # 44
print(marks.get("Kanishk"))     # 100
print(len(marks))               # 3