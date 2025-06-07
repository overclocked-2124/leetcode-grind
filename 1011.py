class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total_weight = 0
        for w in weights:
            total_weight += w
         
        # Search bounds: [max single package, sum of all packages]
        left, right = max(weights), total_weight

        # Binary search on answer space
        while left <= right:
            mid = (left + right) // 2
            if self.checkWeight(mid, days, weights):
                right = mid - 1
            else:
                left = mid + 1
        
        return left
    
    def checkWeight(self, maxWeight: int, days: int, weights: List[int]) -> bool:
        # Simulate loading packages in order
        days_used, current_load = 1, 0
        for w in weights:
            if current_load + w > maxWeight:
                # start a new day
                days_used += 1
                current_load = w
            else:
                current_load += w
        return days_used <= days


# Problem:
#   Given an array weights[] and an integer days, find the minimum ship capacity so that
#   all packages can be shipped in order within the given number of days.
#
# Time Complexity: O(n log S)
#   where n = len(weights), S = sum(weights).
#   - Each binary search step costs O(n) to simulate checkWeight.
#   - There are O(log S) steps.
#
# Space Complexity: O(1)
#   Only a few integer variables are used.
#
# Procedure:
#   1. Compute total_weight = sum(weights).
#   2. Initialize left = max(weights), right = total_weight.
#   3. While left <= right:
#        - mid = (left + right) // 2
#        - if checkWeight(mid) is True (can ship within days):
#             right = mid - 1     -> try smaller capacity
#          else:
#             left = mid + 1      -> need larger capacity
#   4. Return left as the minimum working capacity.
#
# checkWeight(maxWeight):
#   - days_used = 1, current_load = 0
#   - For each package weight w:
#       if current_load + w > maxWeight:
#         days_used += 1      -> start a new day
#         current_load = w
#       else:
#         current_load += w   -> add to current day
#   - Return True if days_used <= days, else False
#
# Key Takeaways:
#   - This is a classic "binary search on answer" pattern: the predicate (can we ship?)
#     is monotonic in the capacity.
#   - Boundaries: left = max(weights) (lowest feasible), right = sum(weights) (highest needed).
#   - When predicate(mid) is True, move right = mid - 1 to find a smaller valid capacity.
#   - After loop, left is the smallest capacity that satisfies the predicate.
#   - Simulate day-count carefully: start count at 1, use '>' (not '>=') to detect overflow,
#     and increment exactly when starting a new day.
#   - Always use integer division (//) for mid.
#   - Call member functions with self.checkWeight(...).
