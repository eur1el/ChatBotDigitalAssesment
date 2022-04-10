mousepad_designs = ['Wave Design- Small','Sakura Blossom Design - Small', 'Plain Blank Design Small','Wave Design- Medium','Sakura Blossom Design - ,Medium', 
'Plain Blank Design Medium', 'Wave Design- Large','Sakura Blossom Design - Large', 'Plain Blank Design Large',]

mousepad_prices = [12.50, 12.50, 12.50, 17.50, 17.50, 17.50, 24, 24, 24]

number_mousepads = 9

print ("How many pizzas would like to order?")
num_pizzas = int(input())

for count in range (number_mousepads):
    print(" {} {} ${:.2f}") .format(count+1,mousepad_designs[count],mousepad_prices[count])


