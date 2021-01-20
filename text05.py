'''
    质数：大于1的整数，除了1和它本身以外不能再被其他数字整除。
        让客户输入一个数字，我们判断是不是质数，
        是就输出True，不是输出False
'''
num = int(input("请输入一个整数："))
for i in range(2,num):
    if num % i == 0:
        print(False)
        break
else:
    print(True)
