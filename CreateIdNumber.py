import os
import random
import datetime

# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# BASE_DIR = os.path.dirname()
# 获取当前目录
path = os.getcwd()
DC_PATH = path + r"\Script\districtcode.txt"

Log.Message(DC_PATH)

mon = ("01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
days = (
"01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
"21", "22", "23", "24", "25", "26", "27", "28")


# 地区代码存放的路径


def create_ID():
    with open(DC_PATH) as file:
        data = file.read()
        districtlist = data.split(',')

    districtlistCode = districtlist[random.randint(0, len(districtlist))]  # 地区代码
    birthday = random.randint(1945, 2020)  # 出生年份
    monAndDays = datetime.date.today() + datetime.timedelta(days=random.randint(1, 366))  # 月份和日期项
    monAndDays = monAndDays.strftime('%m%d')
    # nums = str(random.randint(100,300))#，顺序号
    nums = str(100)  # ，顺序号

    # print(districtlistCode)

    id = str(districtlistCode) + str(birthday) + monAndDays + nums

    i = 0
    count = 0
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
    checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '4', '9': '3',
                 '10': '2'}  # 校验码映射
    print(len(id))
    print(id[1])
    for i in range(0, len(id)):
        count = count + int(id[i]) * weight[i]
    #    Log.Message(count)
    checkcode = checkcode[str(count % 11)]  # 算出校验码
    id = id + checkcode
    Project.Variables.IdCard = id  # 身份证ID设置为全局变量
    return id
