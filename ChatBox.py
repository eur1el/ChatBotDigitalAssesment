# Chat Box Program
# import random
import sys
import random
from random import randint

#constants 
low = 1
high = 2
ph_low = 7
ph_high = 10

# list of mousepad names
from multiprocessing.sharedctypes import Value


# names for randomised name function for pizza bot
names = ["Dennis", "Marcus", "Railey", "Karlos", "Jacob", "Euriel", "Cindy", "Eilee", "Tifa"]


# list of mousepad designs
mousepad_designs = ['Wave Design- Small','Sakura Blossom Design - Small', 'Plain Blank Design - Small','Whiteout Design - Small','Wave Design- Medium','Sakura Blossom Design - Medium', 
'Plain Blank Design Medium','Whiteout Design - Medium', 'Wave Design- Large','Sakura Blossom Design - Large', 'Plain Blank Design Large','Whiteout design - Large']

# mousepad prices
mousepad_prices = [ 12.50, 12.50, 12.50, 12.50, 17.50, 17.50, 17.50,17.50, 24, 24, 24,24 ]

# list to store ordered mousepads
order_list = []
# list to store mousepad prices
order_cost = []

# Customer details dictionary
customer_details = {}


# validates inputs to check if they are blank
def not_blank(question): # define following program as not_blank
    valid = False # valid = false
    while not valid: # When valid is not false 
        response = input(question) # asks the user the question, then asks for users input
        if response != "":# if response is filled out correctly
            return response.title()# display response given
        else:#  if input is not given
            print("This cannot be blank")# tell user response cannot be blank

def check_string(question):# define code as check_string
    while True:# Create loop
        response = input(question)# response 
        x = response.isalpha()# x checks if input includes letters from the alphabet, isalpha checks if something is in the alphabet
        if x == False:# if input was not in the alphabet print following message
            print("Input must only contain letters")# Print invalid input message 
        else:# if input does include letters from the alphabet
            return response.title()# return input back to user
            

def valid_integer(low, high, question):# define following code as "valid_integer"
    while True:# Create loop
        try:# Run 
            num = int(input(question))# input given to question = number
            if num >= low and num <= high:# if number is between low and high 
                return num# Proceed with code as number given is valid
            else:# If number is not inputted 
                print (f"Please enter a number between {low} and {high}")# print message asking user to enter a valid number between "low" and "high"
        except ValueError:# If integer is below "low" or higher than "high" then run the following
            print ("That is not a valid number")# Print invalid number message
            print (f"Please enter a number between {low} and {high}")# Ask user to enter a valid number between "low" and "high"

            
def check_phone(question, ph_low, ph_high):# define following code as "check_phone"
    while True:# 
        try:#
            num = int(input(question))# asks user for a number/integer input
            test_num = num#
            count = 0# sets count as 0
            while test_num > 0:# When testnum is greater than 0
                test_num = test_num//10# If num is greater than 0 divide number by 10
                count = count + 1# count = 0 + 1
            if count >= ph_low and count <= ph_high:# if count is between low and high
                return str(num)#  return input
            else:# if number isnt correct
                print("NewZealand mobile numbers contain 7 to 10 digits")# Print message telling user to enter a number between 7 and 10 digits
        except ValueError:# If users input is not between 7u to 10 digits 
            print("Please enter a number ")# Print message asking user to enter a number

def welcome():# Define following code as "welcome"
    num = randint(0, 8)# choose a random integer between 0 and 8
    name = (names[num])# random integer chosen correlates to name from randomised name list
    print("Hello, Welcome to Noels Neat Mousepads")# Print welcome message
    print("My name is", name,"")# Print message using code "name"
    print("I will be here to help you order your neat mousepad")# Print Help message


# Menu for pick up or delivery
def ordertype():# define following code as "order_type"
    del_pick = ""# Delivery pick = input
    question = (f"Enter a number between {low} and {high} ")# Ask user to enter a number between low (1) and high(2)
    print(" Is your order for click and collect or would you like it delivered?")# Ask user if their order type is Click and Collect or delivered.
    print(" For click and collect please enter 1")# Tell user to enter 1 if they want their order to be Click and Collect
    print(" For delivery please enter 2")# Tell user to enter 2 if they want their order to be delivered
    delivery = valid_integer(low,high, question)# makes sure integer given is between "low"(1) and "high"(2)
    if delivery == 1:# If delivery integer = 1
        print("Click and Collect")#  Print Message "Click and Collect"
        del_pick = "Click and Collect"# delivery type =  Click and Collect
        pickup_info()# Print code called "pickup_info"
    else:# if pick up doesnt equal 1
        print("Delivery")# Print message "Delivery"
        delivery_info()# Print code called "delivery_info"
        del_pick = "Delivery"# delivery type = Delivery
    return del_pick# return input
    

