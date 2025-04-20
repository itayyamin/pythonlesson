# -----------------------------
# File: teacher_class.py
# -----------------------------
# Task: Teacher class with properties, methods, and string formatting
# Focus: `__repr__`, `__eq__`, and custom methods

class Teacher:
    def __init__(self, name, salary, subject):
        self.name = name
        self.salary = salary
        self.subject = "_______________"  # Example of an additional property

    # Method to represent the object as a string
    def __repr__(self):
        return f""  # <-- Complete string formatting

    # Method to compare two Teacher objects based on name and salary
    def __eq__(self, other):
        if isinstance(other, Teacher):
            return self.name == other.name and self.salary == other.salary
        return False

    # Custom function to calculate yearly salary (optional: with bonus)
    def yearly_salary(self, bonus=0):
        return "_______________"  # <-- Implement yearly salary calculation with bonus if provided

    # Additional method for string concatenation or any custom behavior
    def full_description(self):
        return "_______________"  # <-- Complete string formatting


# Main program to play with the code
if __name__ == "__main__":
    # Creating Teacher objects
    teacher1 = Teacher("John Doe", 4000, "Mathematics")
    teacher2 = Teacher("Jane Smith", 4500, "Physics")
    teacher3 = Teacher("John Doe", 4000, "Mathematics")  # Same name and salary as teacher1

    # Print object representation
    print(teacher1)
    print(teacher2)

    # Compare teachers
    print(f"Are teacher1 and teacher3 the same? {teacher1 == teacher3}")  # Expected: True

    # Calculate yearly salary with a bonus for teacher1
    print(f"{teacher1.name}'s yearly salary (with bonus): {teacher1.yearly_salary(1000)}")

    # Get a full description of teacher2
    print(f"Full description of teacher2: {teacher2.full_description()}")

# Teacher(name='John Doe', salary='4000', subject='Mathematics')
# Teacher(name='Jane Smith', salary='4500', subject='Physics')
# Are teacher1 and teacher3 the same? True
# John Doe's yearly salary (with bonus): 49000
# Full description of teacher2: Jane Smith teaches Physics and earns a salary of 4500
