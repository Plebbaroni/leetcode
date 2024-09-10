class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word1Count = 0
        word2Count = 0
        letterStack = []
        if (len(word2) > 0):
            while (word1Count < len(word1) and word2Count < len(word2)):
                letterStack.append(word1[word1Count])
                letterStack.append(word2[word2Count])
                word1Count += 1
                word2Count += 1
            if (word1Count < len(word1)):
                letterStack.append(word1[word1Count:len(word1)])
            elif (word2Count < len(word2)):
                letterStack.append(word2[word2Count:len(word2)])
            return "".join(letterStack)
        else:
            return word1