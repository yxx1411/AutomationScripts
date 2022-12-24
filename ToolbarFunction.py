# toolbar 工具栏中的属性
toolbar = Aliases.Hsp.frmMain.panel_fill_content.extTabStrip1.Nto_His_DrugInOut_UI_Controls_ucInOutManage.BaseFormNew.panelToolBar.toolBar1

'''
点击HIS系统中工具栏的方法，通过文字识别返回对应的文字位置，点击对应的位置内容
'''
from Logger import write_log
from ResponseOcr import response_OCR
from ScreensShot import make_screenshot


def click_toolbar_words(keysWords):
    # 截图
    # x1,y1,x2,y2 工具栏中的坐标
    x1, y1, x2, y2 = 102, 70, 1200, 105
    keywords = keysWords
    fp = make_screenshot(x1, y1, x2, y2)
    try:
        if object == None or keysWords == None:
            write_log(40, "click_toolbar_words(object,keywords)传入的值为空!")
    except ValueError:
        write_log(40, "click_toolbar_words(object,keywords)传入的值有误!")
    position = get_world_position(fp, keywords)
    x = position[0]
    y = position[1]
    toolbar.Click(x, y)


def get_world_position(fp, keywords):
    '''
    通过输入关键字，在图片中获取到位置
    :param images: 图片路径
    :param words: 输入的关键字
    :return: 返回关键字所在的位置二维坐标
    '''
    result = response_OCR(fp, 2)
    result = result["words_result"]
    print(result)
    for every_dict in result:
        # 判断迭代出来的字典中是否有与关键字匹配的值
        if every_dict["words"] == keywords:
            # 获取该字典中的location中的值
            location = every_dict["location"]
            x1 = location["left"]
            y1 = location["top"]
            x2 = location["left"] + location["width"]
            y2 = location["top"] + location["height"]
            X = round((x1 + x2) / 2)
            Y = round((y1 + y2) / 2)
            print(X, Y)
            return X, Y
        else:
            write_log(30, "没有找到与之匹配的keywords")


def main():
    click_toolbar_words("查询")


def words_analysis(text):
    """
    传入药品的系统规格，解析出基本剂量、剂量单位、包装数量、最小单位、包装单位、体积浓度
    基本剂量：basic_nums
    剂量单位：basic_unit
    包装数量：pack_nums
    最小单位：small_unit
    包装单位：pack_unit
    体积浓度：volume
    :param text: 传入的系统参数
    :return: None
    """
    # 提取体积浓度
    # 判断是否有":"
    str = "："
    char = " "
    line = text
    try:
        if str in line:
            # 体积浓度
            nums = line.find(str)
            volume = line[0:nums]  # 体积浓度

            # 基本剂量
            start_nums = line.find(str)
            end_nums = line.find(char)
            basic_nums = line[start_nums + 1:end_nums]

            KeywordTests.DrugInfoEdit.Variables.Volume = volume
            KeywordTests.DrugInfoEdit.Variables.BasicNums = basic_nums


        else:
            # 基本剂量
            end_nums = line.find(char)
            basic_nums = line[:end_nums]

            KeywordTests.DrugInfoEdit.Variables.BasicNums = basic_nums

    except:
        pass

    finally:

        # 剂量单位
        end_units = line.find("×")  # 找到×号的位置
        basic_unit = line[end_nums + 1:end_units]

        # 包装数量 pack_nums
        end_packnums = line.rfind(char)
        pack_nums = line[end_units + 1:end_packnums]

        # 最小单位small_unit
        end_small_nums = line.find("/")
        small_unit = line[end_packnums + 1:end_small_nums]

        # 包装单位
        pack_unit = line[end_small_nums + 1:]

        KeywordTests.DrugInfoEdit.Variables.BasicUnit = basic_unit
        KeywordTests.DrugInfoEdit.Variables.PackNums = pack_nums
        KeywordTests.DrugInfoEdit.Variables.SmallUnit = small_unit
        KeywordTests.DrugInfoEdit.Variables.PackUnit = pack_unit
