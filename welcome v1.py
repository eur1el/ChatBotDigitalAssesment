#import random
import random
from random import randint

#names for randomised name function for pizza bot
names = ["Dennis","Marcus","Railey","Karlos","Jacob","Euriel","Cindy","Eilee","Tifa"]

#make number represent a random generated integer
num = randint(0,9)

name = (names[num])

#print welcome message and print randomised name from ransomised name list
print("**** Welcome to Nathaniels neat mousepads***")
print("*** My name is",name,"***")
print("***I will be here to help you order your delicious Dream Pizza***")