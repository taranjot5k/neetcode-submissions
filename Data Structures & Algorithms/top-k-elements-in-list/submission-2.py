class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #hashmap
        #special array thats going to be the same size as the input array
        freq = [[]for i in range(len(nums)+ 1)]

        for n in nums: #how many times a number is repeated in nums
            count[n] = 1 + count.get(n, 0)
         #going through each value that we counted
        for n, c in count.items(): #returns key value pairs that we added to our dict
            freq[c].append(n) #value of n occurs c amount of times

        res = []
        for i in range(len(freq) -1, 0, -1): 
            for n in freq[i]:
                res.append(n)#value that occurs most freq
                if len(res) == k: 
                    return res

        




