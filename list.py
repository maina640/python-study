fruits=['mango','banana',100,30.5,False,True]
print(type(fruits))

#accessing elements inside a list
print(fruits[1])
print(fruits[-1])

#list methods= manipulate or modify data in a list
#Append=used to add elements at the end of a list
fruits.append("oranges")
print(fruits)

#insert= add items to a specific index
fruits.insert(1,1000)
print(fruits)

#remove=is used to remove the first occurrence of a specific element
num=[10,20,30,40,50,10,50]
num.remove(50)
print(num)

#pop=it removes items of a specific index
num.pop(0)
print(num)

#list slicing=used to extract a subset of datafrom a list
print(num[0:3])

#length= used to get lemgth of a list
print(len(num))

#check if element is inside a list
students=["maina","arnold","frank","vera","abdi"]
print("maina" in students)
print("kim" in students)

#concatenate list
list1=[1,2,3,4,5]
list2=[5,7,8,9,10]
list3=list1+list2
print(list3)
