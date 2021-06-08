hour=int(input("輸入幾點(24小時制)："))
minute=int(input("輸入幾分："))

if(minute>=10 or minute==0):
    if(hour>=8 and hour<=11):
        print("現在是第{0}節".format(hour-7))
    elif(hour>=12 and hour<=23):
        print("現在是第{0}節".format(hour-8))
else:
    print("現在不是上課時間")
