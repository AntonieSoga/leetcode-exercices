class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 1
        counter = 1
        for j in range(1,len(nums)) :
            if nums[j] == nums[j-1]:
                counter += 1
            else: 
                counter = 1
        
            if counter <= 2:
                nums[i] = nums[j]
                i += 1

        return i