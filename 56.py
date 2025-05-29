"""
56. Merge Intervals
Medium

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]

        for current in intervals[1:]:
            last_interval = result[-1]

            if(current[0]<=last_interval[1]):
                last_interval[1]=max(last_interval[1],current[1])          
            else:
                result.append(current)
        return result

# Time Complexity: O(n log n)
# Space Complexity: O(1) extra space (excluding output)

# Procedure: 
# -> Sort intervals by start time to ensure left-to-right processing
# -> Initialize result with first interval 
# -> Iterate through remaining intervals
# -> Check overlap condition: current_start <= last_end
# -> If overlap: merge by extending end to maximum of both ends
# -> If no overlap: append current interval as separate interval
# -> Return merged result

# Key Takeaways:
# - Sorting is crucial: Input intervals are not guaranteed to be sorted by start time
# - Overlap condition: Two intervals [a,b] and [c,d] overlap if c ≤ b (assuming sorted order)
# - Merging logic: Keep minimum start (guaranteed by sorting) and maximum end
# - Alternative approaches: Boolean array method works but has O(max_value) space complexity
# - Edge cases: Handle empty input, single interval, adjacent intervals (touching endpoints count as overlap)
# - In-place optimization: Modify last interval directly instead of creating new intervals for better memory usage