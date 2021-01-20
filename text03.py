'''
    判断二维数字列表中是否存在某个数字，二维列表就是列表中嵌套列表
    输入：[[1,2,3,4],[5,6,7,8,],[9,10,11,12]]、11
    输出：true
'''
list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
# list02 = []
# for line in list01:
#     for i in line:
#         list02.append(i)
# if str(input("请输入字符：")) in list02:
#     print(True)
# else:
#     print(False)

# for i in range(len(list01)):
#     for j in range(4):
#         if list01[i][j] == 11:
#             print(True)
#         else:
#             print(False)
for line in list01:
    if 11 in line:
        print(True)
        break
else:
    print(False)