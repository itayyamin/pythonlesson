
def count_long_words(message, min_length):


#test code
def count_long_words2(message, min_length):





def process_messages1(messages):



def process_messages2(messages):


def process_and_count(messages, min_length):


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
