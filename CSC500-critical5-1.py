# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 00:52:53 2024

@author: iliat
"""
def calculate_average_rainfall():
    total_years = int(input("Enter the number of years: "))
    total_rainfall = 0.0

    for year in range(1, total_years + 1):
        for month in range(1, 13):
            monthly_rainfall = float(input(f"Enter the rainfall (in inches) for year {year}, month {month}: "))
            total_rainfall += monthly_rainfall

    total_months = total_years * 12
    average_rainfall = total_rainfall / total_months

    print(f"\nNumber of months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall} inches")
    print(f"Average rainfall per month: {average_rainfall:.2f} inches")

calculate_average_rainfall()
