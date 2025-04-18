# inventory_manager.py

class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: {self.quantity}"


class Inventory:
    def __init__(self):
        self.items = {}  # Dictionary to store items: key = name, value = Item object

    def add_item(self, name, quantity):
        if name in self.items:
            print(f"{name} already exists. Use update_quantity instead.")
        else:
            self.items[name] = Item(name, quantity)
            print(f"Added {name} with quantity {quantity}.")

    def update_quantity(self, name, quantity):
        if name in self.items:
            self.items[name].quantity = quantity
            print(f"Updated {name} to quantity {quantity}.")
        else:
            print(f"{name} not found in inventory.")

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            print(f"Removed {name} from inventory.")
        else:
            print(f"{name} not found in inventory.")

    def print_inventory(self):
        if not self.items:
            print("Inventory is empty.")
        else:
            print("📦 Current Inventory:")
            for item in self.items.values():
                print(f" - {item}")



# Example usage
if __name__ == "__main__":
    inventory = Inventory()

    inventory.add_item("apple", 10)
    inventory.add_item("banana", 5)
    inventory.add_item("orange", 8)

    inventory.print_inventory()

    inventory.update_quantity("banana", 10)
    inventory.remove_item("apple")
    inventory.add_item("pear", 4)

    inventory.print_inventory()
