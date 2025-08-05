# Write a program to find the sum of first n natural numbers using while loop. 

num = int(input("Enter the number :"))

i = 0
sum = 0
while(i <= num):
   
    sum = sum+i
    i +=1

print(f"Sum of sum of first {num} natural numbers is {sum}")