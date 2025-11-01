str1 = "racecar"
str2 = "carrace"

print(str1[0])

# def anagram():
#     flag = False
#     for x in range(len(str1)):
#         for y in range(len(str2)):
#             if y < len(str2) -1 :
#                 if str1[x] == str2[y]:
#                     flag = True
#                     break 
#                 else:
#                     flag = False
            
#             else:
#                 if str1[x] == str2[y]:
#                     flag = True
#                     break 
#                 else:
#                     flag = False
#                     return flag
        
#     return flag    


def anagram():
    if len(str1) != len(str2):
        return False
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

print(anagram())
     