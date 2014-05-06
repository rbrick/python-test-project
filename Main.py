import os
import BrickUtils


name = raw_input("What is your name? ")
print "You said your name is " + name

answer = raw_input("Is this correct? ")
text = name
path = "/home/ryan/PythonTestFolder/test.txt"
if answer is 'y': 
   print "Your name is " + name
   if BrickUtils.doesPathExist(path) is False:
	   open("test.txt",'w').write(text)
   else:
	   open("test.txt",'a').write("," + text)
while answer is 'n':
    print "Y u lie man, lying ain't cool"   
    answer = None
    name = raw_input("What is your name? ")
    answer = raw_input("Is this correct? ")
