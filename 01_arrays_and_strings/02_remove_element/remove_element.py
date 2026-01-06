class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        end = len(nums)
        for n in range(0,end):
            if nums[n] != val:
                nums[k] = nums[n]
                k +=1
        return k