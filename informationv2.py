
#prints information request message
print("Please enter your information")

#asks for users name and saves as an input under "name"
valid = False
while not valid:
    name = input("Please enter your name")
    if name != "":
        print(name)
        break
    else:
        print("Sorry this number cannot be blank")

#asks for users phone number an saves as input under "phone"
valid= False
while not valid:
    phone = input("Please enter your phone number")
    if phone != "":
        print(phone)
        break
    else:
        print("Sorry this cannot be blank")


#prints users input for "name"
#prints users input for "phone"
print(name)
print(phone)