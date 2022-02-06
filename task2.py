from collections import Counter

def anagram(s1, s2):
    if (Counter(s1) == Counter(s2)):
        print("The strings are anagram")
    else:
        print("The strings are not anagrams.")


# driver code
s1 = "maya"
s2 = "yma"
anagram(s1, s2)