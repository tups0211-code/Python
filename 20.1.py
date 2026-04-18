l = list(map(int, input().split()))
freq = {}
for i in l:
 if i in freq:
   freq[i] += 1
 else:
   freq[i] = 1
print(freq)