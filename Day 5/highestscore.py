students_score=input("Enter the students score \n").split()
print(students_score)
for n in range(0,len(students_score)):
    students_score[n]=int(students_score[n])
highest_score=0    
for score in students_score:    
    if highest_score<score:
        highest_score=score
print(f"The highest score in the class is:{highest_score}")        
