class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        if x <= arr[0]:
            return arr[0:k]
        elif x >= arr[-1]:
            return arr[-k:]
        while left < right:
            mid = left + (right - left) // 2
            if x - arr[mid] <= arr[mid + k] - x:
                right = mid
            else:
                left = mid + 1
        return arr[left:left + k]

# Time complexity: O(log(n-k)), where n is the length of arr.
# Space complexity: O(1) (excluding output).
# 
# Procedure:
# -> Handle edge cases: If x is less than or equal to the first element, return the first k elements.
# -> If x is greater than or equal to the last element, return the last k elements.
# -> Otherwise, perform binary search for the optimal starting index of the k-sized window.
# -> At each step, compare the distance of arr[mid] from x with arr[mid + k] from x.
# -> If arr[mid] is closer or equally close (and smaller), move right to mid (keep arr[mid]).
# -> Otherwise, move left to mid + 1 (discard arr[mid], prefer arr[mid + k]).
# -> When left == right, the window arr[left:left + k] is the answer.
#
# Key takeaways:
# - For a sorted array, the k closest elements always form a contiguous subarray.
# - Binary search efficiently finds the best window, leveraging the sorted property.
# - Edge cases are handled directly for performance.
# - This approach is much more efficient than sorting by absolute difference.
