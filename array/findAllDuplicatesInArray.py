class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict = set()
        dupes = []
        for i in nums:
            if i in dict:
                dupes.append(i)
            else: 
                dict.add(i)
        return dupes
        