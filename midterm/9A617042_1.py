year=int(input("輸入西元："))
month=int(input("月份："))
day=int(input("日期："))
if(month>2 and month<9):
    print("{0}/{1}/{2}為第二學期".format(year-1912,month,day))
elif(month==1):
    print("{0}/{1}/{2}為第一學期".format(year-1912,month,day))
else:
    print("{0}/{1}/{2}為第一學期".format(year-1911,month,day))
