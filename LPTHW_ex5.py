name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
inch_to_cm_multiplier = 2.54
lbs_to_kg_multiplier = 0.4535924
height_cm = height * inch_to_cm_multiplier
weight_kg = weight * lbs_to_kg_multiplier

print "Let's talk about %s." % name
print "He's %d inches (%d cm) tall." % (height, height_cm)
print "He's %d poinds (%.2f kg) heavy." % (weight, weight_kg)
print "He's %f kg heavy." % round(weight_kg, 2)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(eyes, hair)
print "His teeth are usually %s depending on the coffee." %teeth

# this line is trichy, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
