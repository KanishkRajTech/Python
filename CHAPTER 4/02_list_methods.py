friends = ["Apple", "Orange", 5, 345.06, False, "Kanishk", "Rohan"]

friends.append("Akash")
print(friends)   # ['Apple', 'Orange', 5, 345.06, False, 'Kanishk', 'Rohan', 'Akash']


#Sort
l1= [1, 8, 7, 2, 21, 15]
l1.sort()
print(l1)       # [1, 2, 7, 8, 15, 21]

#Reverse
l2= [1, 8, 7, 2, 21, 15]
l2.reverse()
print(l2)       #[15, 21, 2, 7, 8, 1]

#Insert
l3= [1, 8, 7, 2, 21, 15]
l3.insert(3,8)
print(l3)       #[1, 8, 7, 8, 2, 21, 15]

#Pop
l4= [1, 8, 7, 2, 21, 15]
l4.pop(2)
print(l4)       #[1, 8, 2, 21, 15]

#Remove
l5= [1, 8, 7, 2, 21, 15]
l5.remove(21)
print(l5)       #[1, 8, 7, 2, 15]