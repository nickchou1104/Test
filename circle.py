n=int(input("請輸入總人數: "))
m=int(input("請規定報到數字幾的人退出圈子: "))
circle=[]
for i in range(1, n+1):
        circle.append(i)
num=1
while len(circle)!=1:
        circle.append(circle.pop(0))
        num+=1
        if num==m:
            del circle[0]
            num=1
print("最後留下的人是原來第{}號的人".format(*circle))