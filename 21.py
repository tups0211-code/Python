f = open("file.txt", "w") 
f.write("Hello\nWorld\nPython") 
f.close() 
f = open("file.txt", "r") 
for line in f: 
 print(line.strip()) 
f.close() 