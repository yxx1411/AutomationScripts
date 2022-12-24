from InventoryManagement import into_pages, into_menu

hsp = Aliases.Hsp
baseFormNew = hsp.frmMain.panel_fill_content.extTabStrip1.Nto_His_DrugInOut_UI_Controls_ucPrePayFinanceItemizedBill.BaseFormNew

search_bar = baseFormNew.panel1.panelMain.ucPrePayFinanceItemizedBill


class CheckDrugNums:
    def __int__(self):
        pass

    def into_drug_details(self, DrugName):
        # 进入药房管理界面
        MenuPages = "药库管理"
        ParentMenuNames = "查询统计"
        MenuNames = "药品明细帐"
        into_pages(MenuPages)
        into_menu(ParentMenuNames, MenuNames)
        search = search_bar.extPannel1
        search.dtpBeginTime.wDate = "2022-08-11"
        extTextBox = search.txtFilter
        extTextBox.Click(28, 13)
        extTextBox.SetText(DrugName)
