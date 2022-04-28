#list to store ordered mousepads
order_list=['Wave Design- Small','Sakura blossom Design - Small','Plain Black Design - Small',]

#list to store mousepad prices
order_cost = [12.50, 12.50, 12.50]

count = 0
for item in order_list:
    print("Ordered: {} Cost ${:.2f}".format(item,order_cost[count]))
    count = count+1