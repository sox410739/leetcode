#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        allNumber = []
        nums1.append(10**6 + 1)
        nums2.append(10**6 + 1)
        while(len(nums1) > 1 or len(nums2) > 1):
            if(nums1[0] < nums2[0]):
                allNumber.append(nums1[0])
                del nums1[0]
                continue

            if(nums1[0] > nums2[0]):
                allNumber.append(nums2[0])
                del nums2[0]
                continue

            if(nums1[0] == nums2[0]):
                allNumber.append(nums1[0])
                allNumber.append(nums2[0])
                del nums1[0]
                del nums2[0]
                continue
        

        length = len(allNumber)
        if(length & 1 == 0):
            return float((allNumber[length//2] + allNumber[length//2-1])/2)
        return float(allNumber[length//2])
# @lc code=end

