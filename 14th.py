d = {"a": 1, "b": 2, "c": 3, "d": 4} 
del d["a"] 
print(d) 
x = d.pop("b") 
print(x) 
print(d) 
y = d.popitem() 
print(y) 
print(d) 
d.clear() 
print(d) 