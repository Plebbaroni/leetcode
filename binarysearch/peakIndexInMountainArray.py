class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        start, end = 0, len(arr)-1
        if end == 0:
            return arr[0]
        while start <= end:
            mid = start + (end-start)/2
            if arr[mid] < arr[mid+1]:
                start = mid+1
            elif arr[mid] < arr[mid-1]:
                end = mid-1
            elif arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
                return mid
        return mid