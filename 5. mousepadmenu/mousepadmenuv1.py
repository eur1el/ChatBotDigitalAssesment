mousepad_designs = ['Wave Design- Small','Sakura Blossom Design - Small', 'Plain Blank Design Small','Wave Design- Medium','Sakura Blossom Design - Medium', 
'Plain Blank Design Medium', 'Wave Design- Large','Sakura Blossom Design - Large', 'Plain Blank Design Large',]

mousepad_prices = [12.50, 12.50, 12.50, 17.50, 17.50, 17.50, 24, 24, 24]

number_mousepads = 9

print ("How many mousepads you would like to order?")
number_mousepads = int(input())

for count in range (number_mousepads):
    print(count,mousepad_designs[count],mousepad_prices[count])

