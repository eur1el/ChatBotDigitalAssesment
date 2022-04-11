#list to store ordered mousepads
order_list=['Wave Design- Small','Sakura blossom Design - Small','Plain Black Design - Small']

#list to store mousepad prices
order_cost = [12.50, 12.50, 12.50]

cust_details = {'name':'Euriel','phone':'0212121213','house':'45','street':'Daniel','subrb':'Mangere'}


print(f"{cust_details['name']} {cust_details['phone']} {cust_details['house']} {cust_details['street']} {cust_details['suburb']}")

count = 0
for item in order_list:
    print("Ordered: {} Cost ${:.2f}"  .format(item, order_cost[count]))
    count = count+1