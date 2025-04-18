# -----------------------------
# File: product_task.py
# -----------------------------
# Task: Manage product inventory
# Focus: Method with conditionals

class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    # TODO: Add a method sell(quantity) that reduces stock if enough, otherwise print error


# Instructions:
# 1. Implement the sell method.
# 2. Create a Product called "Notebook" with 20 units in stock
# 3. Sell 5, then print the stock
# 4. Try selling 30 and make sure it prints an error
