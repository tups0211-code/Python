def find_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"
    for char in text:
     if char in vowels:
        count = count +1
    return count

text = input("enter a string : ")
result = find_vowels(text)
print("total vowels are : ",result)
