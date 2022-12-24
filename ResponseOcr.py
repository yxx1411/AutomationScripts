# encoding:utf-8
# from aip import AipOcr

import base64
import os
import requests

from Logger import write_log
from ScreensShot import make_screenshot

""" 你的 APPID AK SK """
APP_ID = '26990936'
API_KEY = 'kZwvGwPcw4s5MNIXA968Y9nH'
SECRET_KEY = 'av8SAnN3VWZ5Un3fUpH4S5wBw4X9G8Er'

# client_id 为官网获取的AK， client_secret 为官网获取的SK


get_url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials"
client_id = API_KEY
client_secret = SECRET_KEY


def get_token():
    host = get_url + "&" + "client_id=" + API_KEY
    host = host + "&" + "client_secret=" + SECRET_KEY
    response = requests.get(host)
    get_json = response.json()
    access_token = get_json.get("access_token")
    return access_token


'''
通用文字识别（高精度含位置版）
'''


def response_OCR(path_images, mode=1):
    """

    :param path_images: 图片的路径
    :param mode: 识别的模式，mode默认为1 mode=1 通用识别，不返回文字的位置  mode = 2 高精度识别，返回位置
    :param gap:是否定位单字符位置，big:不定位单字符位置，默认值; small:定位单字符位置
    :return: 返回识别的结果，json格式的结果
    """
    # 请求的URL
    if mode == 1:
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    elif mode == 2:
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate"
    else:
        raise ValueError

    path = os.getcwd()
    # \Script
    write_log(20, path)
    write_log(20, "截图所在的位置：{}".format(path_images))
    # f = open(path_images, 'rb')
    # img = base64.b64encode(f.read())
    # params = {"image": img}

    with open(path_images, "rb") as f:
        image = base64.b64encode(f.read())

    body = {
        "image": image,
        "language_type": "auto_detect",
        "recognize_granularity": "big",
        "detect_direction": "true",
        "vertexes_location": "true",
        "paragraph": "true",
        "probability": "true",
    }

    access_token = get_token()
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=body, headers=headers)

    if response:
        get_data = response.json()
        write_log(20, get_data)
        print(get_data)
        return get_data


