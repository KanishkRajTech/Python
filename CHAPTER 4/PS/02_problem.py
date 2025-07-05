# Write a program to accept marks of 6 students and display them in a sorted  manner. 

marks = []

s1 = int(input("Enter the 1st student marks: "))
marks.append(s1)
s2 = int(input("Enter the 2nd student marks: "))
marks.append(s2)
s3 = int(input("Enter the 3rd student marks: "))
marks.append(s3)
s4 = int(input("Enter the 4th student marks: "))
marks.append(s4)
s5 = int(input("Enter the 5th student marks: "))
marks.append(s5)
s6 = int(input("Enter the 6th student marks: "))
marks.append(s6)

marks.sort()

print(marks)
