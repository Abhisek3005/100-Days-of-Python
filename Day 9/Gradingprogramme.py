students_score={
    "Harry":81,
    "Peter":78,
    "Abhilipsa":99,
    "Trupti":74,
    "Puja":62
}
students_grades={}
for student in students_score:
    #print(student)
    score=students_score[student]
    #print(score)
    if score > 90:
        students_grades[student]="Outstanding"
    elif score > 80:
        students_grades[student] = "Exceeds Expectations"    
    elif score >  70:
        students_grades[student] = "Acceptable"
    else:
        students_grades[student] = "Fail"        
print(students_grades)        