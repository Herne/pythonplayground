# constants
CM_PER_INCH = 2.54
POUND_PER_KILOGRAM = 2.20462234
# variables
my_name = 'Herne Liu'
my_age = 35
my_height = 64  # inches
height_cm_round = round(my_height * CM_PER_INCH, 2)  # cm
my_weight = 110  # lbs
weight_kg_round = round(my_weight / POUND_PER_KILOGRAM, 2)  # kg
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

# print (f"Let's talk about {name}.")
print(f"Let's talk about {my_name}.")
print(f"She's {my_height} inches tall.")
print(f"She's {height_cm_round} centimeters tall.")
print(f"She's {my_weight} pounds heavy.")
print(f"She's {weight_kg_round} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"She's got {my_eyes} eyes and {my_hair} hair.")
print(f"Her teeth are usually {my_teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

my_age = input("How old are you?\n")
print(f"I'm {my_age} years old.")
