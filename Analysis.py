def find_word(text):
    '''

    :param text: 药品规格数据
    :return:
    '''
    nums = text.find(" ")     #查询出规格中空格
    materials = text[:nums]
    spec = text[nums+1:]
    KeywordTests.InfoCheck.Variables.materials = materials
    KeywordTests.InfoCheck.Variables.spec = spec
    
    return materials,spec