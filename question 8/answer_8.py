nums = [5,5,1,1,1,5,5]
class Solution:
    # def majorityElement(self,nums):
    #     prev = []
    #     max_element = 0
    #     for x in range(len(nums)):
    #         count = 0
    #         if nums[x] in prev:
    #             continue
    #         prev.append(nums[x])  
    #         for y in range(x+1,len(nums)):
    #             if nums[x] == nums[y]:
    #                 count += 1
    #         if max_element == 0 or max_element < count:
    #             max_element = nums[x]   
    #     return max_element
    def majorityElement(self,nums):
        n = len(nums)
        for num in nums:
            count = sum(1 for i in nums if i == num)
            if count > n // 2:
                return num



solution = Solution()
print (solution.majorityElement(nums))