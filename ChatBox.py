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

def valid_integer(low, high, question):
    while True:
        try:
            num = int(input(question))
            if num >= low and num <= high:
                return num
            else:
                print (f"Pleas enter a number between {low} and {high}")
        except ValueError:
            print ("That is not a valid number")
            print (f"Please enter a number between {low} and {high}")



def welcome():
    # make number represent a random generated integer
    # print welcome message 
    #print randomised name from ransomised name list
    #prints customer service message
    num = randint(0, 8)
    name = (names[num])
    print(" **** Welcome to Noels neat mousepads*** ")
    print("*** My name is", name, "***")
    print("***I will be here to help you order your neat mousepad***")


# Menu for pick up or delivery
def ordertype():
    del_pick = ""
    low = 1
    high = 2
    question = (f"Enter a number between {low} and {high}")
    print(" Is your order for pickup or delivery?")
    print(" For pickup please enter 1")
    print(" For delivery please enter 2")
    delivery = valid_integer(low,high, question)
    if delivery == 1:
        print("Click and Collect")
        del_pick = "Click and Collect"
        pickup_info()
    else:
        print("Delivery")
        delivery_info()
        del_pick = "Delivery"
    return del_pick
    

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

    question = ("Please enter your suburb")
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
    low = 1
    high = 15
    menu_low = 1
    menu_high = 13
    question = (f"Enter a number between {low} and {high}")
    print("How many costumes do you want to order?")
    num_costumes = valid_integer(low,high,question)
    #Choose costume from menu
    for item in range(num_costumes):
        while num_mousepads > 0:
            print("Please choose the mousepad you want by providing the number of the mousepad from the menu")
            question = (f"Enter a number between {low} and {high}")
            mousepads_ordered = valid_integer(menu_low, menu_high, question)
            mousepads_ordered = mousepads_ordered -1
            order_list.append(mousepad_prices[mousepads_ordered])
            order_cost.append(mousepad_prices[mousepads_ordered])
            print("{} ${:.2f}".format(mousepad_designs[mousepads_ordered],mousepad_prices[mousepads_ordered]))
            num_mousepads = num_mousepads -1


# Print order out - including
def print_order(del_pick):
    print ()
    total_cost = sum(order_cost)
    print ("Customer Details")
    if del_pick == "Click and Collect":
        print("Your order is for Click and Collect")
        print(f"{customer_details['name']} {customer_details['phone']}")
    elif del_pick == "delivery":
        print("Your order is for delivery a $9.00 delivery charge applies")
        print(f"{customer_details['name']} {customer_details['phone']} {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    print()
    #Function
    print("Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {}  Cost ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()
    if del_pick =="Delivery":
        if len(order_list) >= 5:
            print("Your order will be delivered for free")
        elif len(order_list) <= 5:
            print("There is an additional $9.00 delivery charge")
            total_cost = total_cost +9
        print("Order Cost Details")
        print(f"${total_cost:.2f}")
    if del_pick == "Click and Collect":
        print("Thank you for your order, we'll let you know when its ready")
    elif del_pick == "Delivery":
        print("Thank you for your order, it will be processed soon")

# Ability to cancel or proceed with order
def confirm_cancel():
    low = 1
    high = 2
    question = (f"Enter a number between {low} and {high}")
    print(" Please confirm your order")
    print(" To confirm please enter 1")
    print(" To cancel please enter 2")
    confirm = valid_integer(low, high, question)
    if confirm == 1:
        print ("Ordered Confirmed")
        print ("Your order has been sent to our manufactures")
        print("Your neat mousepad will be yours shortly")
        new_exit()
    elif confirm == 2:
        print("Your order has been cancelled")
        print("You can restart your order or exit the chat")
        new_exit()

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
    welcome()
    del_pick = ordertype()
    menu()
    order_mousepads()
    print_order(del_pick)
    confirm_cancel()
    menu()
    
main()

