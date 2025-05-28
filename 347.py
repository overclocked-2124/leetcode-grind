"""
347. Top K Frequent Elements (Medium)

Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k is in the range [1, the number of unique elements in the array]
- Follow up: Time complexity must be better than O(n log n)
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets=[[] for _ in range(len(nums)+1)]
        result=[]
        freq_dict={}
        for num in nums:
            freq_dict[num] = freq_dict.get(num,0)+1
        for num , count in freq_dict.items():
            buckets[count].append(num)
        
        for bucket in reversed(buckets):
            for num in bucket:
                result.append(num)
                if len(result) ==k:
                    return(result)
        return(result)

# Time Complexity: O(n)
# Space Complexity: O(n)

# Procedure: Bucket Sort Approach
# -> Create buckets array with size n+1 (since max frequency can be n)
# -> Build frequency dictionary using freq.get(num, 0) + 1 to count occurrences  
# -> Place each number into bucket at index equal to its frequency
# -> Iterate buckets backwards (highest to lowest frequency) using reversed()
# -> Collect numbers from buckets until we have k elements
# -> Return result when exactly k elements found

# Key Takeaways:
# 1. Bucket sort achieves O(n) time by using frequency as array index
# 2. Lists inside buckets needed because multiple numbers can have same frequency
# 3. freq.get(num, 0) safely gets count or returns 0 if key doesn't exist
# 4. freq.items() returns (key, value) pairs from dictionary
# 5. reversed(buckets) iterates from highest frequency to lowest
# 6. Early return when len(result) == k optimizes the solution
# 7. This approach beats O(n log n) requirement from follow-up question
