s = input()
words = s.split()
rev = ""
for i in range(len(words)-1, -1, -1):
 rev += words[i] + " "
print(rev.strip())