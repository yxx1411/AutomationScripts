import cx_Oracle as cx
from Logger import write_log

# .........................
# 连接Oracle数据库的账号密码
# .........................

# User = "hsp_md_1019_2"
# Password = "hsp_md_1019_2"
# Con = "192.168.5.224:1521/ORCL"


User = "testdyhis"
Password = "testdyhis"
Con = "172.15.50.240/ORCL"


def connect_oracle(User, Password, Con):
    con = cx.connect(User, Password, Con)
    cursor = con.cursor()
    return cursor


def excute_sql(sql):
    # .............................................................................................................................
    # 目的：执行传入的SQL语句
    # 输入的参数：db_config的配置信息 sql:需要执行的SQL语句
    # 返回结果：返回查询的结果
    # 注意事项：
    # 作者：杨继宏
    # 创建时间：2022-7-26
    # ..............................................................................................................................
    cursor = connect_oracle(User, Password, Con)
    cursor.execute(sql)  # 执行sql语句
    data = cursor.fetchone()  # 获取一条数据
    data = data[0]

    return data


def find_facname(facname):
    """
    传入厂家名称，查看库中是否已有厂家存在
    :param facname: 厂家名称
    :return: 从表中查询出来的厂家
    """
    cursor = connect_oracle(User, Password, Con)
    cursor.execute(
        "SELECT FAC_NAME FROM  D_COMPANY WHERE FAC_NAME = '{}' AND COMPANY_TYPE='0' AND HOS_ID = '0105'".format(facname)
    )  # 执行sql语句
    data = cursor.fetchone()  # 获取一条数据
    try:
        # 提取获取的数据
        data = data[0]
    except TypeError:
        return None
    return data


def find_PATIENT_NO(ID):
    """
    传入厂家名称，查看库中是否已有厂家存在
    :param facname: 厂家名称
    :return: 从表中查询出来的厂家
    """
    cursor = connect_oracle(User, Password, Con)
    cursor.execute(
        "SELECT PNAME,INPATIENT_ID,PATIENT_NO,CLIENT_ID,CERTIFICATE_NO FROM F_IP_INMAININFO WHERE CERTIFICATE_NO = '{}'".format(
            ID)
    )  # 执行sql语句
    data = cursor.fetchone()  # 获取一条数据
    write_log(20, data)
    return data
