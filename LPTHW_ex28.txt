print True and True #=> True
print False and True #=> False
print 1 == 1 and 2 == 1 #=> True and False #=> False
print "test" == "test" #=> True
print 1 == 1 or 2 != 1 #=> True or True #=> True
print True and 1 == 1 #=> True and True #=> True
print False and 0 != 0 #=> False and False #=> False
print True or 1 == 1 #=> True or True #=> True
print "test" == "testing" #=> False
print 1 != 0 and 2 == 1 #=> True and False #=> False
print "test" != "testing" #=> True
print "test" == 1 #=> False
print not (True and False) #=> not (False) #=> True
print not (1 == 1 and 0!= 1) #=> not (True and True) #=> False
print not (10 == 1 or 1000 == 1000) #=> not (False or True) #=> False
print not (1 != 10 or 3 == 4) #=> not (True or False) #=> False
print not ("testing" == "testing" and "Zed" == "Cool Guy") #=> not (True and False) #=> True
print 1 == 1 and not ("testing" == 1 or 1 == 0) #=> True and not (False or False) #=> True
print "chunky" == "bacon" and not (3 == 4 or 3 == 3) #=> False and False #=> False
print 3 == 3 and not ("testing" == "testing" or "Python" == "Fun") #=> False
