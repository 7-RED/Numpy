year = int(input("輸入年份: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} 是閏年".format(year))
       else:
           print("{0} 不是潤年".format(year))
   else:
       print("{0} 是潤年".format(year))
else:
   print("{0} 不是潤年".format(year))
