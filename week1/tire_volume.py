import math
import os
from datetime import datetime

current_date_and_time = datetime.now()

w = float(input("Enter the width of the tire in mm (ex 205): "))
a = float(input("Enter the aspect ratio of the tire (ex 60): "))
d = float(input("Enter the diameter of the wheel in inches (ex 15): "))
v = 0
pi = math.pi

w2 = w**2
part1 = (w * a )+( d * 2540) 
part2 = (pi * w2 ) * a 
part3 = part1 * part2
v = part3 / 10000000000

print(f"The approximate volume is {v:.2f} liters")

# Exceeding the Requirements
buy = input("Would you like to buy tires with this dimmention? ")
buy = buy.upper()

if buy == "YES":
    phone = input("Tell us you phone number: ")
    print("We will be in touch!")
else:
    phone=""
    print("Ok, Thanks!")
# End of Exceeding the Requirements

file_name = "volumes.txt"
date = f"{current_date_and_time:%Y-%m-%d}"

if not os.path.exists(file_name):
    with open(file_name, "at") as file:
        pass
with open(file_name, "at") as file:
    if phone == "":
        print(f"{date}, {w}, {a}, {d}, {v:.2f}, '0'", file=file)
    else:
        print(f"{date}, {w}, {a}, {d}, {v:.2f}, '{phone}'", file=file)