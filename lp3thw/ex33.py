def print_numbers(count):
    i = 0
    numbers = []

    while i < count:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += 2
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    return numbers


# def print_numbers(count):
#     i = 0
#     numbers = []
#
#     for i in range(0, count):
#         print(f"At the top i is {i}")
#         numbers.append(i)
#
#         # i += 1
#         print("Numbers now: ", numbers)
#         print(f"At the bottom i is {i}")
#     return numbers


user_numbers = print_numbers(int(input('Count: ')))
print("The numbers: ")

for num in user_numbers:
    print(num)
