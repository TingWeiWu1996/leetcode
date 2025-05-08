class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        result = []
        i = 0
        j = 0
        while i < n or j < m:
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1

        return ''.join(result)