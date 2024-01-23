# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 22:49:57 2024

@author: iliat
"""

def calculate_alarm_time(current_time, wait_hours):
    # Calculate the alarm time
    alarm_time = (current_time + wait_hours) % 24
    return alarm_time

# Get current time and wait hours from the user
current_time = int(input("Enter the current time (0-23 hours): "))
wait_hours = int(input("Enter the number of hours to wait for the alarm: "))

# Calculate and display the alarm time
alarm_time = calculate_alarm_time(current_time, wait_hours)
print(f"The alarm will go off at {alarm_time:02d}:00 hours.")
