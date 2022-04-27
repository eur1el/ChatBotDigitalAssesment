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
    
for count in range(number_mousepad) :
    print(" {} {} ${:.2f}".format(count+1,mousepad_designs[count],mousepad_prices[count]))


menu()


def order_mousepad():
    #ask for total number of mousepadsfor order
    num_mousepads = 0
    while True:
        try:
            num_mousepads = int(input("How many mousepads do you want order>"))
            if num_mousepads >= 1 and num_mousepads <= 5:
                break
            else:
                print("Your order must be between 1 and 5")
        except ValueError:
                print("That is not a valid number")
                print("Please enter 1 or 5")      
    #Choose pizza from menu
    
    for item in range(num_mousepads):
        while num_mousepads > 0:
            while True:
                try:
                    mousepad_ordered = int(input("Please choose your mousepad by entering the number from the menu"))
                    if mousepad_ordered >=1 and mousepad_ordered  <= 9:
                        break
                    else:
                        print("Your order must be between 1 and 9")
                except ValueError:
                    print ("That is not a valid number")
                    print("Please enter a number between 1 and 9")
                mousepad_ordered = mousepad_ordered -1
                order_list.append(mousepad_designs[mousepad_ordered])
                order_cost.append(mousepad_designs[mousepad_ordered])
                print(" {} {} ${:.2f}".format(mousepad_designs[mousepad_ordered],mousepad_prices[mousepad_ordered]))
                num_mousepads = num_mousepads-1

order_mousepad()

print(order_list)
print(order_cost)

