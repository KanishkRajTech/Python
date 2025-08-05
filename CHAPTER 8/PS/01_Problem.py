# Write a program using functions to find greatest of three numbers.

def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(a>b and a>c):
        return c
a = 1
b = 3
c = 7
print(greatest(a, b, c))