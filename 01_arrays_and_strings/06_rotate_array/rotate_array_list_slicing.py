class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #via list slicing
        k = k % len(nums)
        if k:
            nums[:k], nums [k:] = nums[-k:], nums[:-k]