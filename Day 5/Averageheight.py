Students_height=input("Enter students height:\n").split()
print(Students_height)
Height_sum=0
for height in range(0,len(Students_height)):
    Students_height[height]=int(Students_height[height])
    Height_sum+=Students_height[height] #without using sum function
    print(Height_sum)

students_length=0
for students in range(0,len(Students_height)):
    students_length+=1 #withouut using len function
    print(students_length)
Average_height=Height_sum//students_length
print("The Average Height of the Student is:",Average_height)
