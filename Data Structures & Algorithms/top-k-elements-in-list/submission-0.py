class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        freq_count ={}
        for num in nums:
            if num in freq_count :
                freq_count[num]+=1
            else :
                freq_count[num]=1
        
            
        freq_bucket = [[] for _ in range(len(nums)+1)]

        for num, count in freq_count.items():
            freq_bucket[count].append(num)

        for i in range(len(freq_bucket)-1,0,-1):
            for num in freq_bucket[i]:
                res.append(num)
                if len(res) == k :
                    return res
