class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged=[]
        cur1=0
        cur2=0
        while cur1!=len(nums1) and cur2!=len(nums2):
            if nums1[cur1]<=nums2[cur2]:
                merged.append(nums1[cur1])
                cur1+=1
            else:
                merged.append(nums2[cur2])
                cur2+=1

        if cur1!=len(nums1):
            merged+=nums1[cur1:]
        elif cur2!=len(nums2):
            merged+=nums2[cur2:]

        if len(merged)%2==0:
            return float(merged[len(merged)/2-1]+merged[len(merged)/2])/2
        else:
            return merged[len(merged)//2]