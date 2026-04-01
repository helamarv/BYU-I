# how many items fit in the boxes?
import math

items = int(input("Enter the number of items: "))
boxes = int(input("Enter the number of boxes: "))

fit = items/boxes
fit = math.ceil(fit)

print(f"For {items} items, packing {boxes} items in each box, you will need {fit} boxes.")