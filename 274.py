# Problem:
# 274. H-Index
# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper,
# return the researcher's h-index.
# The h-index is defined as the maximum value of h such that the given researcher has published at least h papers
# that have each been cited at least h times.

# Approach:
# - Use a counting sort (bucket) approach for O(n) time complexity.
# - Create a bucket array of size n+1 (where n is the number of papers).
#   - bucket[i] counts how many papers have exactly i citations.
#   - bucket[n] counts all papers with n or more citations (since h-index can't be more than n).
# - Populate the bucket by iterating over citations.
# - Iterate backwards from n to 0, maintaining a running total of papers with at least i citations.
# - The first i where total >= i is the h-index.

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        total = 0
        bucket = [0] * (n + 1)
        for cit in citations:
            if cit < n:
                bucket[cit] += 1
            else:
                bucket[n] += 1
        for i in range(n, -1, -1):
            total += bucket[i]
            if total >= i:
                return i

# Time Complexity: O(n), where n is the number of papers.
#   - One pass to fill the bucket array.
#   - One pass to compute the h-index.
# Space Complexity: O(n), for the bucket array of size n+1.

# Key Takeaways:
# -> Use bucket counting to avoid sorting and achieve linear time.
# -> Always allocate n+1 buckets to group all citations >= n together.
# -> Iterate from high to low to find the maximum valid h-index.
# -> Include i=0 in the search to handle the case where all papers have 0 citations.
# -> Avoid using reversed() on lists when index access is needed; use range(n, -1, -1) instead.
# -> This approach is more efficient than the O(n log n) sorting-based method.



# Example:
# Input: citations = [3,0,6,1,5]
# After bucketing: [1,1,0,1,0,2]
# Running total from i=5 down: 2,2,3,4,5,5
# First i where total >= i is 3, so h-index = 3.



