#list of mousepad names
mousepad_designs = ['Wave Design- Small','Sakura Blossom Design - Small', 'Plain Blank Design - Small','Whiteout Design - Small','Wave Design- Medium','Sakura Blossom Design - Medium', 
'Plain Blank Design Medium','Whiteout Design - Medium' 'Wave Design- Large','Sakura Blossom Design - Large', 'Plain Blank Design Large','Whiteout design - Large']

#list of mousepad prices
mousepad_prices = [ 12.50, 12.50, 12.50, 12.50, 17.50, 17.50, 17.50,17.50, 24, 24, 24,24 ]

#list to store ordered mousepads
order_list = []

#list to store mousepad prices
order_cost = []

#list to store order cost
number_mousepad = 12
def menu():
    number_mousepad = 12
    
for count in range(number_mousepad) :
    print(" {} {} ${:.2f}".format(count+1,mousepad_designs[count],mousepad_prices[count]))


menu()


def order_mousepad():
    #ask for total number of mousepadsfor order
    num_mousepads = 0
    while True:
        try:
            num_mousepads = int(input("How many mousepads do you want order? "))
            if num_mousepads >= 1 and num_mousepads <= 9:
                break
            else:
                print("Your order must be between 1 and 15")
        except ValueError:
            print ("That is not a valid number")
            print ("Please enter a number between 1 and 15")
    # Choose costume from menu
    for item in range(num_mousepads):
        while num_mousepads > 0:
            while True:  
                try:
                    mousepad_ordered = int(input("Please choose the mousepad you would like to order by entering the number of the mousepad from the menu "))
                    if mousepad_ordered>= 1 and mousepad_ordered <= 9:
                        break
                    else:
                        print("Your mousepad order must be between 1 and 9")
                except ValueError:
                    print ("That is not a valid number")
                    print ("Please enter a number between 1 and 9")
            mousepad_ordered = mousepad_ordered -1
            order_list.append(mousepad_designs[mousepad_ordered])
            order_cost.append(mousepad_prices[mousepad_ordered])
            print("{} ${:.2f}"  .format(mousepad_designs[mousepad_ordered],mousepad_prices[mousepad_ordered]))
            num_mousepads = num_mousepads -1
order_mousepad()



