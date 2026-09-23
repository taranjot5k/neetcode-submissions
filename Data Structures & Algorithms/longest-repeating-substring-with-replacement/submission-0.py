class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        r = 0
        count = {}
        maxLength = 0
        while r < len(s):
        
            count[s[r]] = count.get(s[r], 0) + 1 
            window_length = r - l + 1 #total characters in our current window
            replacement = window_length - max(count.values()) #most common character#max((count.values))
            


            if replacement > k: #Remove the old left character from my counts, then slide the left boundary forward
                count[s[l]] = count.get(s[l], 0) - 1
                l += 1
            maxLength = maxLength = max(maxLength, r - l + 1)
            r += 1

        return maxLength