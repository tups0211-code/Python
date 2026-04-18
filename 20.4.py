l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
common = []
for i in l1:
 if i in l2 and i not in common:
   common.append(i)
print(common)