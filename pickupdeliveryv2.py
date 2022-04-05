#customer details dictionary
from unicodedata import name


customers_details ={}

#Basic Instructions
print("Please enter the pickup information")

#Customer name not found
valid = False
while not valid:
    customers_details['name'] = input("Please enter your name")
    if customers_details['name'] != "":
        break
    else:
        print("Sorry this cannot be blank")

#Customer phone number
valid = False
while not valid:
    phone = input("Please enter your phone number")
    if phone != "":
        print (phone)
        break
    
    else:
        print("Sorry this cannot be blank")
