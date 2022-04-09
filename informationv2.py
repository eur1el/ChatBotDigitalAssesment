#customer details dictionary
customer_details = {}


#prints information request message
print("Please enter your information")

#asks for users name and saves as an input under "name"
valid = False
while not valid:
    customer_details['name'] = input("Please enter your name")
    if customer_details['name'] != "":
        print (customer_details['name']
        break
    else:
        print("Sorry this cannot be blank")

#asks for users phone number an saves as input under "phone"
valid = False
while not valid:
    customer_details['name'] = input("Please enter your phone number")
    if customer_details['phone'] != "":
        print (customer_details['phone']
        break
    else:
        print("Sorry this number cannot be blank")



#prints users input for "name"
#prints users input for "phone"
print(name)
print(phone)