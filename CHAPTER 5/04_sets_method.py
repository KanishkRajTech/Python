s = { 40, 1, 2, 3, 10, 4, 5, 1, 1, 1, 5, 8, 9, 10, 9, "Kanishk" }

print(s) # {'Kanishk', 1, 2, 3, 4, 5, 40, 8, 10, 9}

s.add(599)
print(s, type(s)) # {1, 2, 3, 4, 5, 'Kanishk', 40, 8, 10, 9, 599}  <class 'set'>



# PROPERTIES OF PYTHON DICTIONARIES 
# 1. It is unordered. 
# 2. It is mutable. 
# 3. It is indexed. 
# 4. Cannot contain duplicate keys.

s.remove("Kanishk")
print(s, type(s))   # {1, 2, 3, 4, 5, 40, 8, 10, 9, 599} <class 'set'>
s.pop()
print(s, type(s))   # {2, 3, 4, 5, 40, 8, 10, 9, 599} <class 'set'> "pop remove any element from the sets"

s.clear()
print(s, type(s))   # set() <class 'set'>