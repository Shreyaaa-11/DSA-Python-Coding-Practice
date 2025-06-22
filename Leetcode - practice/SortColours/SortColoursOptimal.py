#Dutch National Flag problem solution

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        low = mid = 0
        high = n - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


#The Dutch National Flag Algorithm is used to sort an array with three distinct elements (like 0, 1, and 2) into three separate groups. It's named after the Dutch flag, which has three colors.

#It uses three pointers:
#low – marks the boundary for 0s,
#mid – the current element being checked,
#high – marks the boundary for 2s.

#Loop while mid <= high:

#If arr[mid] == 0: swap arr[low] and arr[mid], increment both.
#If arr[mid] == 1: just increment mid.
#If arr[mid] == 2: swap arr[mid] and arr[high], decrement high.