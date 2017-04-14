# import argument variables function from module sys
# from sys import argv
# unpacking the argv into 2 variables
# script, filename = argv
# open the file will return a file object, assign this file object to variable txt
# txt = open(filename)
# print the name of the file
# print "Here's your file %r:" % filename
# read from the file object, and print its content out
# print txt.read()
# prompt
print "Type a filename:"
#ask user for another file 
file_again = raw_input("> ")
# open the file and assign the new file object to another variable
txt_again = open(file_again)
# read from the new file, and print its content out
print txt_again.read()
# close the file when I'm done with it
txt_again.close()
