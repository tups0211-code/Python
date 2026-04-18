import json 
data = {"id": 1, "name": "A"} 
f = open("data.json", "w") 
json.dump(data, f) 
f.close() 
f = open("data.json", "r") 
print(json.load(f)) 
f.close() 