# pickup information - phone and number
def pickup_info():# Define following code as "pickup_info"
    question = ("Please enter your name ")# Ask user to enter their name
    customer_details['name'] = check_string(question)# When user has entered their name use code "check_string" to see whether only letters are being inputed
    print(customer_details['name'])# Print customers input for name

    question = ("Please enter your phone number ")# Ask user to enter their phone number
    customer_details['phone'] = check_phone(question,ph_low,ph_high)# 
    print(customer_details['phone'])# Print customers input for phone number

    # delivery information - phone and number
def delivery_info():# Define following code as "delivery_info"
    question = ("Please enter your name ")# Ask user to enter their name
    customer_details['name'] = check_string(question)# When user has their name entered use code "check_string" to see whether only letters are being inputed
    print(customer_details['name'])# Print users name

    question = ("Please enter your phone number ")# Ask user to enter their phone number
    customer_details['phone'] = check_phone(question,ph_low,ph_high)# When user has entered their phone number use code "check phone" to see whether only integers are being inputed
    print(customer_details['phone'])# print users input for phone

    question = ("Please enter your house number ")# Ask user to enter their house
    customer_details['house'] = not_blank(question)# When user has entered their house use code "not blank" to make sure user does input their house and is not left blank
    print(customer_details['house'])# Print Customers house

    question = ("Please enter your street name ")# Ask user to enter their street
    customer_details['street'] = check_string(question)# When user has entered their street then uses code "check_string" to see whether user only inputted letters
    print(customer_details['street'])# # Print customers input for street

    question = ("Please enter your suburb ")# Ask user to enter their suburb
    customer_details['suburb'] = check_string(question)# When user has entered use code "check_string" to see whether only letters are being inputed
    print(customer_details['suburb'])# Print customers input for suburb 


# mousepad menu
def menu():# Define following code as "menu"
    number_mousepads = 12# number of mousepads is 12
    for count in range(number_mousepads):# when count is in range (15)
        print("{} {} ${:.2f}".format(count+1, mousepad_designs[count], mousepad_prices[count]))# prints mousepad designs names, listing them and providing their price


def order_mousepads():# defines following code as order_mousepad
    # ask for total number of mousepads for order
    num_mousepads = 0 # sets num_mousepads to 0
    count = 0# sets count to 0
    num_low = 1# sets num_low to 1
    num_high = 15# sets num_high to 15
    menu_low = 1# sets menu low to 1
    menu_high = 12# sets menu high to 12
    question = (f"Enter a number between {num_low} and {num_high} ")# asks user to enter a number between num_low (1) nad num_high (15)
    print("How many mousepads do you want to order?")# Print message asking user how many mousepads they want to order
    num_mousepads = valid_integer(num_low,num_high,question)# When user gives input, check input to see whether it is between 1 and 15
    #Choose mousepad from menu
    for item in range(num_mousepads):
        while num_mousepads > 0:# when num_mousepad is greater than 0
            print("Please choose your mousepad using the menu number")# Asks user to choose their mousepad by entering a number which correlates to the menu
            question = (f"Enter a number between {menu_low} and {menu_high} ")# asks user to enter a number between menu_low (1) and menu_high(12)
            mousepads_ordered = valid_integer(menu_low, menu_high, question)# makes sure integer inputted by user is between "menu_low"(1) and "menu_high"(15)
            mousepads_ordered = mousepads_ordered -1# makes sure correct mousepad ordered are printer
            order_list.append(mousepad_designs[mousepads_ordered])# links users integer to chosen mousepad 
            order_cost.append(mousepad_prices[mousepads_ordered])# links chosen mousepad to price
            print("{} ${:.2f}".format(mousepad_designs[mousepads_ordered],mousepad_prices[mousepads_ordered]))# prints mousepad designs and prices that user has ordered
            num_mousepads = num_mousepads -1# creates loop by taking 1 away when mousepad is ordered
            

