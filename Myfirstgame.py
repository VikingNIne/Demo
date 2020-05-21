"""用python设计第一个游戏"""
"""
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
guess = int(temp)

if guess == 9:
    print ("恭喜你猜对了！你太厉害了")
    b=false
else:
    print("你猜错了！再来一次吧!")

第二讲作业
cj =input("输入你的成绩：")
zcj = int(cj)
if zcj==100:
    print("好棒，你离女神又近了一步^_^")
else:
    print("小子，想要幸福，就得努力！")

第三讲作业
dpy = 365
hpd = 24
mph = 60
spm = 60
spy=dpy*hpd*mph*spm
print(spy,"\a")

name = input("请输入你的姓名：")
print("你好",name,sep=",",end="!")

第四讲作业
print("D:\three\two\one\now")
print(r"D:\three\two\one\now")

fishc=r
      ___                     ___          ___          ___     
     /\  \         ___       /\  \        /\__\        /\  \    
    /::\  \       /\  \     /::\  \      /:/  /       /::\  \   
   /:/\:\  \      \:\  \   /:/\ \  \    /:/__/       /:/\:\  \  
  /::\~\:\  \     /::\__\ _\:\~\ \  \  /::\  \ ___  /:/  \:\  \ 
 /:/\:\ \:\__\ __/:/\/__//\ \:\ \ \__\/:/\:\  /\__\/:/__/ \:\__\
 \/__\:\ \/__//\/:/  /   \:\ \:\ \/__/\/__\:\/:/  /\:\  \  \/__/
      \:\__\  \::/__/     \:\ \:\__\       \::/  /  \:\  \      
       \/__/   \:\__\      \:\/:/  /       /:/  /    \:\  \     
                \/__/       \::/  /       /:/  /      \:\__\    
                             \/__/        \/__/        \/__/

print(fishc)

for i in range(1,10):
    for j in range(1,i+1):
        print(i,"X",j,"=",i*j,end='    ')
    print('\n')

第五讲作业

num1 = int(input("请输入第一个整数："))
num2 = int(input("请输入第二个整数："))

if num1 < num2:
    print("第一个数比第二个数小！")
elif num1 > num2:
    print("第一个数比第二个数大！")
elif num1 == num2:
    print("第一个数和第二个数一样大！")

第六讲作业
用Python设计第一个游戏 
    
counts = 3
    
while counts > 0:
    temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
    guess = int(temp)
    if guess == 8:
        print("你是小甲鱼心里的蛔虫嘛？！")
        print("哼，猜中了也没奖励！")
    else:
        if guess < 8:
            print("小啦~")
        else:
            print("大啦~")
    counts = counts - 1
    
x = input("请输入你的成绩：")
while x!='e':
    x = int(x)
    if x==100:
        print("S")
    elif x>=90 and x<100:
        print("A")
    elif x>=80 and x<90:
        print("B")
    elif x>=60 and x<80:
        print("C")
    elif x<60:
        print("D")
    x = input("请输入你的成绩：")
第七讲作业
import random
print(random.randrange(0,99,2))
numberOne = random.randint(1,33)
numberTwo = random.randint(1,33)
numberThree = random.randint(1,33)
numberFour = random.randint(1,33)
numberFive = random.randint(1,33)
numberSix = random.randint(1,33)
numberBlue = random.randint(1,16)
print(numberOne,numberTwo,numberThree,numberFour,numberFive,numberSix,numberBlue,sep=",")

第八讲作业
import random
a = random.randint(0,1)
i = 0
count=input("请输入抛硬币次数：")
j=0
while i<int(count):
    if j>5:
        print()
        j=0
    a = random.randint(0,1)
    if a==0:
        print("正面",end="   ")
        j +=1
    else:
        print("反面",end="   ")
        j +=1
    i +=1
"""
i = 0

while i <= 100:
    if i % 2 == 0:
        print(i, "是偶数！")
    i = i + 1







