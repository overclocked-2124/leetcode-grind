"""
Problem: Sort Colors (Dutch National Flag Problem)

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:
- n == nums.length
- 1 <= n <= 300
- nums[i] is either 0, 1, or 2
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low,mid,high=0,0,len(nums)-1

        while(high>=mid):
            if(nums[mid]==0):
                temp=nums[mid]
                nums[mid]=nums[low]
                nums[low]=temp
                mid+=1
                low+=1
            elif(nums[mid]==1):
                mid+=1
            elif(nums[mid]==2):
                temp=nums[mid]
                nums[mid]=nums[high]
                nums[high]=temp
                high-=1

# Time Complexity: O(n) - each element is processed at most once
# Space Complexity: O(1) - in-place sorting, only using constant extra space

# Procedure: Dutch National Flag Algorithm
# -> Initialize three pointers: low=0, mid=0, high=n-1
# -> Create invariant: [0,low-1] contains 0s, [low,mid-1] contains 1s, [high+1,n-1] contains 2s
# -> Process unknown region [mid,high] until mid > high
# -> For nums[mid]==0: swap with nums[low], increment both low and mid (0 goes to correct position)
# -> For nums[mid]==1: just increment mid (1 is already in correct region)
# -> For nums[mid]==2: swap with nums[high], decrement high only (need to check swapped value)
# -> Continue until entire array is partitioned correctly

# Key Takeaways:
# 1. Why different from normal sorting: Only 3 distinct values (0,1,2) allows O(n) solution vs O(n log n)
# 2. Dutch National Flag optimizes for limited value range - more efficient than general sorting
# 3. Algorithm maintains invariant: processed regions stay sorted while unknown region shrinks
# 4. Critical insight: Don't increment mid when swapping with high - new value needs checking
# 5. Three-pointer technique efficiently partitions array in single pass
# 6. In-place sorting achieved with O(1) extra space using clever swapping strategy
