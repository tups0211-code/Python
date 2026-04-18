nums = {1, 2, 4, 6, 7}
start = 1
end = 7
full = set(range(start, end + 1))
missing = full - nums
print(missing)