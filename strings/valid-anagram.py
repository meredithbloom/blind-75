# 242. Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise

# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase english letters


from collections import Counter

def isAnagram(s, t):
    s_count = Counter(s) # O(n) - constructing counter requires iteration
    t_count = Counter(t)
    if (s_count == t_count):
        return True
    else:
        return False
    
        
            
a = 'anagram'
b = 'nagaram'

c = 'rat'
d = 'car'

print(isAnagram(a, b))
print(isAnagram(c, d))

# what if the inputs contained unicode characters? how would i adapt my solution to such a case?