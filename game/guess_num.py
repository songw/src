import random
import math

# 随机生成的数
random_num = random.randint(1, 100)
# 输入猜测的数字
guess_num = int(input("请输入你猜测的 0 ~ 100 之间的数字："))

while True:
    if guess_num > random_num:
        guess_num = int(input("你猜的数字过大，请继续猜："))
    elif guess_num < random_num:
        guess_num = int(input("你猜的数字过小，请继续猜："))
    else:
        print("恭喜你，猜对了！", guess_num)
        break
