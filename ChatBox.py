#import random
from email import message
import random
from random import randint
from unittest import FunctionTestCase

#names for randomised name function for pizza bot
names = ["Dennis","Marcus","Railey","Karlos","Jacob","Euriel","Cindy","Eilee","Tifa"]

def welcome():
    '''
    
    Purpose: To generate a random name from the list and print it out
    a welcome message 
    Parameters: None
    Returns: None
    '''
#make number represent a random generated integer
num = randint(0,8)
name = (names[num])
#print welcome message and print randomised name from ransomised name list
print("**** Welcome to Noels neat mousepads***")
print("*** My name is",name,"***")
print("***I will be here to help you order your neat mousepad***")
 
# Bugs
# Will only work for valid input "d" and "p"
# invalid input triggers else input but program doesnt ask for input again  

#Menu for pick up or

def pickup():
    print(" Is your order for pickup or delivery?")
    print(" For pickup please enter 1")
    print(" For delivery please enter 2")
    while True:
        try:
            delivery = int(input("Please enter a number"))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print("Pickup")
                    break
        
                elif  delivery == 2:
                    print("Delivery")
                    break

            else:
                print("The number must be 1 or 2")
        except ValueError:
            print("That is not a valid number")
            print("Please enter 1 or 2")


#Main function
def main():
    '''
    Purpose:to run all Functions 
    a welcome message
    Parameters: None
    Returns: None
    '''
    welcome()
    pickup()

main()

