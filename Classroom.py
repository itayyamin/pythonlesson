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



# This function prints the entire quiz report:
# Each student's score, the class average, and the top scorer.
def print_quiz_report(scores):
    """
    Displays the scores for each student, the class average,
    and the name of the top-scoring student.

    Args:
        scores (dict): A dictionary of student scores.
    """



# The main function handles user input and drives the program.
def main():
    """
    Main program loop that allows the teacher to input scores
    for multiple students and then displays the quiz report.
    """



# Entry point of the script
if __name__ == "__main__":
    main()
