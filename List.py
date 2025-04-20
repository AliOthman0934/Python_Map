# lists 
# 1) List itmes are enclosed in sqarwe brackets.
# 2) List are ordered, To use  index to access the item
# 3) list are mutable=> add,delete,edite
# 4) List items is not unique.


myAwesomList = ["one","two","ali","ahmed",1,3445,True]
print(myAwesomList)
print(myAwesomList[3])

myAwesomList[3] = "osman"
myAwesomList[0:2] = []
print(myAwesomList)


# List methods part 1

# append()

a = [1,2,3,4,5]
rendom = ["appel","banana"]
a.append(6)
print(a)
a.append(rendom)
print(a[6][1])

# extend()
b = ["ali","osamn"]
c = [29,59]

b.extend(c)
print(b)


# remove()

d = ["water","milk"]
d.remove("milk")
print(d)


# sort()

c =[1,2,66,3422,554]
c.sort()
print(c)

# reverse()

e = ["osman",4,"ali",5]
e.reverse()
print(e)