# This class collects student grades and calculates the average.
# Input: number of students, and for each: name and grade.
# Output: Dictionary { student_name: grade }

class Report:
    def __init__(self, teacher_name, number_of_students):
        self.teacher_name = teacher_name
        self.number_of_students = number_of_students
        self.grades = {}

    def get_student_grades(self):
        for _ in range(self.number_of_students):
            name = input("Enter student name: ")
            grade = float(input("Enter grade (0-100): "))
            self.grades[name] = grade
        return self.grades

    def get_teacher_name(self):
        return self.teacher_name

    def calculate_average(self):
        average = sum(self.grades.values()) / len(self.grades)
        return average

    def calculate_average_loop(self):
        grades_sum = 0

        for grade in self.grades.values():
            grades_sum += grade

        return grades_sum / len(self.grades)

def main():


    shola_report = Report("shola",2)
    dani_report = Report("dani", 12)

    print(shola_report.get_teacher_name())
    print(dani_report.get_teacher_name())

    # teacher = input("Enter teacher name: ")
    # n = int(input("Enter number of students: "))
    #
    # report_instance = Report(teacher, n)
    # grades = report_instance.get_student_grades()
    # average = report_instance.calculate_average()
    #
    # print("\nStudent Grades:")
    # for name, grade in grades.items():
    #     print(f"{name}: {grade}")
    #
    # print(f"\nClass average: {average:.2f}")

if __name__ == "__main__":
    main()
