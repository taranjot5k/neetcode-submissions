class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        l = 0
        r = 0
        charCount = {} # count char in s1
        windowCount = {} # count char in s2

        while r < len(s1):
            charCount[s1[r]] = charCount.get(s1[r], 0) + 1
            r += 1

        r = 0
            
        while r < len(s2):
            windowCount[s2[r]] = windowCount.get(s2[r], 0) + 1
            currentWindow = r - l + 1

            if currentWindow > window_size: # is window too big?
                windowCount[s2[l]] = windowCount[s2[l]] - 1
                if windowCount[s2[l]] == 0:
                    del windowCount[s2[l]]
                l += 1

            if charCount == windowCount:
                return True
            r += 1

        return False