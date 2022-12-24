'''
这是一个文字处理的模块，从百度OCR接口中返回带位置的文字数据，判断是否是一个词，并且返回该词语的x,y值
'''


class Operation:
    def __init__(self, text):
        self.text = text

    def get_list(self):
        '''
        传入的text经过处理获得三个列表
        :return: 返回长度相同的三个列表
        '''
        # 分别对数据中的值创建5个不同的列表
        char_list = []
        top_list = []
        left_list = []
        width_list = []
        height_list = []

        words_results = self.text["words_result"]

        # 迭代出数据中的有多少行数据
        for result in words_results:
            rows = result['chars']
            for item in rows:
                chars, location = item["char"], item["location"]
                top, left, width, height = location["top"], location["left"], location["width"], location["height"]
                char_list.append(chars)
                top_list.append(top)
                left_list.append(left)
                width_list.append(width)
                height_list.append(height)

        # 变换为一个二位坐标
        x_list = []  # 创建一个空的列表
        y_list = []  # 创建一个空的列表

        for nums in range(0, len(left_list)):
            x_list.append(left_list[nums] + round(width_list[nums] / 2))
            y_list.append(top_list[nums] + round(height_list[nums] / 2))

        return char_list, x_list, y_list

    def remove_word(self):
        '''
        通过char中的坐标值来去重，若列表中两个词x值和y值相等，则表示重复
        :return: 去重以后的三个列表
        '''
        # 创建三个空列表
        remove_words = []
        remove_x = []
        remove_y = []

        words = ['查询', '保存', '打印', '设置', '打印设置', '预览', '导出']
        # 迭代出相关数据
        rows = self.get_list()
        chars, x, y = rows[0], rows[1], rows[2]  # 获得三个列表

        for i in range(0, len(chars) - 1):  # i表示迭代的索引
            # 判断chars表中相联字符是否一致
            if chars[i] != chars[i + 1]:
                remove_words.append(chars[i])
                remove_x.append(x[i])
                remove_y.append(y[i])
        # 加上列表中末尾的词
        remove_words.append(chars[len(chars) - 1])
        remove_x.append(x[len(x) - 1])
        remove_y.append(y[len(y) - 1])

        print(remove_words)
        print(remove_x)
        print(remove_y)
        print(len(remove_x))
        return remove_words, remove_x, remove_y

    def del_chars(self):
        # 去除无效词语
        rows = self.remove_word()
        chars = rows[0]
        x = rows[1]
        y = rows[2]
        char = []
        X_list = []
        Y_list = []
        for i in range(0, len(x) - 2):
            left_word = x[i]
            right_word = x[i + 1]
            if right_word - left_word < 15 and y[i] == y[i + 1]:
                char.append(chars[i])
                char.append(chars[i + 1])
                X_list.append(x[i])
                X_list.append(x[i + 1])
                Y_list.append(y[i])
                Y_list.append(y[i + 1])

        print("============================================================================")
        print(char)
        print(X_list)
        print(Y_list)
        print(len(char))
        print(len(X_list))
        print(len(Y_list))

        new_x_list = []
        new_char_list = []
        new_y_list = []
        for x in range(0, len(X_list)):
            if X_list[x] not in new_x_list:
                new_x_list.append(X_list[x])
                new_char_list.append(char[x])
                new_y_list.append(Y_list[x])

        return new_char_list, new_x_list, new_y_list
        print('----------------new list ----------------------------')
        print(len(new_x_list))
        print(len(new_char_list))
        print(len(new_y_list))

    def make_word(self):
        rows = self.del_chars()
        chars = rows[0]
        x = rows[1]
        y = rows[2]
        n = 2
        # 创建一个列表用来存放xy值
        group_xy = []
        regroup = []
        regroup_xy = []
        group_chars = []
        str = ''

        # 获得一个组合以后的列表
        for i in range(0, len(x)):
            group_xy.append(x[i])
            group_xy.append(y[i])

        for xy in [group_xy[i:i + n] for i in range(0, len(group_xy), n)]:
            regroup.append(xy)

        for midxy in [regroup[i:i + n] for i in range(0, len(regroup), n)]:
            regroup_xy.append(midxy)

        # 分割成两个字的词
        for char in [chars[i:i + n] for i in range(0, len(chars), n)]:
            newwords = str.join(char)
            group_chars.append(newwords)

        print('--------------------------')
        print(group_chars)
        print(regroup_xy)
        return group_chars, regroup_xy

    def calculate_xy(self, xy):
        '''
            计算出两个字坐标的中心位置
        :param ls:
        :return:
        '''
        # rows = self.make_word()
        location = xy
        calc_list = []
        calc_height = []
        for item in location:
            calc_list.append(item[0])
            calc_height.append(item[1])

        # x1 + x2
        value_x = sum(calc_list) / len(calc_list)
        mid_xy = round(value_x)
        value_y = sum(calc_height) / len(calc_height)
        mid_height = round(value_y)
        print('------------------------')
        print(mid_xy, mid_height)
        return mid_xy, mid_height

    def gorup_words(self):
        words = ['查询', '保存', '打印', '设置', '打印设置', '预览', '导出']
        rows = self.make_word()
        newchar_list = rows[0]
        xy_list = rows[1]
        print("---------------------TTTTTTTTTTTTTTTT--------------------")
        print(newchar_list)
        keywords = '设置'
        for index, keys in enumerate(newchar_list):
            if keys in words:  # 判断组成的新词是否在词库中
                if keywords == keys:
                    xy = xy_list[index]
                    self.calculate_xy(xy)
                else:
                    pass
            continue
