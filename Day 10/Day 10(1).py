#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import sys
sys.path.append('./')
from inventory_utils import export_inventory_report

class Product:
    def __init__(self, name, price, quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def total_value(self):
        return self.price*self.quantity

    def get_info(self):
        return f'{self.name} -> Quantity: {self.quantity}, Unit Price: Rs.{self.price}, Total Value: Rs.{self.total_value():.2f}'


class PerishableProduct(Product):
    def __init__(self, name, price, quantity, expiry_days):
        super().__init__(name, price, quantity)
        self.expiry_days = expiry_days

    def total_value(self):
        if self.expiry_days<5:
            discount =(self.price * self.quantity) * 0.2
            return (self.price * self.quantity) - discount
        else:
            return super().total_value()

    def get_info(self):
        info = super().get_info()
        if self.expiry_days < 5:
            return f'{info} (20% discount: Expiry in {self.expiry_days} days)'
        return info


class InventoryManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_inventory(self):
        print("\n--- Inventory ---")
        if not self.products:
            print("No products in inventory.")
        for i, product in enumerate(self.products, 1):
            print(f'{i}. {product.get_info()}')

    def search_by_name(self, term):
        print(f"\n--- Search Results for '{term}' ---")
        results = list(filter(lambda p: term.lower() in p.name.lower(), self.products))
        if results:
            for p in results:
                print(p.get_info())
        else:
            print("No matching product found.")

    def restock_randomly(self):
        for product in self.products:
            added = random.randint(1, 10)
            product.quantity += added
        print("\nProducts have been restocked.")


def main_menu():
    print('\t---| INVENTORY MANAGEMENT SYSTEM |---\n')
    inventory = InventoryManager()

    # Preload some products
    inventory.add_product(Product("Banana", 5, 10))
    inventory.add_product(PerishableProduct("Milk", 4, 5, 2))

    while True:
        print("\n---< MENU >---")
        print("1. Add Product")
        print("2. List Inventory")
        print("3. Search by Name")
        print("4. Restock Randomly")
        print("5. Export Inventory Report")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter product name: ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            perishable = input("Is this product perishable? (yes/no): ").strip().lower()

            if perishable == 'yes':
                expiry = int(input("Enter days until expiry: "))
                product = PerishableProduct(name, price, quantity, expiry)
            else:
                product = Product(name, price, quantity)

            inventory.add_product(product)
            print(f"{name} added to inventory.")

        elif choice == '2':
            inventory.list_inventory()

        elif choice == '3':
            term = input("Enter name to search: ")
            inventory.search_by_name(term)

        elif choice == '4':
            inventory.restock_randomly()

        elif choice == '5':
            print("Calling export function...")
            export_inventory_report(inventory.products)
            print("Inventory report exported successfully.")

        elif choice == '6':
            print("Exiting Inventory Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main_menu()


# In[ ]:




