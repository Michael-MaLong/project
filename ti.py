import calendar
import time
day_now = time.localtime()
day_begin = '%d-%02d-01' % (day_now.tm_year, day_now.tm_mon)  # 月初肯定是1号
wday, monthRange = calendar.monthrange(day_now.tm_year, day_now.tm_mon)  # 得到本月的天数 第一返回为月第一日为星期几（0-6）, 第二返回为此月天数
print(monthRange)
day_end = '%d-%02d-%02d' % (day_now.tm_year, day_now.tm_mon, monthRange)
print('月初日期为：',day_begin, '月末日期为：',day_end)
