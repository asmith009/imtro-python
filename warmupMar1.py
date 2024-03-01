# GradeBook system.
grades = [60,70,80,90]

def GradeBook(GradeScore):
    if GradeScore >= grades[3]:
        print('this student has an A.')
    elif GradeScore >= grades[2]:
        print('this sudent has an B')
    elif GradeScore >= grades[1]:
        print('this student has an C.')
    elif GradeScore >= grades[0]:
        print('this sudent has an D')
    else:
        print('this student has an F.')   

GradeBook(99)
