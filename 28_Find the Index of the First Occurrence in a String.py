"""
Given two strings needle and haystack, 
return the index of the first occurrence of 
needle in haystack, or -1 if needle is not part of haystack.
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = haystack.find(needle)
        return index if index != -1 else -1

test = Solution()
print(test.strStr("sadbutsad", "sad")) # 0
            
        
            
                 