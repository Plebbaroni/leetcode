class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        initsat, maxsat, tempsat = 0, 0, 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                initsat += customers[i]
            if grumpy[i] == 1 and i < minutes:
                tempsat += customers[i]
        maxsat = tempsat
        for i in range(minutes, len(customers)):
            if grumpy[i] == 1:
                tempsat += customers[i]
            if grumpy[i-minutes] == 1:
                tempsat -= customers[i-minutes]
            maxsat = max(tempsat, maxsat)
        return initsat+maxsat
            