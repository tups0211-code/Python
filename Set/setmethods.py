num1= {1,2,3}
num2 = {2,3,4}

num1.add(4)
print(num1)

num1.remove(4)
print(num1)

num1.pop()
print(num1)

result = num1.union(num2)
print(result)

result = num1.intersection(num2)
print(result)

num1.clear()
print(num1)

empty_set = set()
print(empty_set)
