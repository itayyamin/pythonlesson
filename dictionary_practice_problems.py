def word_count(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Create an empty dictionary to store word counts
    count_dict = {}

    # Loop through each word
    for word in words:
        # If the word is already in the dictionary, increase its count
        if word in count_dict:
            count_dict[word] += 1
        # Otherwise, add the word to the dictionary with count 1
        else:
            count_dict[word] = 1

    return count_dict

def find_people_by_age(people, age):
    result = []
    for name, person_age in people.items():
        if person_age == age:
            result.append(name)
    return result

def merge_dicts(dict1, dict2):
    merged = dict1.copy()  # Start with a copy of dict1
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged

def char_count(s):
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count


def most_frequent_word(sentence):
    words = sentence.split()
    count = {}

    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    max_word = max(count, key=count.get)
    return (max_word, count[max_word])

if __name__ == "__main__":

    # word count

    sentence = "hello world hello"
    result = word_count(sentence)
    print(result)  # Output: {'hello': 2, 'world': 1}

    # find people by age
    # Example
    people = {
        "Alice": 30,
        "Bob": 25,
        "Charlie": 30,
        "Diana": 22
    }
    print(find_people_by_age(people, 30))  # ['Alice', 'Charlie']

    # merge dictionaries
    dict1 = {"apple": 3, "banana": 2}
    dict2 = {"banana": 5, "orange": 4}
    print(merge_dicts(dict1, dict2))  # {'apple': 3, 'banana': 7, 'orange': 4}

    # character count
    print(char_count("hello"))  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}

    # most frequent word
    print(most_frequent_word("dog cat dog dog bird"))  # ("dog", 3)`