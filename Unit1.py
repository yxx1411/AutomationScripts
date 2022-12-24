def FactoryInfoEdit():
    import BaseFuntion
    FactoryName = ""
    InputFactName = ""
    Project.Variables.FactoryFile.Reset()
    RecordIdx = 1
    while RecordIdx < 2:
        Project.Variables.FactoryFile.Next()
        RecordIdx = RecordIdx + 1
    RecordIdx = 2
    while RecordIdx <= 5:
        #The beginning of the 检索厂家是否存在 group
        #The beginning of the 检索厂家 group
        #Clicks the 'txtFilter' object.
        Aliases.Hsp.frmMain.panel_fill_content.extTabStrip1.Nto_His_Term_UI_Controls_ucCompanyManager.BaseFormNew.panel1.panelMain.ucCompanyManager.panel1.txtFilter.Click(32, 11)
        #Enters the text KeywordTests.FactoryInfoEdit.Variables.FactoryFile["厂家"] in the 'txtFilter' text editor.
        Aliases.Hsp.frmMain.panel_fill_content.extTabStrip1.Nto_His_Term_UI_Controls_ucCompanyManager.BaseFormNew.panel1.panelMain.ucCompanyManager.panel1.txtFilter.SetText(Project.Variables.FactoryFile.Value["厂家"])
        #The end of the 检索厂家 group
        #Runs a script routine.
        LastResult = BaseFuntion.ocr_words(192, 218, 550, 249)
        Log.Message("===========")
        Log.Message(LastResult)
        FactoryName = LastResult
        #Posts an information message to the test log.
        Log.Message(FactoryName, "")
        if InputFactName == FactoryName:
            #Posts an information message to the test log.
            Log.Message("厂家已存在", "")
        else:
            #Posts an information message to the test log.
            Log.Message("可以添加厂家", "")
            #点击添加按钮
            Aliases.Hsp.frmMain.panel_fill_content.extTabStrip1.Nto_His_Term_UI_Controls_ucCompanyManager.BaseFormNew.panelToolBar.toolBar1.Click(43, 13)
            #Clicks the 'txtName' object.
            Aliases.Hsp.frmCompanyMaintain.pnlMain.extPannel1.txtName.Click(25, 13)
            #Enters the text KeywordTests.FactoryInfoEdit.Variables.FactoryFile["厂家"] in the 'txtName' text editor.
            Aliases.Hsp.frmCompanyMaintain.pnlMain.extPannel1.txtName.SetText(Project.Variables.FactoryFile.Value["厂家"])
            #Clicks the 'btnSave' button.
            Aliases.Hsp.frmCompanyMaintain.pnlBottom.btnSave.ClickButton()
            #Clicks the 'ExtButton' button.
            Aliases.Hsp.FrmMessageBox.ExtButton.ClickButton()
            #Clicks the 'btnClose' button.
            Aliases.Hsp.frmCompanyMaintain.pnlBottom.btnClose.ClickButton()
        #The end of the 检索厂家是否存在 group
        Project.Variables.FactoryFile.Next()
        RecordIdx = RecordIdx + 1
