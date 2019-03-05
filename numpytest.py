import numpy
import pandas
import lxml

x=numpy.array([11,22,33,4,5,6,7,])  #创建一维数组
x2=numpy.array([['asfas','asdfsdf','dfdf',11],['1iojasd','123',989012],["jhyfsdaeku","jhgsda"]])    #创建二维数组,注意是([])

a = x.sort()   #排序，没有返回值的，修改原处的值，这里等于修改了X
# print(a)
b = x.max()    # 最大值，对二维数组都管用
# print(b)
c = x.min()    # 最小值，对二维数组都管用
# print(c)
x1=x[1:3]   # 取区间，和python的列表没有区别
# print(x1)

#numpy.random.random_integers(最小值,最大值,个数)  获取的是正数
data = numpy.random.random_integers(1,20000,30)   #生成整形随机数
# print(data)
#正态随机数  numpy.random.normal(均值,偏离值,个数)  偏离值决定了每个数之间的差 ,当偏离值大于开始值的时候，那么会产生负数的。
data1 = numpy.random.normal(3.2,29.2,10)    # 生成浮点型且是正负数的随机数
# print(data1)



a=pandas.Series([1,2,3,34,])   # 等于一维数组
b=pandas.DataFrame([[1,2,3,4,],["sdaf","dsaf","18hd"],[1463]])   # 二维数组
# print(b)
# print(b.head())  # 默认取头部前5行,可以看源码得知
# print(b.head(2))  # 直接传入参数，如我写的那样
# print(b.tail())   # 默认取尾部前后5行
# print(b.tail(1))     # 直接传入参数，如我写的那样
# print(b.describe()) # 显示统计数据信息
# print(b.T)   # 转置

html_from_online = pandas.read_html('https://book.douban.com/')  # 读取互联网的html文件
# print(html_data)
print(html_from_online)