from sys import argv

script, user_name, role_class = argv
prompt = '>>> '

print "Hi %s the %s, I'm the %s script." % (user_name, role_class, script)
print "I'd like to ask you a few questions."
print "Do you like me %s the %s?" % (user_name, role_class)
likes = raw_input (prompt)


print "Where do you live %s?" % user_name
lives = raw_input (prompt)

print "What kind of computer do you have %s?" % user_name
computer = raw_input (prompt)

print '''
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
''' % (likes, lives, computer)
