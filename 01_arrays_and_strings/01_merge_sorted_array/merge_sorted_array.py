class Solution:
    def merge (nums1: list[int], m, nums2: list[int], n) -> None :

        end = n + m - 1

        while n and m :
            if nums1[m-1] > nums2[n-1] :
                nums1[end] = nums1[m-1]
                m-=1
            else:
                nums1[end] = nums2[n-1]
                n-=1
            end-=1

        while m :
            nums1[end] = nums1[m-1]
            m -= 1
            end -=1
