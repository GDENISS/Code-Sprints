
def gradingStudents(grades):
    if grades < 40:
        return f'pass'
    elif grades > 40 and grades % 5== 0 :
        return f'pass'
    elif grades >40 and grades % 5 != 0:
        return grades +2
    
    return grades

print(gradingStudents(78))
