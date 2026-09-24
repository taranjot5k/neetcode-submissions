class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        r = 0 
        charCount = {}
        longestWindow = 0

        while r < len(s):
            charCount[s[r]] = charCount.get(s[r], 0) + 1
            windowLength = r - l + 1
            replacement = windowLength - max(charCount.values())
            
            if replacement > k:
                charCount[s[l]] = charCount[s[l]] - 1
                l += 1
            longestWindow = max(longestWindow, r - l + 1)
            r += 1 
    
        return longestWindow
        

        