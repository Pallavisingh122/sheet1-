Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import math
x, y = 0, 0
while True:
    
    step = input("Type in UP/DOWN/LEFT/RIGHT #step number: ")

    
Type in UP/DOWN/LEFT/RIGHT #step number: UP
Type in UP/DOWN/LEFT/RIGHT #step number: DOWN
Type in UP/DOWN/LEFT/RIGHT #step number: LEFT
Type in UP/DOWN/LEFT/RIGHT #step number: RIGHT
Type in UP/DOWN/LEFT/RIGHT #step number: 
Type in UP/DOWN/LEFT/RIGHT #step number:  if step == "":
        break
    else:
        step = step.split(" ")

        if step[0] == "UP":
            y = y + int(step[1])
        elif step[0] == "DOWN":
            y = y - int(step[1])
        elif step[0] == "LEFT":
            x = x - int(step[1])
        elif step[0] == "RIGHT":
            x = x + int(step[1])

c = math.sqrt(x**2 + y**2)

print("Distance:", c)