def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b


def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b


def multiply(a, b):
    print(f"MULTIPLY {a} * {b}")
    return a * b


def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


#
# print("Let's do some math with just functions!")
#
# age = add(30, 5)
# height = subtract(78, 4)
# weight = multiply(90, 2)
# iq = divide(100, 2)
#
# print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")
#
# # A puzzle for the extra credit, type it in anyway
# print("Herne is a puzzle.")
#
# what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
#
# print("That becomes: ", what, "Can you do it by hand?")


on = True

while on:
    print("""
=========================
Simple Calculator
=========================
1 - ADD
2 - SUBTRACT
3 - MULTIPLY
4 - DIVIDE
=========================
0 - QUIT
=========================
""")
    num_1 = float(input("First Number: "))
    num_2 = float(input("Second Number: "))
    method = int(input("Operation Method: "))
    if method == 1:
        print(add(num_1, num_2))
    elif method == 2:
        print(subtract(num_1, num_2))
    elif method == 3:
        print(multiply(num_1, num_2))
    elif method == 4:
        print(divide(num_1, num_2))
    elif method == 0:
        on = False
        print("Good Bye!")
    else:
        print("Not Supported.")
