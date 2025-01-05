class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = []
        for char in s:
            if char == '*':
                ans.pop()
            else:
                ans.append(char)
        return ''.join(ans)
