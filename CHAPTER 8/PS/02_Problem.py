#  Write a python program using function to convert Celsius to Fahrenheit.

def f_to_c(f):
    c = 5*(f-32)/9
    return c

f = int(print("Enter temperature in f")) 
print(f_to_c(f))