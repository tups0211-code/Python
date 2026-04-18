s = input() 
v = 0 
c = 0 
d = 0 
sp = 0 
 
for ch in s: 
    if ch in "aeiouAEIOU": 
        v += 1 
    elif ch.isalpha(): 
        c += 1 
    elif ch.isdigit(): 
        d += 1 
    elif ch == " ": 
        sp += 1 
 
print(v, c, d, sp)