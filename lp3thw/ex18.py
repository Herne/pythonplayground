# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2, arg3 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
    print(f"arg3: {arg3}")


# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")


# this takes no arguments
def print_none():
    print("I got nothin'.")


print_two("Herne", "Liu", "Hill")
print_two_again("Herne", "Hill")
print_one("Herne")
print_none()
