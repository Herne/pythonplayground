# define a function takes 2 arguments. Print.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # inside the function. print arg1 as number
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

print "We can just give the function numbers directly:"
# call the function, give it 2 arguments directly
cheese_and_crackers(20,30)
# below will cause problem, expecting number, not str
# cheese_and_crackers("Hello", "World")
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
# call the function with 2 variables, prior assigned
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
# call the function, arguments are math resutls, but still numbers
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
# combine varialbe and math, still numbers
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print "How many cheeses do you have?"
amount_of_cheese = int(raw_input("> "))
print "How many boxes of crackers do you have?"
amount_of_crackers= int(raw_input("> "))
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
