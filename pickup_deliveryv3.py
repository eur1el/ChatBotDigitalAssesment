# Bugs
# Will only work for valid input "d" and "p"
# invalid input triggers else input but program doesnt ask for input again  

print(" Is your order for pickup or delivery?")

print(" For pickup please enter 1")
print(" For delivery please enter 2")

low = 1
high = 2

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




