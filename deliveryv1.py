#Customers details dictionary
customers_details = {}


def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response != "":
            return response.title()
        else:
            print("This cannot be blank")

#Basic Instuctions
question = ("Please enter your name")
customers_details['name'] = not_blank( question)
print(customers_details['name'])

question = ("Please enter your phone number  ")
customers_details['phone'] = not_blank(question  )
print(customers_details['phone'])

question = ("Please enter your house")
customers_details['house'] = not_blank( question)
print(customers_details['house'])

question = ("Please enter your street number")
customers_details['street'] = not_blank(question  )
print(customers_details['street'])

question = ("Please enter your phone suburb")
customers_details['suburb'] = not_blank(question  )
print(customers_details['suburb'])



