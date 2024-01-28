# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 22:51:57 2024

@author: iliat
"""

class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description=""):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_purchase):
        found = False
        for item in self.cart_items:
            if item.item_name == item_to_purchase.item_name:
                if item_to_purchase.item_price != 0:
                    item.item_price = item_to_purchase.item_price
                if item_to_purchase.item_quantity != 0:
                    item.item_quantity = item_to_purchase.item_quantity
                if item_to_purchase.item_description != "":
                    item.item_description = item_to_purchase.item_description
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items += item.item_quantity
        return num_items

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += (item.item_price * item.item_quantity)
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
            print(f"Total: ${total_cost}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")


def print_menu(cart):
    customer_menu = ("MENU\n"
                     "a - Add item to cart\n"
                     "r - Remove item from cart\n"
                     "c - Change item quantity\n"
                     "i - Output items' descriptions\n"
                     "o - Output shopping cart\n"
                     "q - Quit\n")
    print(customer_menu)
    choice = input("Choose an option:\n")
    while choice != 'q':
        if choice == 'a':
            # Implement Add item to cart logic here
            item_name = input("Enter the item name:\n")
            item_description = input("Enter the item description:\n")
            item_price = float(input("Enter the item price:\n"))
            item_quantity = int(input("Enter the item quantity:\n"))
            new_item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            cart.add_item(new_item)
        elif choice == 'r':
            # Implement Remove item from cart logic here
            item_name = input("Enter name of item to remove:\n")
            cart.remove_item(item_name)
        elif choice == 'c':
            # Implement Change item quantity logic here
            item_name = input("Enter the item name:\n")
            new_quantity = int(input("Enter the new quantity:\n"))
            modified_item = ItemToPurchase(item_name, item_quantity=new_quantity)
            cart.modify_item(modified_item)
        elif choice == 'i':
            # Implement Output items' descriptions logic here
            cart.print_descriptions()
        elif choice == 'o':
            # Implement Output shopping cart logic here
            cart.print_total()
        else:
            print("Invalid option. Please choose a valid option.")

        choice = input("Choose an option:\n")


def main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")

    # Create ShoppingCart object
    cart = ShoppingCart(customer_name, current_date)

    # Call print_menu with ShoppingCart object
    print_menu(cart)


if __name__ == "__main__":
    main()
