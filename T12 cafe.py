#Created a list for the café menu and two dictionaries for stock amounts and price amounts
menu = ["coffee", "tea", "hot chocolate", "croissant"]

stock = {"coffee": 164, "tea": 159, "hot chocolate": 22, "croissant": 17}

price = {"coffee": 150, "tea": 135, "hot chocolate": 200, "croissant": 250}

#Calculates the total value of the various menu items, multiplying stock by price. 
#Prices start in pence and then divided by 100 to represent value in pounds. i.e. 274p / 100 = £2.74, finally formatted always to 2 decimal places.
coffee_total = (stock["coffee"] * price["coffee"])/100
coffee_total = "%.2f" % coffee_total
print(f"The total value of coffee at the cafe is £{coffee_total}")


tea_total = (stock["tea"] * price["tea"])/100
tea_total = "%.2f" % tea_total
print(f"The total value of tea at the cafe is £{tea_total}")


hot_chocolate_total = (stock["hot chocolate"] * price["hot chocolate"])/100
hot_chocolate_total = "%.2f" % hot_chocolate_total
print(f"The total value of hot chocolate at the cafe is £{hot_chocolate_total}")


croissant_total = (stock["croissant"] * price["croissant"])/100
croissant_total = "%.2f" % croissant_total
print(f"The total value of croissants at the cafe is £{croissant_total}")

#Iterate through all dictionary entries to calculate the total value of the stock.
total_stock = sum(stock[i] * price[i] for i in stock)/100
total_stock = "%.2f" % total_stock
print(f"The total value of all stock at the cafe is £{total_stock}")