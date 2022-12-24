from PIL import ImageGrab
import datetime
import os
from Logger import write_log


# from ResponseOcr import get_words


def make_screenshot(x1, y1, x2,y2):
    """截图

    :param x1: 开始截图的x1坐标
    :param y1: 开始截图的x1标
    :param x2: 开始截图的x2坐标
    :param y2: 结束截图的y2坐标
    :return: 保存图片的名称和文件路径
    """
    try:
        '''
        输入的参数有误则抛出异常
        '''
        if x2 <= 1920 and y2 <=1080:
            images = (x1, y1, x2, y2)
            images = ImageGrab.grab(images)
        else:
            print("截图范围超过屏幕最大分配率，默认分辨率为1920*1080")
    except (UnboundLocalError,ValueError,NameError) as e:
        print(e)
    # 获取当前路径的位置
    path = os.getcwd()
    images_path = path + "\images"
    write_log(20,images_path)
    # 如果文件夹不存在则创建个文件夹
    if not os.path.exists(images_path):
        os.mkdir(images_path)
    else:
        pass
    # 当前时间并且转化为年月日时分秒
    now_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    # 图片名称
    images_name = now_time
    try:
        images.save(images_path + r"\{}.png".format(images_name))
    except (AttributeError,UnboundLocalError):
        print("images对象没有截取到图片，请检查")
    return images_path + r"\{}.png".format(images_name)


