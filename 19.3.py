s = input()
result = ""
for ch in s:
 if ch == " ":
  result += "-"
 else:
  result += ch
print(result)