from pykeyboard.windows import PyKeyboard

from pymouse import *

hsp = Aliases.Hsp
baseFormNew = hsp.frmMain.panel_fill_content.extTabStrip1.Nto_His_DrugInOut_UI_Controls_ucInOutManage.BaseFormNew
ucInOutManage = baseFormNew.panel1.panelMain.ucInOutManage

mouse = PyMouse()
keys = PyKeyboard()


class WriteDrugOrder(object):
    """
    这是一个专门解决药房药库中XML中，不能输入类型
    通过单元格位置来进行定位
    """

    def write_drugName(self, y, DrugName):
        mouse.click(350, y)
        keys.type_string(DrugName)

    def write_batchNo(self, x, y, BatchNo):
        mouse.click(x, y)
        keys.type_string(BatchNo)

    def write_applynums(self, x, y, ApplyNums):
        mouse.click(x, y)
        keys.type_string(ApplyNums)

    # 采购入库中的生产批号 (850,250)
    def write_PbatchNo(self, y, PBnumber):
        mouse.click(750, y)
        keys.type_string(PBnumber)

    # 采购入库中的申请数量
    def write_Pnums(self, y, Pnums):
        mouse.click(1366, y)
        keys.type_string(Pnums)

    # 采购入库中的药品名称
    def write_PdrugName(self, y, PDrugName):
        mouse.click(250, y)
        keys.type_string(PDrugName)

    # 采购入库中的有效期
    def write_Pend_time(self, y, Ptime):
        mouse.click(930, y)
        keys.type_string(Ptime)

    # 盘盈、盘亏中的ＸＭＬ相关药品名称
    def write_AdrugName(self, y, AdrugName):
        mouse.click(230, y)
        keys.type_string(AdrugName)
        OCR.Recognize(ucInOutManage.panelDrugTerm.ucDrugOption.fpDrugList).BlockByText("注射用青霉素钠").DblClick()

    # 盘盈、盘亏中的批次号 (850,250)
    def write_AbatchNumber(self, y, PbatchNumber):
        mouse.click(1030, y)
        keys.type_string(PbatchNumber)

    # 单位
    def write_Anuits(self, y, Anuits):
        mouse.click(1404, y)

    #        OCR.Recognize(ucInOutManage.panelDrugTerm.ucDrugOption.fpDrugList).BlockByText("*" + Anuits + "*" ).DblClick()
    # keys.type_string(Anuits)
    # 盘盈、盘亏的申请数量
    def write_AapplyNums(self, y, AapplyNums):
        mouse.click(1560, y)
        keys.type_string(AapplyNums)
