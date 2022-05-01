#list of pizza names
from multiprocessing.sharedctypes import Value


mousepad_designs = ['Wave Design- Small','Sakura Blossom Design - Small', 'Plain Blank Design Small','Wave Design- Medium','Sakura Blossom Design - ,Medium', 
'Plain Blank Design Medium', 'Wave Design- Large','Sakura Blossom Design - Large', 'Plain Blank Design Large',]

#list of pizza prices
mousepad_prices = [12.50, 12.50, 12.50, 17.50, 17.50, 17.50, 24, 24, 24]

#list to store ordered mousepads
order_list = []

#list to store mousepad prices
order_cost = []

#list to store order cost
number_mousepad = 9
def menu():
    number_mousepad = 9

count = 0
    
for count in range (number_mousepad):
    print(" {} {} ${:.2f}".format(count+1,mousepad_designs[count],mousepad_prices[count]))

menu()

#ask for total number of mousepads for order
num_mousepads = 0
while True:
    try:
        num_mousepads = int(input("How many mousepads do you want order? "))
        if num_mousepads >= 1 and num_mousepads <=15:
            break
        else:
            print("Your order must be between 1 and 15")
    except ValueError:
            print("That is not a valid number")
            print("Please enter 1 or 15")
           

#Choose mousepad from menu
print("Please choose your mousepads by entering the number from the menu")
for item in range(num_mousepads):
    while num_mousepads > 0:
        mousepads_ordered = int(input())
        order_list.append(mousepad_designs[mousepads_ordered])
        order_list.append(mousepad_designs[mousepads_ordered])
        num_mousepads = num_mousepads-1

print(order_list)




