class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        begin, end = -1, -1
        left, right = 0, len(nums) - 1

        # First binary search: find the rightmost (last) occurrence of target
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid + 1
                end = mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        left, right = 0, len(nums) - 1

        # Second binary search: find the leftmost (first) occurrence of target
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right = mid - 1
                begin = mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return [begin, end]

# Time Complexity: O(log n) 
# Space Complexity: O(1) (no extra data structures used)

# Procedure:
# -> Initialize begin and end to -1 (default "not found" values)
# -> Perform binary search to find the rightmost index of target:
#    -> If nums[mid] == target, move left to mid+1 (search right), update end
#    -> If nums[mid] > target, move right to mid-1
#    -> If nums[mid] < target, move left to mid+1
# -> Reset left and right pointers
# -> Perform binary search to find the leftmost index of target:
#    -> If nums[mid] == target, move right to mid-1 (search left), update begin
#    -> If nums[mid] > target, move right to mid-1
#    -> If nums[mid] < target, move left to mid+1
# -> Return [begin, end] as the result

# Key Takeaways:
# -> Linear scanning after finding the target (even if you start with binary search) can degrade to O(n) time in the worst case.
# -> The optimal way is to use two modified binary searches: one for the leftmost (first) occurrence, and one for the rightmost (last).
# -> When you find the target, don't stop—instead, keep searching in the direction of the edge (left for first, right for last).
# -> This guarantees O(log n) runtime, which is critical for large sorted arrays.
# -> Always consider edge cases: empty array, all elements are target, target not present.
# -> If the first search (for leftmost) fails (returns -1), you can skip the second search for a minor optimization.
# -> Binary search is versatile: by tweaking the update of left/right pointers, you can find specific boundaries, not just existence.

# Problem Statement:
# Given a sorted array "nums", return the indices of the first and last occurrence of "target".
# If target does not exist, return [-1, -1].
