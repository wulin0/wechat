# This is a sample Python script.
from time import sleep

import itchat
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 生成对象
    myself = itchat.new_instance()

    # 登录
    itchat.login()
    # 获取好友列表
    friends = itchat.get_friends(update=True)[0:]
    # 遍历输出好友列表
    for friend in friends:
        print(friend)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
