# Bugs
# Will only work for valid input "d" and "p"
# invalid input triggers else input but program doesnt ask for input again  

print("Do you want your order delivered or are you picking it up?")

print(" For pickup enter p")
print(" For delivery enter d")

delivery = input()

if delivery == "d":
    print("Delivery")

elif  delivery == "p":
    print("Pickup")

else:
    print ("That was not a valid input")