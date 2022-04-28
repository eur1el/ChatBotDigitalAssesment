def confirm_cancel():
    print ("Please confirm your order")
    print ("To confirm please enter 1")
    print ("To cancel please enter 2")
    while True:
        try:
            confirm = int(input("Please enter a number "))
            if confirm >= 1 and confirm <= 2:
                if confirm == 1:
                    print ("Your order has been confirmed")
                    print ("Your order has been sent to our warehouse")
                    print ("Your mousepad will be with you within 1-2 weeks working days")
                    break
                elif confirm == 2:
                    print ("Your Order has been Cancelled")
                    print ("You can either restart or exit the chat bot")
                    break
            else:
                print ("The number must be 1 or 2")
        except ValueError:
            print ("That is not a valid number")
            print ("Please enter 1 or 2") 

confirm_cancel()