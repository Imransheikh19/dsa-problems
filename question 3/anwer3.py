array =[1,3,6,9]
target = 15

def solution():
    list =[]
    for x in range(len(array)):
        for y in range(x+1,len(array)):
            if array[x] + array[y] == target:
                list.append(x)
                list.append(y)
                return list
        
print(solution())