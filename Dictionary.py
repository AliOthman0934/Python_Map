# Dictionary in python

# Dict items are enclosed in curly braces
# Dict items are contains key : value

user = {
    "name" : "Ali",
    "age" : 23
}

# Dict key need to be immutable (num,str,tuple) list not allowed

#user2= {
#    "name" : "osman",
#    ["age","skils"] : 
#} error 

# Dict value can have any data types
# Dict key need to be unique

user3 = {
    "name" : "Ahmed",
    "age" : 34,
    "skils" : [1,2,3],
    "active" : False
}

# Dict is not ordered, you can access its elements with key
print(user3["active"])
print(user3.keys())
print(user3.values)

# Dictionary methodes part one

# clear()
dicUser={
    "name" : "osama"
}

dicUser.clear()
print(dicUser)

# update()
dicUser.update({"age" : 24})
dicUser["con" : "Ned"]

print(dicUser)

#copy()
b = dicUser.copy()
print(b)