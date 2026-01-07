class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Boyer-Moore Voting Algorithm
        candidate = None
        count = 0

        for num in nums:
            # If count is 0, we pick a new candidate
            if count == 0:
                candidate = num
            
            # Increment count if we see the candidate, otherwise decrement
            count += (1 if num == candidate else -1)

        return candidate