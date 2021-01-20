'''
    双十一到了，我们网购书本，书本正常单价为25元一本，
    但是双十一打4.5折，运费第一本3元，之后每多一本书多加0.5元，
    请问买35本书共花费多少元？请问我们买书马云亏了多少钱？
'''
book_price = 25
count = int(input("请输入买多少本书："))
consum = book_price * count * 0.45 + 3 + (count-1) * 0.5
result = book_price * count *(1-0.45)
print("买书共花费%.2f钱，马云亏了%.2f钱"%(consum,result))