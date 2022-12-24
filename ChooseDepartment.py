# 这是一个切换药房的函数  传入药房名称
def ChooseDepartment(DepartmentName):
    import time
    # 切换药房
    hsp = Aliases.Hsp
    # 获取到右下角科室的名称
    Name = Aliases.Hsp.frmMain.panel_bottom_status.tcbDept.WinFormsObject("Edit", "").wText
    Log.Message("识别到的库是：-----")
    Log.Message(Name)
    if Name == DepartmentName:
        Log.Message("打开的是:" + DepartmentName)
    #      hsp.frmMain.panel_bottom_status.tcbDept.Click(204, 17)
    #      hsp.ToolStripDropDown.DataGridView.ClickCell(1, "编码")
    else:
        # 否则打开中草药房
        hsp.frmMain.panel_bottom_status.tcbDept.Click(204, 17)
        time.sleep(0.5)
        hsp.ToolStripDropDown.DataGridView.ClickCell(1, "编码")
        Log.Message("切换到:" + DepartmentName)
