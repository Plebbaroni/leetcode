class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        ans = []
        for asteroid in asteroids:
            while ans and ans[-1] > 0 and asteroid < 0:
                if abs(asteroid) > ans[-1]:
                    ans.pop()
                    continue
                if abs(asteroid) == ans[-1]:
                    ans.pop()
                    break
                else:
                    break
            else:
                ans.append(asteroid)
        return ans


        