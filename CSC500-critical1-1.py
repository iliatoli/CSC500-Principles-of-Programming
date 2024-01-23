# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 22:49:14 2024

@author: iliat
"""

# Get the charge for the food from the user
food_charge = float(input("Enter the charge for the food: $"))

# Calculate tip and sales tax
tip_percent = 18
tax_percent = 7

tip_amount = (tip_percent / 100) * food_charge
tax_amount = (tax_percent / 100) * food_charge

# Calculate total amount
total_amount = food_charge + tip_amount + tax_amount

# Display each amount and the total price
print(f"Food Charge: ${food_charge:.2f}")
print(f"Tip ({tip_percent}%): ${tip_amount:.2f}")
print(f"Sales Tax ({tax_percent}%): ${tax_amount:.2f}")
print(f"Total Price: ${total_amount:.2f}")
