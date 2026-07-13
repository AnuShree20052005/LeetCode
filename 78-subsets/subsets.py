class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(start):
            result.append(subset[:])

            for i in range(start, len(nums)):
                subset.append(nums[i])      # Choose
                backtrack(i + 1)            # Explore
                subset.pop()                # Backtrack

        backtrack(0)
        return result