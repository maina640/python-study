#Write a program that displays a numbers 1 to 50 inside a list.
##num(variable)=list(range(1,51))

num=list(range(1,51))
print(num)

#From 1 above display the ones divisible by 7 or 5 inside a list.
#divisibles=[]
#for f in num:
#    if f%7==0 or f%5==0:
#        f.append(f)
#print(divisibles)


#Find sum and average of values in the range between 10 to 40.
num1=list(range(10,41))
sum=0

#Put in a list the first 10 odd numbers between 10 to 50.
numbers=list(range(10,51))
odd_numbers=[]
for i in numbers:
    if i%2!=0:
        odd_numbers.append(i)
print(odd_numbers[0:11])
odd_numbers1=[]
count=0
for x in num:
    if x%2!=0:
        odd_numbers1.append(x)
        count+=1
        if count==10:
            break

print(odd_numbers1)

#write a program that takes a number as input and prints its
#multiplication table up to 10 using a for loop
quantity=int(input('enter quantity:'))
for j in range(0,11):
    mult=quantity*i
    print(f'{quantity} *  {j}={mult}')
#write a program that counts and prints the number of even numbers between 1 
#and 50 using a for loop
count=0
for k in range(1,51):
    if k%2==0:
        count+=1

print(count)

#ls1 = [ (“Jay”, 20), (“Mo”, 30), (“Mya”, 32) ]
#Display the total quantity of the 3 above.
lsl=[('jay',20),('Mo', 30), ('Mya', 32),('lsl',100)]
total_quantity=0
for m in lsl:
    stock=1[1]
    total_quantity+=stock
print(total_quantity)


