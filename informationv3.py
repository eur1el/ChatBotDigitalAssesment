customer_details = {}

#Basic instructions
print("Please enter the pickup information")

#customer name
valid = False
while not valid:
    customer_details['name'] = input("Please enter your name")
    if customer_details['name'] != "":
        print(customer_details['name'])
        break
    else:
        print("Sorry this cannot be blank")


#Customer phone number
valid = False
while not valid:
    customer_details['name'] = input("Please enter your name")
    if customer_details['name'] != "":
        print(customer_details['name'])
        break
    else:
        print("Sorry this cannot be blank")