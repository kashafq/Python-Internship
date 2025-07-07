#!/usr/bin/env python
# coding: utf-8

# In[37]:


import random
import sys
sys.path.append('./')
from inventory_utils import export_inventory_report

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

class PerishableProduct(Product):
    def __init__(self, name, price, quantity, expiry_days):
        super().__init__(name, price, quantity)
        self.expiry_days = expiry_days

    def total_value(self):
        if self.expiry_days < 5:
            print('You get a 20% discount')
            discount = (self.price * self.quantity) * 0.2
            return (self.price * self.quantity) - discount
        else:
            return super().total_value()


class InventoryManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_inventory(self):
        print("\n--- Inventory ---")
        for i, product in enumerate(self.products, 1):
            print(f'{i}. {product.name} -> Quantity: {product.quantity}, Value: Rs.{product.total_value()}')

    def search_by_name(self, term):
        print(f"\n--- Search Results for '{term}' ---")
        results = list(filter(lambda p: term.lower() in p.name.lower(), self.products))
        for p in results:
            print(f'{p.name} -> Quantity: {p.quantity}, Value: Rs.{p.total_value()}')

    def restock_randomly(self):
        for product in self.products:
            product.quantity += random.randint(1, 10)

inventory = InventoryManager()

inventory.add_product(Product("Apple", 5, 10))
inventory.add_product(PerishableProduct("Milk", 4, 5, 2))

inventory.list_inventory()
inventory.search_by_name("milk")
inventory.restock_randomly()
inventory.list_inventory()

export_inventory_report(inventory.products)


# In[ ]:




