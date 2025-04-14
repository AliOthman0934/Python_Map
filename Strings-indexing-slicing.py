myString ="This is text"
print(myString[0])
print(myString[-1])
print(myString[4:8])
print(myString[4:8:2])

# Strings emthods
# strip(),rstrip(),lstrip()


a ="   This is string    "
print(a.strip())
print(a.lstrip())

#title()
print(a.title())

#capitalize()
print(a.capitalize())

b,d,f = "2","44","5953"
print(b.zfill(4))
print(d.zfill(4))
print(f.zfill(4))

#upper()
print(a.upper())

#lower()
print(a.lower())

#split(),rsplit()
g="Hello my name is ali"
print(g.split())
print(g.split("-",2))

# count()
h="This is text"
print(h.count("t"))

#center()
print(h.center(15,"#"))

#sawpcase()
print(h.swapcase())

#startsWith()
print(h.startswith("i"))

#endWith()
print(h.endswith("t"))

#index()
print(h.index("p"))
#print(h.index("p",0,15)) error

#find()
#same method like index 

#rjust(width,fill char)
#same like center()

#splitline()
lin=""" hallo
heelo
hey"""
print(lin.splitlines())

#istitle()
print(h.istitle())

#islower()
print(h.islower())

#isspace()
#isidentifier()
#isaplpha()
#isalnum()

#replace()
replaceText="hallo this me "
print(replaceText.replace("this","is",1))