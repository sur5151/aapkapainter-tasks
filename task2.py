from collections import Counter

def anagram(s1, s2):
    if (Counter(s1) == Counter(s2)):
        print("The strings are anagram")
    else:
        print("The strings are not anagrams.")



s1 = "atal"
s2 = "lata"
anagram(s1, s2)
