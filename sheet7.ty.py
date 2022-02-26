Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print("Original set elements:")
Original set elements:
print(color_list_1)
{'White', 'Red', 'Black'}
print(color_list_2)
{'Red', 'Green'}
print("\nDifference of color_list_1 and color_list_2:")

Difference of color_list_1 and color_list_2:
print(color_list_1.difference(color_list_2))
{'White', 'Black'}
print("\nDifference of color_list_2 and color_list_1:")

Difference of color_list_2 and color_list_1:
print(color_list_2.difference(color_list_1))
{'Green'}
