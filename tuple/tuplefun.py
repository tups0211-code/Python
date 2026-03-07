mytuple = (86, 56, 78, 98, 54)
print(mytuple)
print(mytuple[4])

# mytuple[2] = 34     #its not possible , tuple = imutable
# print(mytuple)

student = ("ram","sham","sham","sham",90,96)
print(student)
print(type(student))

#empty tuples
emptytuple = ()
print(type(emptytuple))

#singletuple
single = (1,)
print(type(single))

print(student.index("sham"))
print(student.count("sham"))

marks =(99,97,96,59,45,34)
print(max(marks))
print(min(marks))
