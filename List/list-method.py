marks = [99,100,90,95]

marks.append(88)
print("after append",marks)

marks.insert(1,80)
print("after insert",marks)

marks.remove(99)
print("after remove",marks)

marks.pop(2)
print("after pop",marks)

marks.sort()
print("after sort",marks)

marks.reverse()
print("after reverse",marks)


print(len(marks))
print(max(marks))
print(min(marks))

