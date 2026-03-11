#count the vowels and consonants 
ef count(name):
    vowels = "aeiouAEIOU"
    countvowels = 0
    countconsonent=0

    for eachChar in name:
        if(eachChar.isalpha()):
            if(eachChar in vowels):
                countvowels = countvowels+1
            else : 
                countconsonent=countconsonent+1
    return countvowels,countconsonent

vowels,consonants=count("Trupti Nishant Thengil")
print("vowels = ",vowels)
print("consonants = ",consonants)
