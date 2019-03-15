'''
这是一个计算器演示程序
'''

op_type = {
    '1': '加法',
    '2': '减法',
    '3': '乘法',
    '4': '除法'
}


def add(a, b):
    return a + b


def sbutract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    assert b != 0
    return a / b


def print_menu():
    print('1.加法')
    print('2.减法')
    print('3.乘法')
    print('4.除法')
    print('\n')


if __name__ == '__main__':
    while True:
        print('\n\n开启计算模式\n\n')
        print_menu()

        menu_str = input('请输入菜单指令...')
        if menu_str not in ['1', '2', '3', '4']:
            print('\n\n 请输入正确指令!!!')
            continue

        print('你选择了%s运算' % op_type[menu_str])

        input_a = input('请输入第一个参数 a: ')
        input_a = int(input_a)
        print('收到参数a:', input_a)

        input_b = input('请输入第二个参数 b: ')
        input_b = int(input_b)
        print('收到参数b:', input_b)

        print('运算结果: ')

        if menu_str == '1':
            print(add(input_a, input_b))
            continue
        if menu_str == '2':
            print(sbutract(input_a, input_b))
            continue
        if menu_str == '3':
            print(multiply(input_a, input_b))
            continue
        if menu_str == '4':
            print(divide(input_a, input_b))
            continue
