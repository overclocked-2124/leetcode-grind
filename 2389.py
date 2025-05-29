"""
Program to return, for each query, the maximum size of a subsequence from nums
such that the sum of its elements is less than or equal to the query value.

Approach:
- Sort nums to prioritize smallest elements (greedy).
- Build prefix sum array to enable efficient sum checks.
- For each query, use manual binary search to find the largest prefix sum
  less than or equal to the query.
"""

from typing import List

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        answer = []
        pre_sum = []
        nums.sort()
        sum_p = 0
        for i in range(len(nums)):
            sum_p += nums[i]
            pre_sum.append(sum_p)

        for query in queries:
            result = -1
            left, right = 0, len(pre_sum) - 1

            # Manual binary search: find rightmost prefix sum <= query
            while left <= right:
                mid = (left + right) // 2
                if pre_sum[mid] <= query:
                    result = mid
                    left = mid + 1
                else:
                    right = mid - 1
            answer.append(result + 1)  # +1 because indices are 0-based
        return answer

# Time Complexity:
# - Sorting nums: O(n log n)
# - Building prefix sum: O(n)
# - Each query: O(log n) (manual binary search)
# - Total: O(n log n + m log n), where n = len(nums), m = len(queries)

# Key Takeaways:
# 1. Precomputing prefix sums allows for efficient queries on subsequence sums.
# 2. Manual binary search can be used to find the largest valid subsequence size for each query.
# 3. Alternatively, Python's bisect_right can replace manual binary search for even cleaner code:
#    idx = bisect_right(pre_sum, query)
#    answer.append(idx)
