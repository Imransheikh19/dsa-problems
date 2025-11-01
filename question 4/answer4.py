str ='code'
class Solution:
    def ascii_calculator(self,str):
        value = 0
        for x in range(len(str)-1):
            diff = abs(ord(str[x+1]) - ord(str[x]))
            value += diff
        return value

Solution = Solution()
print(Solution.ascii_calculator(str))