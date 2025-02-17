# Code below this line

#Dictionary
#key:str(name), value:int(score)
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco' : 75,
    'Neville': 60,
}

#empty dictionary
student_grades = {}


for key in student_scores:
    if student_scores[key] >= 91:
        student_grades[key] = "Outstanding"
    elif 81 <= student_scores[key] <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif 71 <= student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
    elif student_scores[key] <= 70:
        student_grades[key] = "Fail"
    else:
        pass

print(student_grades)

    #print(student_scores[key])