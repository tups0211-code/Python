a = {1, 2, 3, 4} 
b = {3, 4, 5, 6} 
print(a | b) 
print(a & b) 
print(a - b) 
#Find missing elements in a given range using sets 
nums = {1, 2, 4, 6, 7} 
start = 1 
end = 7 
full = set(range(start, end + 1)) 
missing = full - nums 
print(missing)