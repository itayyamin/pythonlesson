
def count_long_words(message, min_length):
    # Split the message into words by spaces
    words = message.split()

    # Initialize a counter for long words
    long_words_count = 0

    # Iterate through the words
    for word in words:
        # Check if the length of the word is greater than or equal to min_length
        if len(word) >= min_length:
            long_words_count += 1

    # Return the count of long words
    return long_words_count

#test code
def count_long_words2(message, min_length):
    number_of_words = 0
    for i in range(len(message.split())):
        if len(message.split()[i]) >= min_length:
            number_of_words += 1
    return number_of_words




def process_messages1(messages):
    # Initialize the dictionary to store results
    result = {
        "total_messages": len(messages),
        "longest_message": max(messages, key=len) if messages else "",
        "shortest_message": min(messages, key=len) if messages else ""
    }

    return result


def process_messages2(messages):
    # Initialize the dictionary to store results
    result = {
        "total_messages": len(messages),
    }

    # If there are messages, find the longest and shortest
    if messages:
        result["longest_message"] = messages[0]
        result["shortest_message"] = messages[0]

        # Iterate over the messages to update the longest and shortest
        for message in messages[1:]:
            if len(message) > len(result["longest_message"]):
                result["longest_message"] = message
            elif len(message) < len(result["shortest_message"]):
                result["shortest_message"] = message

    return result

def process_and_count(messages, min_length):
    # Process messages and print results
    message_stats = process_messages1(messages)
    print("Message Stats:")
    print(f"Total Messages: {message_stats['total_messages']}")
    print(f"Longest Message: {message_stats['longest_message']}")
    print(f"Shortest Message: {message_stats['shortest_message']}")
    print()

    # Count long words for each message and print the results
    for message in messages:
        long_words_count = count_long_words(message, min_length)
        print(f"Message: \"{message}\" has {long_words_count} long words.")

if __name__ == "__main__":
    # count long words
    message = "This is a simple test message with some long words."
    for i in range(6):
        min_length = i
        print(count_long_words(message, min_length))  # Output:
        print(count_long_words2(message, min_length))  # Output:

    # process messages
    # messages = [
    #     "Hello!",
    #     "This is a longer message.",
    #     "Short message.",
    #     "A really really long message that is by far the longest one."
    # ]
    #
    # result = process_messages1(messages)
    # print(result)
    # result = process_messages2(messages)
    # print(result)
    #
    # # process and count long words
    # messages = [
    #     "This is a test.",
    #     "Another example message with longer words.",
    #     "Short one.",
    #     "An even longer message to test the function properly!"
    # ]
    # min_length = 4
    #
    # process_and_count(messages, min_length)