# Print order out - including
def print_order(del_pick):# define following order as "print_order(del_pick)"
    print ()# Print Blank space
    total_cost = sum(order_cost)# total_cost equals the sum of 
    print ("Customer Details")# Print Customer details -
    if del_pick == "Click and Collect":# If delivery type equals click and collect
         print("Your Order is for Click and Collect")# Print message to user telling their order is ready
         print("You will recieve a message when order is ready for pickup")# Print text pickup message
         print(f"Customer Name: {customer_details['name']}"# Print Customer Name
              f"\nCustomer Phone: {customer_details['phone']}")# Print Customer Phone
    elif del_pick == "Delivery":# If ordertype = delivery
        print("Your order is selected for delivery")# Print message telling user their message is delivery type
        print(f"Customer Name: {customer_details['name']}"# Print Customer Name
              f"\nCustomer Phone: {customer_details['phone']}")# Print Customer Phone
    print()# Print Blank space


    #Function
    print("Order Details")# Print order detail message
    count = 0# Set count as 0
    for item in order_list:# for items within orderlist
        print("Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))# prints the mousepads that the user has ordered followed by its cost in $(dollars)
        count = count+1# Count is equal to 0 + 1
    print()# Print blank space
    if del_pick == "Delivery":# if delivery type is equal to delivery then run following code
        if len(order_list) >= 5:# if amount of mousepads ordered are greater than 5 
            print("Your order will be delivered for free due to ordering 5 or more products")# Print Free delivery message
        elif len(order_list) <= 5:# if mousepads ordered is less than 5 
            print("There is an additional $9.00 delivery charge")# Print delivery cost message
            total_cost = total_cost + 9# total cost for delivery is equal to sum of all products + 9 dollars for delivery
        print("Order Cost Details")# Print Heading for order cost details
        print(f"The total price of the order comes out to: ${total_cost:.2f}")# Print total cost of products with dollar signs
    if del_pick == "Click and Collect":# if pick up type is click and collect
        print("Order Cost Details")# Print Heading for order cost details
        print(f"The total price of the order comes out to: ${total_cost:.2f}")# Print total cost of products with dollar signs
        print()
        print("Thank you for your order, you'll receive a text when order is ready for pickup")# Print message thanking user for order
        print()
    elif del_pick == "Delivery":# if pick up type is delivery
        print("Thank you for your order, it will be processed soon")# Print message thanking user for order
        print()# print blank space


# Ability to cancel or proceed with order
def confirm_cancel():# define following code as "confirm_cancel"
    question = (f"Enter a number between {low} and {high} ")# ask user to enter a number between "low"(1) and high(2)
    print(" Please confirm your order")# Ask user to confirm their order
    print(" To confirm please enter 1")# Tell user to confirm by entering 1
    print(" To cancel please enter 2")# Tell user to cancel by entering 2
    confirm = valid_integer(low, high, question)# make sure integer is between "low"(1) and "high"(2)
    if confirm == 1:# if integer equals 1
        print()# print blank space
        print ("Ordered Confirmed")# Tell user their order has been confirmed
        print ("Your order has been sent to our manufactures")# tell user the order went through
        print("Your neat mousepad will be yours shortly")# Print message telling user their item will come shortly
        print()
        new_exit()# call/ reference code that is defined as "new_exit"
    elif confirm == 2:# if integer is 2
        print()# print blank space
        print("Your order has been cancelled")# Print message telling user their order has been cancelled
        print("You can restart your order or exit the chat")# Print message telling user to restart order or exit chat
        new_exit()# call/ reference code that is defined as "new_exit"



# Option for new order or to exit
def new_exit():#define following code as new_exit
    question = (f"Enter a number between {low} and {high} ")# asks user to enter a number between "low"(1) and "high"(2)
    print ("Do you want to start another Order or Exit?")# Print message asking user if they want another order
    print ("To start another order enter 1")# Print order enter message
    print ("To exit the BOT enter 2")# Print bot exit message
    confirm = valid_integer(low,high, question)# check if integer given is between "low" (1) and "high"(2)
    if confirm == 1:# if integer = 1
        print ("New Order")# Prints New order message
        order_list.clear()# clear inputs and information relating to order_list
        order_cost.clear()# clear inputs and information relating to order_cost
        customer_details.clear()# clear inputs and information relating to customer_details
        main()# Calls / References code "main" to run 

    elif confirm == 2:# if integer = 2
        print()
        print("Thank you for visiting Noels Neat Mousepads")# print thank you message
        order_list.clear()# clear inputs and information relating to order_list
        order_cost.clear()# clear inputs and information relating to order_cost
        customer_details.clear()# clear inputs and information relating to customer_details
        sys.exit()# exit system


# Main function
def main():# defines following code as main
    welcome()# references code called "welcome" and runs it
    del_pick = ordertype()# references code called "del_pick" and runs it
    menu()# references code called "menu" and runs it
    order_mousepads()# references code called "order_mousepads" and runs it
    print_order(del_pick)# references code called "del_pick" and runs it
    confirm_cancel()# references code called "confirm_cancel" and runs it
    
main()# references code called "main" and runs it

