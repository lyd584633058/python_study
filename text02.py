'''
    假如有一只猴子摘了一堆桃子，第一天吃了当前总数的一半之后又多吃一个桃子，
    第二天也是吃了当前总数的一半之后又多吃一个桃子，以此类推，猴子在第八天的时候发现只剩一个桃子了，
    请问猴子第一天吃了多少个桃子？
'''
# num = 1
# for i in range(7):
#     num = (num + 1) * 2
# print("猴子第一天吃了%d个桃子" % (num / 2 + 1))
def eat(num):
    for i in range(7):
        num = num/2-1
    return num

num = 1
while True:
    num += 1
    if eat(num) == 1:
        print(num)
        break
