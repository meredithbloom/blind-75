# 49. Group Anagrams - Medium
'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

CONSTRAINTS
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

'''
from collections import Counter

def groupAnagrams(strings):
    # will be a list of sublists
    anagrams = []
    # could potentially keep a dictionary of counters 
    length_order = sorted(strings, key=len)
    if len(strings) == 1:
        anagrams.append(string)
    






input1 = ["eat","tea","tan","ate","nat","bat"]
input2 = [""]
input3 = ["a"]
