"""
    这里存放的是基础方法
"""
from Logger import write_log
from ResponseOcr import response_OCR
from ScreensShot import make_screenshot


def get_text(text):
    """
    从截取的图片中解析出想要的文字
    :param text: 文字识别接口返回的词
    :return: target_words:目标词汇
    """
    try:
        text = dict(text)
        words = text["words_result"]
        words = words[0]
        target_words = words["words"]
        return target_words

    except IndexError:
        write_log(20, "OCR接口没有识别到文字，返回的文字为空")
        pass


def ocr_words(x1, y1, x2, y2):
    img = make_screenshot(x1, y1, x2, y2)
    text = response_OCR(img)
    text = get_text(text)
    write_log(20, text)
    #    KeywordTests.FactoryInfoEdit.Variables.FactoryName = text
    return text


def main():
    ocr_words(190, 218, 515, 249)
