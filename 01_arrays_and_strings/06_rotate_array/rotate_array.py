class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #via list slicing
        n = len(nums)
        k = k % n
        self.reverse(nums,0,n-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,n-1)
        

    def reverse(self, nums: list[int], start: int, end: int) -> None:
        while start < end:
            aux = nums[start]
            nums[start] = nums [end]
            nums[end] = aux
            end -= 1
            start +=1