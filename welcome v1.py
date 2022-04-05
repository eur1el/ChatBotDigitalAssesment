#import random
import random
from random import randint

#creates list of names for randomised name function for mousepad chatbox
names = ["Dennis","Marcus","Railey","Karlos","Jacob","Euriel","Cindy","Eilee","Tifa"]

#make number represent a random generated integer
num = randint(0,9)

name = (names[num])

#print welcome message 
#print message using "name" for a randomised name for chatbox customer service name
#prints help order message
print("**** Welcome to  Noels Neat Mousepads***")
print("*** My name is",name,"***")
print("***I will be here to help you order your neat mousepads***")