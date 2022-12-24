import logging
import os
import time
from datetime import datetime, date, timedelta


def write_log(grade, info):
    # 获取今天的日期
    today_date = time.strftime("%Y-%m-%d", time.localtime())
    # 设置日志的输出格式
    LOG_FORMAT = "运行时间：%(asctime)s  - 日志等级：%(levelname)s - 日志信息：%(message)s"
    # 获取当前路径的位置
    PATH = os.getcwd()
    log_path = PATH + "/Script/Log"
    make_file(log_path)
    LOG_PATH = log_path + '/' + today_date + ".log"
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, filename=LOG_PATH)
    logging.log(grade, info)
    return


def make_file(fp, filename=None):
    """
  判断文件路径是否存在，若不存在则创建
  :param fp: 文件的路径
  :param filename: 文件名称
  :return:None
  """
    file_path = fp
    if os.path.exists(file_path):
        return
    else:
        os.makedirs(file_path)
    return
