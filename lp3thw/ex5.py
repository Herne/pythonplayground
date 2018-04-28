# constants
CM_PER_INCH = 2.54
POUND_PER_KILOGRAM = 2.20462234 
# variables
name = 'Herne Liu'
age = 35
height = 64 # inches
height_cm_round = round(height * CM_PER_INCH, 2) # cm
weight = 110 # lbs 
weight_kg_round = round(weight / POUND_PER_KILOGRAM, 2) # kg
eyes = 'Brown'
teeth = 'White'
hair = 'Black'


#print (f"Let's talk about {name}.")
print (f"Let's talk about {name}.")
print (f"She's {height} inches tall.")
print (f"She's {height_cm_round} centimeters tall.")
print (f"She's {weight} pounds heavy.")
print (f"She's {weight_kg_round} kilograms heavy.")
print ("Actually that's not too heavy.")
print (f"She's got {eyes} eyes and {hair} hair.")
print (f"Her teeth are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
total = age + height + weight
print (f"If I add {age}, {height}, and {weight} I get {total}.") 