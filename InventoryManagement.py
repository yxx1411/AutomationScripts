from time import sleep

from Config import excute_sql
from Logger import write_log
from WriteOrder import WriteDrugOrder

hsp = Aliases.Hsp
baseFormNew = hsp.frmMain.panel_fill_content.extTabStrip1.Nto_His_DrugInOut_UI_Controls_ucInOutManage.BaseFormNew
# TXToolStrip = baseFormNew.panelToolBar.toolBar1


# 顶端界面的按钮参数
top_title = hsp.frmMain.panel_top_title.extPannel1.pnlRole

# 底端的科室选择框
bottom_status = hsp.frmMain.panel_bottom_status.tcbDept

# 左侧菜单栏
left_panel = hsp.frmMain.panel_fill_content.extPannel3.txMenuStrip1

# 入出库类型操作类型
operation_type = baseFormNew.panel1.panelMain.ucInOutManage.panelDrugInOut.panelHead.cmbOperType

# 入出库关系维护界面中目标科室
target_department = baseFormNew.panel1.panelMain.ucInOutManage.panelDrugInOut.panelInOut.extGroupBox2.cmbTarget

# 选择框
select_box = hsp.ToolStripDropDown.DataGridView

# 工具栏
tool_bar = baseFormNew.panelToolBar.toolBar1

# 入出库关系维护界面中的查询按钮
btn_query = hsp.frmQueryDrugApplyOut.pnlMain.extSplitContainer1.SplitterPanel2.btnQuery

# 检索药品出库申请记录
splitter_panel = hsp.frmQueryDrugApplyOut.pnlMain.extSplitContainer1.SplitterPanel2

# 检索药品入库记录
splitterPanel = hsp.frmQueryDrugInputApply.pnlMain.extSplitContainer1.SplitterPanel

# 订单面板
order_panel = baseFormNew.panel1.panelMain.ucInOutManage.panelDrugInOut.panelInOut.panelInOutFp.panelFpInOut.fpInOut

# 自定义控件XML输入框
ucInOutManage = baseFormNew.panel1.panelMain.ucInOutManage
extFarpoint = ucInOutManage.panelDrugInOut.panelInOut.panelInOutFp.panelFpInOut.fpInOut
inputTextBox = extFarpoint.GeneralEditor.InputTextBox

# 弹框的提示
MessageBox = Aliases.Hsp.FrmMessageBox


def close_messagebox():
    try:
        if MessageBox.Exists:
            OCR.Recognize(MessageBox).BlockByText("确定", spLeftMost).Click()
            sleep(3)
    except (AttributeError):
        Log.Message("Attribute does not exist!")


def into_pages(MenuPages):
    '''
    :param MenuPages: 界面顶部栏目菜单 如药房管理
    :return:
    '''

    if MenuPages not in ('门诊医生', '门诊收费', '药库管理', '药房管理'):
        Pages = {
            '门诊医生': '01-门诊医生',
            '信息维护': '02-信息维护',
            '财务管理': '03-财务管理',
            '固定资产管理': '04-固定资产管理',
            '门诊护士': '06-门诊护士',
            '住院收费': '10-住院收费',
            '药房管理': '01-门诊医生',
            '下拉框': 'label_menu',
            '住院护士': '11-住院护士',
            '住院医生': '12-住院医生',

        }
        for pages_name in Pages:
            if pages_name == MenuPages:
                pages_name = Pages[pages_name]
                top_title.WinFormsObject(pages_name).Click()
            else:
                Log.Message('找选菜单界面中，请等待！')

    else:
        if MenuPages == '门诊医生':
            top_title.z5_.Click()
        elif MenuPages == '门诊收费':
            top_title.z7_.Click()
        elif MenuPages == '药库管理':
            top_title.z8_.Click()
        elif MenuPages == '药房管理':
            top_title.z9_.Click()


