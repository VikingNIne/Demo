﻿import random

print('------------------我爱鱼C工作室------------------')

times = 3
secret = random.randint(1,10)
guess = 0

print("不妨猜一下小甲鱼现在心里想的是哪个数字：", end=" ")

while (guess != secret) and (times > 0):
    temp = input()
    guess = int(temp)
    times = times - 1 # 用户每输入一次，可用机会就-1
    if guess == secret:
        print("哇哦，你是小甲鱼心里的蛔虫吗？！")
        print("哼，猜中了也没有奖励！")
    else:
        if guess > secret:
            print("哥，大了大了~~~")
        else:
            print("嘿，小了，小了~~~")
        if times > 0:
            print("再试一次吧：", end=" ")
        else:
            print("机会用光咯T_T")
            
print("游戏结束，不玩啦^_^")