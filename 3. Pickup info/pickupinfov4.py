#Customers details dictionary
customers_details = {}


def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response != "":
            return response
        else:
            print("This cannot be blank")

#Basic Instuctions
question = ("Please enter your name")
customers_details['name'] = not_blank( question)
print(customers_details['name'])

question = ("Please enter your phone number  ")
customers_details['phone'] = not_blank(question  )
print(customers_details['phone'])

print (customers_details) 