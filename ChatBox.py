#Chat Box Program
#9/04/22
#Bugs - Phone number allows letters
#     - Name input allows number

#import random
from email import message
import random
from random import randint
from unittest import FunctionTestCase

#names for randomised name function for pizza bot
names = ["Dennis","Marcus","Railey","Karlos","Jacob","Euriel","Cindy","Eilee","Tifa"]

#list of mousepad designs
mousepad_designs = ['Wave Design- Small','Sakura Blossom Design - Small', 'Plain Blank Design Small','Wave Design- Medium','Sakura Blossom Design - ,Medium', 
'Plain Blank Design Medium', 'Wave Design- Large','Sakura Blossom Design - Large', 'Plain Blank Design Large',]

#mousepad prices
mousepad_prices = [12.50, 12.50, 12.50, 17.50, 17.50, 17.50, 24, 24, 24]

#Customer details dictionary
customer_details = {}


# validates inputs to check if they are blank
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response != "":
            return response.title()
        else:
            print("This cannot be blank")


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
 

#Menu for pick up or delivery
def ordertype():
    del_pick = "" 
    print(" Is your order for pickup or delivery?")
    print(" For pickup please enter 1")
    print(" For delivery please enter 2")
    while True:
        try:
            delivery = int(input("Please enter a number"))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print("Pickup")
                    pickup_info()
                    del_pick = "delivery"
                    break
                elif  delivery == 2:
                    print("Delivery")
                    delivery_info()
                    del_pick = "delivery"
                    break

            else:
                print("The number must be 1 or 2")
        except ValueError:
            print("That is not a valid number")
            print("Please enter 1 or 2")
        return del_pick


#pickup information - phone and number
def pickup_info():
    question = ("Please enter your name")
    customer_details['name'] = not_blank( question)
    print(customer_details['name'])

    question = ("Please enter your phone number  ")
    customer_details['phone'] = not_blank(question  )
    print(customer_details['phone'])
    print (customer_details)



#delivery information - phone and number

def delivery_info():
    question = ("Please enter your name")
    customer_details['name'] = not_blank( question)
    print(customer_details['name'])

    question = ("Please enter your phone number  ")
    customer_details['phone'] = not_blank(question  )
    print(customer_details['phone'])

    question = ("Please enter your house")
    customer_details['house'] = not_blank( question)
    print(customer_details['house'])

    question = ("Please enter your street number")
    customer_details['street'] = not_blank(question  )
    print(customer_details['street'])

    question = ("Please enter your phone suburb")
    customer_details['suburb'] = not_blank(question  )
    print(customer_details['suburb'])
    print (customer_details)



#mousepad menu
mousepad_designs = ['Wave Design- Small','Sakura Blossom Design - Small', 'Plain Blank Design Small','Wave Design- Medium','Sakura Blossom Design - ,Medium', 
'Plain Blank Design Medium', 'Wave Design- Large','Sakura Blossom Design - Large', 'Plain Blank Design Large',]

mousepad_prices = [12.50, 12.50, 12.50, 17.50, 17.50, 17.50, 24, 24, 24]

number_mousepads = 9

print ("How many mousepads would like to order?")
num_pizzas = int(input())

for count in range (number_mousepads):
    print(" {} {} ${:.2f}") .format(count+1,mousepad_designs[count],mousepad_prices[count])

#list to store ordered mousepads
order_list=['Wave Design- Small','Sakura blossom Design - Small','Plain Black Design - Small']
#list to store mousepad prices
order_cost = [12.50, 12.50, 12.50]

#Print order out - including 
def print_order(del_pick):
    print ()
    total_cost = sum(order_cost)
    print ("Customer Details")
    if del_pick == "pickup":
        print("Your order is for pickup")
        print(f"{customer_details['name']} {customer_details['phone']}")
    elif del_pick == "delivery":
        print("Your order is for delivery")
        print(f"{customer_details['name']} {customer_details['phone']} {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    print()
    print("Order Details")
    count = 0
    for order in order_list:
        print("Ordered: {}  Cost ${:.2f}".format(item,order_cost[count]))
        count = count+1
    print()
    print("Order Cost Details")
    print(f"${total_cost:.2f}")

print_order()



#Main function
def main():
    '''
    Purpose:to run all Functions 
    a welcome message
    Parameters: None
    Returns: None
    '''
    welcome()
    del_pick = ordertype()
    print(del_pick)
    mousepad_designs()
    ordertype()
    print_order()
    

main()

