arr = [2,4,5,3,1,2]
class Solution():
    def replaceElements(self,arr):
        for x in range(len(arr)):
            gretest_element = 0
            prev = 0
            for y in range(x + 1,len(arr)):
                if gretest_element == 0 or gretest_element < arr[y]:
                    gretest_element = arr[y]
                prev = arr[y]
            arr[x] = gretest_element
        arr[len(arr)-1] = -1
        return arr

solution = Solution()
print(solution.replaceElements(arr))


# class Solution:
#     def replaceElements(self, arr: List[int]) -> List[int]:
#         n = len(arr)
#         ans = [0] * n
#         for i in range(n):
#             rightMax = -1
#             for j in range(i + 1, n):
#                 rightMax = max(rightMax, arr[j])
#             ans[i] = rightMax
#         return ans
