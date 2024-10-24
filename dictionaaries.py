person={
    'name':'maina',
    'age':'23',
    'gender':'male',
    'location':['kiambu',518,'thika'],
    'address':{
        'street':'muthaiga',
        'city':'nairobi',
        'country':'kenya'
    }
}
print(type(person))
print(person['name'])

#age
print(person['age'])

#gender
print(person['gender'])

#diaplsy 'thika'
print(person['location'][-1])

#display 'city'
print(person['address']['city'])

#'street'
print(person['address']['street'])

#modify(update)
person['age']=40
print(person)

person['location']='juja'
print(person)

#add new key and a value
person['occupation']='doctor'
print(person)

#dictionaries methods
print(person.keys())

#values
print(person.values())

#items
print(person.items())

#pop
person.pop('occupation')
print(person)