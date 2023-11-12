class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
        print(f"{quantity} {item_name}(s) added to the inventory.")

    def update_quantity(self, item_name, new_quantity):
        if item_name in self.items:
            self.items[item_name] = new_quantity
            print(f"Quantity of {item_name} updated to {new_quantity}.")
        else:
            print(f"{item_name} not found in the inventory.")

    def view_inventory(self):
        if not self.items:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for item, quantity in self.items.items():
                print(f"{item}: {quantity}")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"{item_name} removed from the inventory.")
        else:
            print(f"{item_name} not found in the inventory.")

def main():
    inventory = Inventory()

    while True:
        print("\nMenu:")
        print("1. Add new item to the inventory")
        print("2. Update existing item's quantity")
        print("3. View current inventory")
        print("4. Remove item from inventory")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            item_name = input("Enter the item name: ")
            quantity = int(input("Enter the quantity: "))
            inventory.add_item(item_name, quantity)

        elif choice == '2':
            item_name = input("Enter the item name to update: ")
            new_quantity = int(input("Enter the new quantity: "))
            inventory.update_quantity(item_name, new_quantity)

        elif choice == '3':
            inventory.view_inventory()

        elif choice == '4':
            item_name = input("Enter the item name to remove: ")
            inventory.remove_item(item_name)

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
