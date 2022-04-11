# Chat Box Program
# import random
from email import message
import random
from random import randint
from unittest import FunctionTestCase
import sys

# list of mousepad names
from multiprocessing.sharedctypes import Value


# names for randomised name function for pizza bot
names = ["Dennis", "Marcus", "Railey", "Karlos", "Jacob", "Euriel", "Cindy", "Eilee", "Tifa"]


# list of mousepad designs
mousepad_designs = ['Wave Design- Small', 'Sakura Blossom Design - Small', 'Plain Blank Design Small', 'Wave Design- Medium', 'Sakura Blossom Design - ,Medium', 'Plain Blank Design Medium', 'Wave Design- Large', 'Sakura Blossom Design - Large', 'Plain Blank Design Large', ]

# mousepad prices
mousepad_prices = [12.50, 12.50, 12.50, 17.50, 17.50, 17.50, 24, 24, 24]


# list to store ordered mousepads
order_list = []

# list to store mousepad prices
order_cost = []

# Customer details dictionary
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
# make number represent a random generated integer
num = randint(0, 8)
name = (names[num])

# print welcome message 
#print randomised name from ransomised name list
#prints customer service message
print(" **** Welcome to Noels neat mousepads*** ")
print("*** My name is", name, "***")
print("***I will be here to help you order your neat mousepad***")

# pickup information - phone and number
def pickup_info():
    question = ("Please enter your name")
    customer_details['name'] = not_blank(question)
    print(customer_details['name'])

    question = ("Please enter your phone number")
    customer_details['phone'] = not_blank(question)
    print(customer_details['phone'])
    print (customer_details)

    # delivery information - phone and number
def delivery_info():
    question = ("Please enter your name")
    customer_details['name'] = not_blank(question)
    print(customer_details['name'])

    question = ("Please enter your phone number")
    customer_details['phone'] = not_blank(question)
    print(customer_details['phone'])

    question = ("Please enter your house")
    customer_details['house'] = not_blank(question)
    print(customer_details['house'])

    question = ("Please enter your street number")
    customer_details['street'] = not_blank(question)
    print(customer_details['street'])

    question = ("Please enter your phone suburb")
    customer_details['suburb'] = not_blank(question)
    print(customer_details['suburb'])
    print (customer_details)


# mousepad menu
def menu():
    number_mousepads = 9
    for count in range(number_mousepads):
        print("{} {} ${:.2f}".format(count+1, mousepad_designs[count], mousepad_prices[count]))


# ask for total number of mousepads for order
def order_mousepads():
    num_mousepads = 0 
    count = 0
    while True:  # when number of mousepads = 0
        try:  # while number of mousepads = 0 run following code
            num_mousepads = int(input("How many mousepads do you want order>")) # ask user how many mousepads they want to order and save as an integer
            if num_mousepads >= 1 and num_mousepads <= 9: # if number of mousepads is more than 1 and less than 5
                break  # if number is between 1 and 5 continue with other code
            else:  # if number is not between 1 and 5 run following code
                print("Your order must be between 1 and 5") # if number is less than 1 and greater than 5 tell user to enter a number between 1 and 5
        except ValueError:  # If input is not an integer 
                print("That is not a valid number")  # print message to tell user that the input was not valid
                print("Please enter 1 or 5")  # print message to tell user to enter a number between 1 and 5
    # Choose pizza from menu
    for item in range(num_mousepads):
        while num_mousepads > 0:
            while True:
                try:
                    mousepads_ordered = int(input("Please choose your mousepad by entering the number from the menu"))
                    if mousepads_ordered >= 1 and mousepads_ordered <= 12:
                        break
                    else:
                        print("Your mousepad order must be between 1 and 9")
                except ValueError:
                            print("That is not a valid number")
                            print("Please enter a number between 1 and 12")
                            mousepads_ordered = mousepads_ordered -1
                            order_list.append(mousepad_prices[mousepads_ordered])
                            order_cost.append(mousepad_prices[mousepads_ordered])
                            print("{} ${:.2f}".format(mousepad_designs[mousepads_ordered],mousepad_prices[mousepads_ordered]))
                            num_mousepads = num_mousepads -1

    print(order_list)
    print(order_cost)


# Menu for pick up or delivery
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
                    del_pick = "pickup"
                    pickup_info()
                    break
                elif delivery == 2:
                    print("Delivery")
                    order_list.append("Delivery Charge")
                    order_cost.append(5)
                    delivery_info()
                    del_pick = "delivery"
                    break

            else:
                print("The number must be 1 or 2")
        except ValueError:
            print("That is not a valid number")
            print("Please enter 1 or 2")
        return del_pick

# list to store ordered mousepads
order_list = ['Wave Design- Small', 'Sakura blossom Design - Small', 'Plain Black Design - Small']


# list to store mousepad prices
order_cost = [12.50, 12.50, 12.50]


# Print order out - including
def print_order(del_pick):
    print ()
    total_cost = sum(order_cost)
    print ("Customer Details")
    if del_pick == "pickup":
        print("Your order is for pickup")
        print(f"{customer_details['name']} {customer_details['phone']}")
    elif del_pick == "delivery":
        print("Your order is for delivery a $9.00 delivery charge applies")
        total_cost = total_cost + 5
        print(f"{customer_details['name']} {customer_details['phone']} {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    print()
    print("Order Details")
    count = 0
    for order in order_list:
        print("Ordered: {}  Cost ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()
    print("Order Cost Details")
    print(f"${total_cost:.2f}")


# Ability to cancel or proceed with order
def confirm_cancel():
    print(" Please confirm your order")
    print(" To confirm please enter 1")
    print(" To cancel please enter 2")
    while True:
        try:
            confirm = int(input(""))
            if confirm >= 1 and confirm <= 2:
                if confirm == 1:
                    print ("Ordered Confirmed")
                    print ("Your order has been sent to our manufactures")
                    print("Your neat mousepad will be yours shortly")
                    break

            elif confirm == 2:
                print("Your order has been cancelled")
                print("You can restart your order or exit the chat")
                break

            else:
                print("The number must be 1 or 2")
        except ValueError:
            print("That is not a valid number")
            print("Please enter 1 or 2")


# Option for new order or to exit
def new_exit():
    print(" Do you want to create another or exit?")
    print(" To start another order enter 1")
    print(" To exit the BOT enter 2")
while True:
    try:
        confirm = int(input("Please enter a number"))
        if confirm >= 1 and confirm <= 2:
            if confirm == 1:
                print ("New Order")
                order_list.clear()
                order_cost.clear()
                customer_details.clear()
                break

        elif confirm == 2:
            print("Exit")
            order_list.clear()
            order_cost.clear()
            customer_details.clear()
            sys.exit()
            break

        else:
            print("The number must be 1 or 2")
    except ValueError:
        print("That is not a valid number")
        print("Please enter 1 or 2")


# Main function
def main():
    '''
    Purpose:to run all Functions
    a welcome message
    Parameters: None
    Returns: None
    '''
    welcome()
    pickup_info()
    delivery_info()
    menu()

