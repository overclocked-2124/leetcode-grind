# Problem:
# 33. Search in Rotated Sorted Array (LeetCode)
# Given a rotated sorted array (distinct integers, rotated at unknown pivot), 
# return the index of the target if present, else -1.
# Must run in O(log n) time.

# Approach:
# -> Use modified binary search.
# -> At each step, check if left or right half is sorted.
# -> Decide which half to search based on where the target could lie.
# -> Repeat until found or search space is exhausted.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # If left half is sorted
            elif nums[mid] >= nums[left]:
                # If target is in the sorted left half
                if target >= nums[left] and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Otherwise, right half is sorted
            else:
                # If target is in the sorted right half
                if target >= nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

# Time Complexity: O(log n)
#   -> Each iteration halves the search space, like classic binary search.

# Procedure:
#   -> Initialize left and right pointers.
#   -> While left <= right:
#       -> Find mid.
#       -> If nums[mid] == target, return mid.
#       -> If left half is sorted (nums[left] <= nums[mid]):
#           -> If target in [nums[left], nums[mid]], search left (right = mid-1).
#           -> Else, search right (left = mid+1).
#       -> Else (right half is sorted):
#           -> If target in [nums[mid], nums[right]], search right (left = mid+1).
#           -> Else, search left (right = mid-1).
#   -> If not found, return -1.

# Key Takeaways:
#   -> In a rotated sorted array, at least one half is always sorted.
#   -> Use the sorted half to decide if the target could be there.
#   -> This preserves O(log n) complexity, even with rotation.
#   -> Avoid off-by-one errors in range checks (use < and > appropriately).
#   -> No need to find the pivot explicitly.
