# my_tuple = ((1,2,3), (4,5,6), (7,8,9))
# print(my_tuple[0][0])
user_items_number = int(input("Input"))
user_prefered_items = []
market_stock = ["ice-cream", "Juice", "Apple"]
user_available_items = []

for i in range(user_items_number):
	item = input("Enter item name you want to buy:")
	user_prefered_items.append(item)

for item in user_prefered_items:
	if item in market_stock:
		user_available_items.append(item)

print(user_available_items)


