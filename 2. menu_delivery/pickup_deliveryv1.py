
print("Do you want your order delivered or are you picking it up")

print("For pickup please enter p")
print("For delivery please enter d")

delivery = input()

if delivery == "d":
    print(delivery)

elif delivery == "p":
    print("Pickup")
else:
    print("That was not a valid input")
