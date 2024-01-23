# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 00:02:05 2024

@author: iliat
"""

class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")


# Item 1
print("Item 1")
item_name_1 = input("Enter the item name: ")
item_price_1 = float(input("Enter the item price: "))
item_quantity_1 = int(input("Enter the item quantity: "))

item_1 = ItemToPurchase(item_name_1, item_price_1, item_quantity_1)

# Item 2
print("\nItem 2")
item_name_2 = input("Enter the item name: ")
item_price_2 = float(input("Enter the item price: "))
item_quantity_2 = int(input("Enter the item quantity: "))

item_2 = ItemToPurchase(item_name_2, item_price_2, item_quantity_2)

# Calculate and print total cost
total_cost = item_1.item_quantity * item_1.item_price + item_2.item_quantity * item_2.item_price

print("\nTOTAL COST")
item_1.print_item_cost()
item_2.print_item_cost()
print(f"Total: ${total_cost}")
