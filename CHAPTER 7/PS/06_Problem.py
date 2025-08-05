# Write a program to calculate the factorial of a given number using for loop.


num = int(input("Enter the number :"))

mul = 1
for i in range(1,num+1):
   
    mul = mul*i
    i +=1

print(f"Factorial of {num}is {mul}")