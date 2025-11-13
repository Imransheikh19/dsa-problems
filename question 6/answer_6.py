strs = ["dance","cag","danger","damage"]
class Solution:
    def longestCommonPrefix(self,strs):
        ans =""
        for x in range(len(strs[0])):
            for str in strs:
                if x == len(str) or str[x] != strs[0][x]:
                    return ans 
            ans += strs[0][x]
        return ans
    
solution = Solution()   
print(solution.longestCommonPrefix(strs))