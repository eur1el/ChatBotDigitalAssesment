#list to store ordered mousepads
order_list=['Wave Design- Small','Sakura blossom Design - Small','Plain Black Design - Small',]

#list to store mousepad prices
order_cost = [12.50, 12.50, 12.50]

count = 0
for order in order_list:
    print("Ordered: {} Cost ${:.2f}".format(item,order))
    count = count+1