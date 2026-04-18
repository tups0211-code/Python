import csv 
f = open("data.csv", "w", newline="") 
w = csv.writer(f) 
w.writerow(["id", "name"]) 
w.writerow([1, "A"]) 
f.close() 
f = open("data.csv", "r") 
r = csv.reader(f) 
for row in r: 
 print(row) 
f.close() 