pay = 3.1415926


def longs(dell: float):
    return dell * 2 * pay


def mianji(dell: float):
    return dell ** 2 * pay


def get_sum():
    while True:
        jsfhhs = input("请输入半径:")
        try:
            dell = float(jsfhhs)
            return dell
        except:
            print("阿弧度无效")


if __name__ == '__main__':
    dell =get_sum()
    print('=圆的周长为：%.2f'%longs(dell))
    print('圆的面积为:%.2f'%mianji(dell))