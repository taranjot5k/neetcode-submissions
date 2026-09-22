class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        charSet = set()
        maxLength = 0


        for r in range(len(s)): 
            while s[r] in (charSet): #while the char at my right pointer alr exists in my curr window, i have a dup
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            length = r - l + 1
            if maxLength < length: 
                maxLength = max(maxLength, length)
        
        return maxLength 




        
        