def into_menu(ParentMenuNames, MenuNames):
    '''

    :param ParentMenuNames: 左侧栏的大菜单
    :param MenuNames: 对应的子菜单
    :return:
    --药房--
    ParentMenuNames:"药品入出库"
    MenuNames:"药品入出库"
    --药库--
    ParentMenuNames:"入出库管理"
    MenuNames:"药品入出库"
    '''
    OCR.Recognize(left_panel).BlockByText(ParentMenuNames).Click()
    OCR.Recognize(hsp.ToolStripDropDownMenu).BlockByText(MenuNames).Click()

    return Log.Message('进入页面成功！')


def choose_department(DepartmentName):
    '''
    :param DepartmentName: 进入的科室名称
    :return:
    '''
    # 选择进入那个药房的方法

    department_name = bottom_status.WinFormsObject("Edit", "").wText
    if department_name != DepartmentName:
        toolStripDropDown = hsp.ToolStripDropDown
        bottom_status.Click(211, 13)
        toolStripDropDown.ExtComboBox.SetText(DepartmentName)
        select_box.ClickCell(0, "名称")
        Log.Message("打开的是:" + DepartmentName)
    else:
        Log.Message("默认打开的是:" + DepartmentName)


def choose_type(OperationName):
    '''
    选择入出库操作类型
    :return:
    '''
    rows_nums = operation_type.wItemCount  # 下拉框列的数量
    operation_type.Click(194, 14)
    for nums in range(0, rows_nums - 1):
        select_box.ClickCell(nums, "名称")
        data = operation_type.WinFormsObject("Edit", "").wText
        if data == OperationName:
            return Log.Message('选择的操作类型是', data)
        operation_type.Click(194, 14)


def choose_target_department(OperationName, TagrgetDepartment):
    '''
    选择目标科室
    :return:
    '''

    if OperationName not in ('药房-调药核准', '药库-药房申请核准出库'):
        target_department.Click(195, 20)
        select_box.ClickCell(TagrgetDepartment, "名称")
    else:
        Log.Message(OperationName + "不需要选择目标科室")


def execute_operation(Operational):
    '''
    执行的操作类型
    :return:
    '''
    # The beginning of the 执行任务栏中相关操作 group
    # 点击审核按钮

    # ----------------------------------------相关操作的坐标位置----------------------------------------
    # 75,20---查询
    # 160，20---新建
    # 260，20--添加
    # 350，20--暂存
    # 425，20--提交
    # 540，20--审核
    # 645，20--打印
    # 730，20--删除
    # 825，20--设置
    # 890，20--刷新
    # 980，20--打回
    # -----------------------------------------------------------
    # The end of the 执行任务栏中相关操作 group

    if Operational == '查询':
        tool_bar.Click(60, 20)
    elif Operational == '新建':
        tool_bar.Click(120, 20)
    elif Operational == '添加':
        tool_bar.Click(180, 20)
    elif Operational == '暂存':
        tool_bar.Click(260, 20)
    elif Operational == '提交':
        tool_bar.Click(330, 20)
        # 等待弹框出现
    #        while not MessageBox.Exists:
    #            sleep(1)
    elif Operational == '审核':
        tool_bar.Click(400, 20)
    elif Operational == '打印':
        tool_bar.Click(480, 20)
    elif Operational == '删除':
        tool_bar.Click(545, 20)
    elif Operational == '设置':
        tool_bar.Click(620, 20)
    elif Operational == '刷新':
        tool_bar.Click(670, 20)
    elif Operational == '打回':
        tool_bar.Click(750, 20)


def write_order(Submit):
    #   Project.Variables.DrugOrder.Iterator.Reset()
    #   while not Project.Variables.DrugOrder.Iterator.IsEOF():
    # 填写药品名称
    DrugName = Project.Variables.DrugOrder.Iterator.Value["DRUG_SORT_ID"]
    Log.Message(DrugName)
    Delay(1000)
    WriteDrugOrder().write_drugName(250, "txhhd")
    Delay(1000)
    OCR.Recognize(ucInOutManage.panelDrugTerm.ucDrugOption.fpDrugList).BlockByText("1 天仙还魂丹").DblClick()

    # 填写批次号
    BatchNo = Project.Variables.DrugOrder.Iterator.Value["BATCH_NO"]
    Delay(1000)
    WriteDrugOrder().write_batchNo(1040, 248, BatchNo)

    # 填写申请数量
    ApplyNums = Project.Variables.DrugOrder.Iterator.Value["NUMBERS"]
    Delay(1000)
    WriteDrugOrder().write_applynums(1654, 250, ApplyNums)
    Delay(500)
    # 提交申请
    Operational = Submit
    Log.Message(Operational)
    execute_operation(Operational)


