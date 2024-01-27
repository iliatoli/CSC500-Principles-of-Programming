# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 22:51:24 2024

@author: iliat
"""

class ItemToPurchase:
    def __init__(self, name="none", price=0.0, quantity=0, description="none"):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description

    def print_item_cost(self):
        total = self.price * self.quantity
        print(f"{self.name} {self.quantity} @ ${self.price:.2f} = ${total:.2f}")

    def print_item_description(self):
        print(f"{self.name}: {self.description}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        item_found = False
        for item in self.cart_items:
            if item.name == item_name:
                self.cart_items.remove(item)
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_purchase):
        item_found = False
        for i, item in enumerate(self.cart_items):
            if item.name == item_to_purchase.name:
                if item_to_purchase.description != "none":
                    self.cart_items[i].description = item_to_purchase.description
                if item_to_purchase.price != 0.0:
                    self.cart_items[i].price = item_to_purchase.price
                if item_to_purchase.quantity != 0:
                    self.cart_items[i].quantity = item_to_purchase.quantity
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = sum(item.quantity for item in self.cart_items)
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = sum(item.price * item.quantity for item in self.cart_items)
        return total_cost

    def print_total(self):
        total_cost = self.get_cost_of_cart()
        if total_cost == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${total_cost:.2f}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()


def print_menu(cart):
    menu = ("\nMENU\n"
            "a - Add item to cart\n"
            "r - Remove item from cart\n"
            "c - Change item quantity\n"
            "i - Output items' descriptions\n"
            "o - Output shopping cart\n"
            "q - Quit\n")

    command = ''
    while command != 'q':
        print(menu)
        command = input("Choose an option:\n")

        if command == 'a':
            print("\nADD ITEM TO CART")
            item_name = input("Enter the item name:\n")
            item_description = input("Enter the item description:\n")
            item_price = float(input("Enter the item price:\n"))
            item_quantity = int(input("Enter the item quantity:\n"))
            new_item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            cart.add_item(new_item)

        elif command == 'r':
            print("\nREMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove:\n")
            cart.remove_item(item_name)

        elif command == 'c':
            print("\nCHANGE ITEM QUANTITY")
            item_name = input("Enter the item name:\n")
            quantity = int(input("Enter the new quantity:\n"))
            item_to_modify = ItemToPurchase(item_name, quantity=quantity)
            cart.modify_item(item_to_modify)

        elif command == 'i':
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif command == 'o':
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()

        elif command == 'q':
            print("Quit")


def main():
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)

if __name__ == "__main__":
    main()
