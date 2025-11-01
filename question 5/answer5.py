nums = [1,4,6,9]


def solution():
    condition = 0
    ans =[]
    while condition < 2:
        for num in nums:
            ans.append(num)
        condition +=1
    return ans

print(solution())