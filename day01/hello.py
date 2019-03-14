"""
这是一个模块注释
"""
# 导入模块
import os

# 定义全局变量
g_var = 100


# 这是一个类
class FooClass(object):
    # __init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
    #
    # 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：

    def __init__(self, a, b):
        self.a = a
        self.b = b

    _num = 'nihao'
    num = '公开的'

    def add(self):
        return self.a + self.b


def add_fun(a, b):
    '''
    加法函数
    :param a:
    :param b:
    :return:
    '''
    print('这是a:' + str(a))
    print('这是b:' + str(b))
    return a + b


def debug_demo():
    a = 2
    b = 4
    c = a + b
    print(c)
    return c


def get_current_path():
    path = os.path.abspath('./hello.py')
    return path


def paixu(list):
    for i in range(0, len(list), 1):
        print(list, i)
        for j in range(0, i, 1):
            if list[j] <= list[j + 1]:
                continue
            temp = list[j]
            list[j] = list[j + 1]
            list[j + 1] = temp
            print(list, i)
            # if i == len(list)-1:
            #     print(list)


def chengfabiao():
    for i in range(1, 10, 1):
        for j in range(1, i + 1, 1):
            print(str(i) + '*' + str(j) + '=' + str(i * j), end=' ')
        print(' ')


def jidan():
    for i in range(1, 1000):
        if (i % 4 == 1):
            if (i % 5 == 4):
                if (i % 6 == 3):
                    if (i % 7 == 5):
                        if (i % 8 == 1):
                            if (i % 9 == 0):
                                print(i)

def jidan2():
    for i in range(1, 1000):
        if i%4!=1:
            continue
        if i % 5 != 4:
            continue
        if i % 6 != 3:
            continue
        if i % 7 != 5:
            continue
        if i % 8 != 1:
            continue
        if i % 9 != 0:
            continue
        print(i)


if __name__ == '__main__':
    list = [5, 12, 2, 1, 4, 66]
    # paixu(list)
    # chengfabiao()
    jidan2()

    # print('Holle Word')
    # debug_demo()
    # c = add_fun(1,8)

    # num = input("请输入一个整数：")
    # a= input()
    # print(a)
    # file = open("a.text","w")
    # for i in range(20):
    #     file.write('nihao\n\r')
    # print(c)
    # print(get_current_path())
