types_of_people = 10  # number
x = f"There are {types_of_people} types of people."  # f-string

binary = "binary"  # string
do_not = "don't"  # string
y = f"Those who know {binary} and those who {do_not}."  # f-string

print(x)  # print f-string
print(y)  # print f-string

print(f"I said: {x}")  # capsule f-string in f-string
print(f"I also said: '{y}'")  # capsule f-string in f-string; single-quote in double-quote

hilarious = False  # boolean
joke_evaluation = "Isn't that joke so funny?! {}"  # {} is placeholder

print(joke_evaluation.format(hilarious))  # .format() replaces {} in string with real value

w = "This is the left side of..."  # string
e = "a string with a right side."  # string

print(w + e)  # string concatenation
