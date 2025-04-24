# set in python
# set itmes are inclosed in curly braces
mySetOne={}

# Set itmes are not ordered and not indexed
mySetTow= {"Ali",23,True}
print(mySetTow)
#print(mySetTow[0]) not indexed

# Set has only immutable data type(numbers,strings,tuples) list and dict not
mySetThree={"Ali",343,"Osman",677,True,[1,2,3]}
#print(mySetThree) error unhashable type list

# Set itmes is unique
mySetFour={1,2,"osama","osama",1}
print(mySetFour) #it will not repate the same item tow time

# Set methods part one

# clear()
a={1,2,3}
a.clear()
print(a)

# union()
b={"one","tow","three"}
c={"1","2","3"}
print(a | b)
print(b.union(c))

# add()
d ={1,2,3,4}
d.add(5)
d.add(6)
print(d)

# copy()
e={1,2,3,4}
f=e.copy(e)
print(f)

# remove()
g={2,3,5,6,874,35}
g.remove(2)
#g.remove(100) error

# discard()
h={55,38,1,4}
h.discard(55)
h.discard(100) # Does not show any error

# pop()
i={1,2,4,"ali",3}
print(i.pop()) #It will pick rendom element form the set


# update()
j={3,4,5,"Ali"}
k={3,4,5,"osman"}
j.update(k)
print(k)