def write_call_drugOder(Submit):
    # 书写调药申请的订单
    Delay(1000)
    WriteDrugOrder().write_drugName(250, "ay")
    Delay(1000)
    OCR.Recognize(ucInOutManage.panelDrugTerm.ucDrugOption.fpDrugList).BlockByText("艾叶").DblClick()
    # 填写批次号
    # BatchNo = Project.Variables.DrugOrder.Iterator.Value["BATCH_NO"]
    # Delay(1000)
    # WriteDrugOrder().write_batchNo(1040, 248, BatchNo)
    # # 填写申请数量
    # ApplyNums = Project.Variables.DrugOrder.Iterator.Value["NUMBERS"]
    # Delay(1000)
    ApplyNums = '0.1'
    WriteDrugOrder().write_applynums(1654, 250, ApplyNums)
    Delay(500)
    # 提交申请
    Operational = Submit
    Log.Message(Operational)
    execute_operation(Operational)


def write_purchase_order(Submit):
    y = 250
    PDrugName = "txhhd"
    PBnumber = "testing01"
    Pnums = "5"
    Ptime = "2023/9/9"
    # 填写药品名称
    WriteDrugOrder().write_PdrugName(y, PDrugName)
    OCR.Recognize(ucInOutManage.panelDrugTerm.ucDrugOption.fpDrugList).BlockByText("1 天仙还魂丹").DblClick()
    # 填写生产批次号
    WriteDrugOrder().write_PbatchNo(y, PBnumber)
    # 填写有效期
    WriteDrugOrder().write_Pend_time(y, Ptime)
    # 填写申请数量
    WriteDrugOrder().write_Pnums(y, Pnums)
    Delay(500)
    # 提交申请
    Operational = Submit
    execute_operation(Operational)


def write_Acheck_inventory_add(Submit):
    # 填写药品订单的方法
    AdrugName = "zsyqmsn"
    y = 250
    Anuits = "瓶"
    AapplyNums = "2"
    # 填写药品名称
    WriteDrugOrder().write_AdrugName(y, AdrugName)
    # 填写单位
    WriteDrugOrder().write_Anuits(y, Anuits)
    # 填写申请数量
    WriteDrugOrder().write_AapplyNums(y, AapplyNums)
    Delay(500)
    # 提交申请
    Operational = Submit
    execute_operation(Operational)


def check_order(OperationalStatus, sql):
    '''
    查询订单
    :return:None
    '''
    # 点击查询按钮
    execute_operation(OperationalStatus)
    CODE = query_applycode(sql)
    write_log(20, "查询框中输入的申请单号是：{}".format(CODE))
    if splitter_panel.txtApplyBillCode.Exists:
        splitter_panel.txtApplyBillCode.Click()
        # 申请单号赋值给查询窗口
        splitter_panel.txtApplyBillCode.SetText(CODE)
        # 点击查询按钮
        btn_query.ClickButton()
        # 点击确定按钮
        hsp.frmQueryDrugApplyOut.pnlBottom.btnSave.ClickButton()
    else:
        splitterPanel.txtInBillCode.Click(38, 13)
        # 申请单号赋值给查询窗口
        splitterPanel.txtInBillCode.SetText(CODE)
        splitterPanel.btnQuery.ClickButton()
        hsp.frmQueryDrugInputApply.pnlBottom.btnSave.ClickButton()
    return


def query_applycode(sql):
    # 查询生成单号码
    APPLY_BILLCODE = excute_sql(sql)
    # Project.Variables.APPLY_BILLCODE = APPLY_BILLCODE
    # Log.Message(APPLY_BILLCODE)
    return APPLY_BILLCODE
