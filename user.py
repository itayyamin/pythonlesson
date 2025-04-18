def get_user_info():
    # Get user input
    name = input("What is your name? ")

    # Get age and ensure it is an integer
    while True:
        try:
            age = int(input("How old are you? "))
            break  # Break the loop if the input is a valid integer
        except ValueError:
            print("Please enter a valid integer for age.")

    location = input("Where do you live? ")

    # Print the collected information
    print("\nUser Information:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Location: {location}")


# Example Usage:
get_user_info()
