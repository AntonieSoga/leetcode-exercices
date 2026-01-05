def merge_1(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    ans = []
    i =j = 0
    while i < m and j < n :
        if nums1[i] < nums2 [j] :
            ans.append(nums1[i])
            i += 1
        else:
            ans.append(nums2[j])
            j += 1
        
    ans.extend(nums1[i:m])
    ans.extend(nums2[j:n])
    
    return ans

print(merge_1([1,2,3],3,[2,5,6],3))

def merge_2(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    end = m + n - 1

    while m > 0 and n > 0:
        if nums1[m-1] > nums2[n-1]:
            nums1[end] = nums1[m-1]
            m -= 1
        else:
            nums1[end] = nums2[n-1]
            n -= 1
        end -= 1

    while n > 0:
        nums1[end] = nums2[n-1]
        n -= 1
        end -= 1


nums1 = [1,2,3,0,0,0]
merge_2(nums1, 3, [2,5,7], 3)
print(nums1)
