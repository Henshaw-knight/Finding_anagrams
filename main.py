"""A python program to check if two words are anagrams"""

def find_anagram(word, anagram):    
    # converting both strings into lowercase and then to list
    word = list(word.lower())
    anagram = list(anagram.lower())

    # sorting the lists
    word.sort()
    anagram.sort()

    if word == anagram:
        return True
    else:
        return False  

print(find_anagram("hello", "check")) # --> False
print(find_anagram("below","elbow")) # --> True
