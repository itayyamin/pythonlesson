# This function updates the scores dictionary with a student's score.
# If the student already exists in the dictionary, their score is replaced.
def record_score(scores, student_name, score):
    """
    Adds or updates a student's score in the scores dictionary.

    Args:
        scores (dict): A dictionary mapping student names to their quiz scores.
        student_name (str): The name of the student.
        score (int): The score the student received (0 to 10).
    """
    scores[student_name] = score


# This function calculates the average score of the class and identifies
# the top-performing student with the highest score.
def calculate_statistics(scores):
    """
    Calculates the class average and identifies the top scorer.

    Args:
        scores (dict): A dictionary mapping student names to their quiz scores.

    Returns:
        tuple: (average_score (float), top_student_name (str))
    """
    total = sum(scores.values())
    avg = total / len(scores)

    top_student = max(scores, key=scores.get)
    return avg, top_student


# This function prints the entire quiz report:
# Each student's score, the class average, and the top scorer.
def print_quiz_report(scores):
    """
    Displays the scores for each student, the class average,
    and the name of the top-scoring student.

    Args:
        scores (dict): A dictionary of student scores.
    """
    print("📊 Quiz Scores:")
    for student, score in scores.items():
        print(f"{student}: {score}")

    avg, top_student = calculate_statistics(scores)
    print(f"\nClass average: {avg:.2f}")
    print(f"🏆 Top scorer: {top_student}")


# The main function handles user input and drives the program.
def main():
    """
    Main program loop that allows the teacher to input scores
    for multiple students and then displays the quiz report.
    """
    scores = {}

    n = int(input("How many students? "))
    for _ in range(n):
        name = input("Student name: ")
        score = int(input("Score (0-10): "))
        record_score(scores, name, score)

    print()
    print_quiz_report(scores)


# Entry point of the script
if __name__ == "__main__":
    main()
