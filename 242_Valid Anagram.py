
"""
Given two strings s and t, return true if t is an anagram of s, 
and false otherwise.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    

test = Solution()
print(test.isAnagram("anagram", "nagaram"))