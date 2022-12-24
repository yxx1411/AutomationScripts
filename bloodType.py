import random

from Logger import write_log


def get_bloodType():
    """
       随机选择血型
        :return:
    """
    blood_list = ["A型", "B型", "O型", "AB型"]
    bloodType = random.choice(blood_list)
    write_log(20, bloodType)
    return bloodType
