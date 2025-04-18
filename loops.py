# -----------------------------
# File: loops_comparison.py
# -----------------------------
# Topic: Loops in Python
# Focus: Using range() vs direct iteration over lists or strings

# -----------------------------
# Example 1: Loop with range()
# -----------------------------
print("Example 1: Loop with range()")
for i in range(5):
    print("Index:", i)
# Output: 0, 1, 2, 3, 4

# -----------------------------
# Example 2: Loop through a list
# -----------------------------
print("\nExample 2: Loop through a list")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)
# Output: apple, banana, cherry


# -----------------------------
# Example 3: Loop with range + list index
# -----------------------------
print("\nExample 3: Loop with range and index on list")
for i in range(len(fruits)):
    print("Fruit at index", i, "is", fruits[i])
# Output: shows index + item

# -----------------------------
# Example 4: Loop through a string
# -----------------------------
print("\nExample 4: Loop through a string")
word = "economy"
for char in word:
    print("Letter:", char)
# Output: e, c, o, n, o, m, y

# -----------------------------
# Example 5: Loop with range and index on string
# -----------------------------
print("\nExample 5: Loop with range and index on string")
for index in range(len(word)):
    print("Index", index, ":", word[index])
# Output: shows index + letter
