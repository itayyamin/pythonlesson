# This function collects student grades into a dictionary.
# Input: number of students, and for each: name and grade.
# Output: Dictionary { student_name: grade }
def get_student_grades(n):
    grades = {}
    for _ in range(n):
        name = input("Enter student name: ")
        grade = float(input("Enter grade (0-100): "))
        grades[name] = grade
    return grades

# This function calculates the average of all grades.
# Input: Dictionary of grades
# Output: Average grade (float)
def calculate_average(grades):
    total = sum(grades.values())
    return total / len(grades)

def main():
    n = int(input("Enter number of students: "))
    grades = get_student_grades(n)
    average = calculate_average(grades)

    print("\nStudent Grades:")
    for name, grade in grades.items():
        print(f"{name}: {grade}")

    print(f"\nClass average: {average:.2f}")

if __name__ == "__main__":
    main()
