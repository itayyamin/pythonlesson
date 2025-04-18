# dictionary_demo.py

def create_dictionary():
    dict = {
        "name": "Alice",
        "age": 25,
        "city": "New York"
    }

    return dict


def access_value(d, key):
    if key in d:
        return d[key]
    else:
        return None
        return f"{key} not found."





def add_or_update(d, key, value):
    d[key] = value + d[key]
    return d


def delete_key(d, key):
    if key in d:
        del d[key]
        return f"'{key}' deleted."
    else:
        return f"'{key}' not found in dictionary."


def check_key_exists(d, key):
    return key in d


def display_dictionary(d):
    for key, value in d.items():
        print(f" this is the {key}: this is the value {value}")


if __name__ == "__main__":

    # print("🔧 Creating dictionary...")
    # my_dict = create_dictionary()

    # print("\n📋 Initial dictionary:")
    # display_dictionary(my_dict)
    #
    # print("\n🔍 Accessing value for key 'name':")
    # print(access_value(my_dict, "name"))
    #
    # print("\n➕ Adding a new key 'email':")
    # add_or_update(my_dict, "email", "alice@example.com")
    # display_dictionary(my_dict)
    #
    # print("\n✏️ Updating key 'age':")
    # add_or_update(my_dict, "age", 26)
    # display_dictionary(my_dict)
    #
    # print("\n❌ Deleting key 'city':")
    # print(delete_key(my_dict, "city"))
    # display_dictionary(my_dict)
    #
    # print("\n🔎 Checking if 'name' exists in dictionary:")
    # print(check_key_exists(my_dict, "name"))


    # dict = {
    #     "apple": "2",
    #     "banana": "5",
    #     "pizza": "7",
    #     "ice cream": "7",
    # }
    #
    # for key, value in dict.items():
    #     print(f" this is the {key}: this is the value {value}")

    # for key, value in dict.items():
    #     print(f"{key}: {value}")

    print("--------------------------")


    # tup = ("key1", "value1")
    # print(tup)
    #

    # print(dict.items())

    # for x in dict.items():
    #     print(x)
    #
    # for x,y in dict.items():
    #     print(f"{x}: {y}")
    #
    # for key in dict.keys():
    #     print(key)
    #
    # for value in dict.values():
    #     print(value)


