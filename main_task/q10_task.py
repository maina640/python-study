#Write a program that calculates the total stock in a company from the array/list below if we know that the
#stock is the last digit in every array/list.
#prods = [[‘omo’,’30kshs’,’300’], [‘milk’,’50kshs’,’200’],[‘bread’,’45kshs’,’359’], [‘coffee’,’5kshs’,’79’]]
products = [['omo', '30kshs', '300'], ['milk', '50kshs', '200'], ['bread', '45kshs', '359'], ['coffee', '5kshs', '79']]
total_stock = 0

for product in products:
  stock = int(product[-1][-1])  # Extract the last digit of the last element
  total_stock += stock

print(f"Total stock: {total_stock}")
