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

#list slicing=used to extract a subset of data from a list
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

 
#trainees = ["John", [2, ["James","Mary"]]]
#1. Display 2 from the list.
#2. Output James  from the list.
#3. Using a method add 56 at the end of the list.
#4. Using a method add the name Mike between James and Mary
#5. Change the value of 2 to 8
#6. Remove John and Mary from the list.
#7. Using a function, determine the length of the list

#1. Display 2 from the list.
trainees=["john",[2,["james","mary"]]]
print(trainees[1])
 
#2. Output James  from the list.
trainees=["john",[2,["james","mary"]]]

#3. Using a method add 56 at the end of the list.
trainees=["john",[2,["james","mary"]]]
trainees.append("56")
print(trainees)

#4. Using a method add the name Mike between James and Mary
trainees=["john",[2,["james","mary"]]]
print(trainees[1])
trainees1=[2,["james","mary"]]
print(trainees1[1])
trainees2=["james","mary"]
f_trainee="james"
l_trainee="mary"
full_list=f_trainee+" "+"mike"+" "+l_trainee
print(full_list)

#5. Change the value of 2 to 8
trainees=["john",[2,["james","mary"]]]
trainees=["john",[2,["james","mary"]]]
print(trainees[1])
trainees1=[2,["james","mary"]]







