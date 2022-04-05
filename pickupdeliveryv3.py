#Customers details dictionary
customers_details = {}


#Basic Instuctions
print("Please enter the pickup information")

#Customer name not found
valid = False
while not valid:
    customers_details['name'] = input("Please enter your name")
    if customers_details['name'] != "":
        print (customers_details['name'])
        break
    else:
        print("Sorry this cannot be blank")



#Customer phone number not blank
valid = False
while not valid:
    customers_details['phone'] = input("Please enter your phone number")
    if customers_details['phone'] != "":
        print(customers_details['phone'])
        break
    else:
        print("Sorry this cannot be blank")

print (customers_details) 