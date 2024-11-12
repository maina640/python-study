# a concise way to create a new list from another 
# create a list of even_numbers from nnumbers between 20 and 100
even_numbers=[i for i in range (20,101) if i%2==0]
for i in range (20,101):
       if i%2==0:
           even_numbers.append(i)
print(even_numbers)