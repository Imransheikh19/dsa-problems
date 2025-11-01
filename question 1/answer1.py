array = [1,2,31,4,31,5,6,]

#solution 1

# def check():
#     for x in range(len(array)):
#         curr = array[x]
#         for y in range(len(array)):
#             if x == y:
#                 continue
#             if curr == array[y]:
#                 return True
#     return False
      

#solution 2

def check():
    for x in range(len(array)):
        for y in range(x+1,len(array)):
            if array[x] == array[y]:
                return True
    return False

print(check())