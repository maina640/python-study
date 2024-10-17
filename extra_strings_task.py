fname="maina"
lname="njane"
full_name=fname+(" ")+lname
print(full_name)

#given PYTHON print the first and last characters
name="PYTHON"
print(name[0:6])

#string phrase is "Learning python is fun!" use slicing to extract python
sentence="Learning python is fun!"
print(sentence[9:15])

#string text is "reverse this", print the reversed version
text="reverse this"
print(text[::-1])

#string text is "Hello World" replace "world" with "python"
string="Hello World"
string=string.replace('World','python')
print(string)

#take "Python programming" and print in upper and lower cases
take="python programming"
print(take.upper())
print(take.lower())

#count how many times letter 's' has appeared in "This is a simple sentence"
sentence1="This is a simple sentence"
print(sentence1.count('s'))

#checking the string quote="The best way to predict the future is to create it"
#substring "future"
quote="The best way to predict the future is to create it"
print(quote.count('future'))

#"Data science" print the string length
statement="data science"
print(len(statement))

#remove whitespace in "   John Doe  "
character="   John Doe  "
print(character.strip())