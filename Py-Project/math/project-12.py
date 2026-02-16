# Grade Calculator 

def get_grades():
    marks = []
    subjects = int(input("Number of subjects: "))
    for i in range(subjects):
        marks.append(float(input(f"Marks {i+1}: ")))
    return marks

def calculate_grade(marks):
    avg = sum(marks) / len(marks)
    if avg >= 90: return "A+"
    elif avg >= 80: return "A"
    elif avg >= 70: return "B"
    else: return "C"

marks = get_grades()
grade = calculate_grade(marks)
print(f"Average: {sum(marks)/len(marks):.1f} | Grade: {grade}")
