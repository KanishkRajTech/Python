a = (1, 3, 4, 5,)
print(type(a)) #<class 'tuple'>

#count(value)
# Returns the number of times the specified value appears in the tuple.
t = (1, 2, 3, 2, 4, 2)
print(t.count(2))  # Output: 3

# index(value[, start[, end]])
# Returns the first index of the specified value.
t = (10, 20, 30, 40, 20)
print(t.index(20))       # Output: 1
print(t.index(20, 2))    # Output: 4

# len()
# Returns the number of elements in a tuple.
t = (5, 10, 15)
print(len(t))  # Output: 3

# Membership Test using in
# Checks if a value exists in the tuple.
t = ('apple', 'banana', 'cherry')
print('banana' in t)  # Output: True
print('grape' in t)   # Output: False


# Tuple Concatenation (+)
# Combines two tuples.
t1 = (1, 2, 3)
t2 = (4, 5)
result = t1 + t2
print(result)  # Output: (1, 2, 3, 4, 5)


# Tuple Repetition (*)
# Repeats the elements in a tuple.
t = ('hi',)
print(t * 3)  # Output: ('hi', 'hi', 'hi')


# Slicing
# Gets a part of the tuple.
t = (0, 1, 2, 3, 4, 5)
print(t[1:4])  # Output: (1, 2, 3)


# Tuple Unpacking
# Assign tuple elements to variables.
t = ('John', 25, 'India')
name, age, country = t
print(name)    # Output: John
print(age)     # Output: 25
print(country) # Output: India