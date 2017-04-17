def count_numbers(max, increment):

    i = 0
    numbers = []

    while i < max_i:
        print "At the top i is %d" % i
        numbers.append(i)

        i += increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    return numbers

max_i = int(raw_input("Max: "))
increment_i = int(raw_input("increment: "))
numbers = count_numbers(max_i, increment_i)

print "The numbers: "

for num in numbers:
    print num
