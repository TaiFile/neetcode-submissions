class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        final_array =  nums1 + nums2
        final_array.sort()
        size = len(final_array)
        if size % 2 == 1:
            return final_array[size//2]
        result = (final_array[size//2] + final_array[(size//2) - 1]) / 2
        return result