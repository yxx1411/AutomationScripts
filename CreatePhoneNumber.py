import random


# 随机生产手机号码
def createPhone():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152", "153",
               "155", "156", "157", "158", "159", "186", "187", "188"]
    PhoneNumber = random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))
    Project.Variables.PhoneNumber = PhoneNumber  # 身份证ID设置为全局变量
    return PhoneNumber
