'''
    找出字符串中第一个不重复的字符
    输入：ABCACDBEFD
    输出：E
'''
list01 = ["A","B","C","A","C","D","B","E","F","D"]
for i in list01:
    if list01.count(i) == 1:
        print(i)
        break