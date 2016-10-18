NUM = 5
num = input("请输入你认为输入对的数：")
while int(num) != NUM:
    num = input("输入的不对，请重新输入：")
print("恭喜你输入对啦"+str(NUM))