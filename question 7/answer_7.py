nums = [1,1,2,3,4,]
val = 1
class Solution:
    def remove_element(nums,val):
        ans = []
        for x in nums:
            if x != val:
                ans.append(x)
        for y in range(len(ans)):
            nums[y] = ans[y]   
        return len(ans)

    
solution = Solution()
Solution.remove_element(nums,val)
print(nums) 
