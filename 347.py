class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result=[]
        freq_dict={}
        num_set=set(nums)
        for num in nums:
            if num in freq_dict:
                freq_dict[num]+=1
            else:
                freq_dict[num]=1
        for i in range(k):
            max=0
            max_num=0
            for num in num_set:
                if(freq_dict[num]>max):
                    max=freq_dict[num]
                    max_num=num
            freq_dict[max_num] = 0
            result.append(max_num)
        return(result)