class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        freq={}

        for num in arr:
            freq[num] = freq.get(num,0)+1

        for num in arr:
            if num!=0 and 2*num in freq:
                return(True)
            if num==0 and freq[0]>1:
                return(True)
        return(False)