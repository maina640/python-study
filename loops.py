fruits=['banana','mango','oranges','lemon','watermelon']
for fruit in fruits:
    print(fruit)

x=[1,2,3,4,5,6,7,8,9,10]
y=list(range(1,11))
print(y)

#create a list of numbers between 1-1000
#num(variable)=list(range(1,1000))
num=list(range(1,1000))
print(num)

#iterate through numbers from 20 to 100
for num in range (20,101):
    print(num)


#iterate through numbers from 20 to 100 and only display even numbers
numbers=list(range(20,101))
for i in numbers:
    if i%2==0:
        print(i)
