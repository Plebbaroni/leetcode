class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        #put nums onto stack until you find operator in which case evaluate
        #the thingy, and push the result.
        stack = []
        for t in tokens:
            if t == '+':
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif t == '-':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b - a)
            elif t == '*':
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif t == '/':
                a = float(stack.pop())
                b = float(stack.pop())
                stack.append(int(b/a))
            else:
                stack.append(t)
        return int(stack.pop())