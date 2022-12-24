from ToolbarFunction import click_toolbar_words
from InventoryManagement import (into_pages,
                                 into_menu,
                                 choose_department,
                                 choose_type,
                                 choose_target_department,
                                 execute_operation,
                                 write_order,
                                 check_order,
                                 close_messagebox,
                                 write_call_drugOder,
                                 write_purchase_order,
                                 write_Acheck_inventory_add)


def apply_drugMain(MenuPages, ParentMenuNames, MenuNames,
                   DepartmentName, OperationName, Operational,
                   Submit, TagrgetDepartment, OperationalStatus, sql):
    '''
    :param MenuPages: 顶部栏的菜单
    :param ParentMenuNames: 左侧栏的菜单
    :param MenuNames: 子菜单
    :param DepartmentName: 底部栏的科室名称
    :param OperationName: 执行的操作
    :param Operational: 执行的操作
    :param Submit: 目标科室
    :param TagrgetDepartment:
    :param OperationalStatus:
    :param sql: 操作状态
    :return:
    创建时间：2022-8-6
    '''
    # 进入药房管理界面
    into_pages(MenuPages)
    # 选择底部操作栏中的科室
    choose_department(DepartmentName)
    # 选择左侧栏中的菜单，点击子菜单操作
    into_menu(ParentMenuNames, MenuNames)
    # 选择操作类型
    choose_type(OperationName)
    # 选择申请的目标科室
    choose_target_department(OperationName, TagrgetDepartment)
    # 选择执行的操作
    execute_operation(Operational)
    # 对操作类型进行判断，如何点击添加操作的按钮，则需要书写表单
    if Operational == '添加':
        write_order(Submit)
        close_messagebox()
    # 执行提交操作
    check_order(OperationalStatus, sql)
    # 关闭弹框
    close_messagebox()


def approval_Drug(sql):
    '''
        科室核准出库的审核流程
        输入的参数：MenuPages：顶部栏的菜单
            ParentMenuNames：左侧栏的菜单
            MenuNames：子菜单
            DepartmentName：底部栏的科室名称
            OperationName：执行的操作
            Operational：执行的操作
            TagrgetDepartment:目标科室
            OperationalStatus：操作状态

    :param sql:
    :return: None
    '''

    MenuPages = '药库管理'
    ParentMenuNames = "入出库管理"
    MenuNames = "药品入出库"
    DepartmentName = "西药库"
    OperationName = "药库-药房申请核准出库"
    TagrgetDepartment = "西药房"
    OperationalStatus = "查询"
    Operational = "审核"

    # 进入药库管理界面
    into_pages(MenuPages)
    # 选择底部操作栏中的科室
    choose_department(DepartmentName)
    # 选择左侧栏中的菜单，点击子菜单操作
    into_menu(ParentMenuNames, MenuNames)
    # 选择操作类型
    choose_type(OperationName)
    # 选择申请的目标科室
    choose_target_department(OperationName, TagrgetDepartment)
    # 选择执行的操作
    check_order(OperationalStatus, sql)
    # 点击审核按钮
    execute_operation(Operational)
    # 关闭弹框
    close_messagebox()


def approval_into_storage(sql):
    # .............................................................................................................................
    # 目的：入库领药申请
    # 输入的参数：MenuPages：顶部栏的菜单
    #           ParentMenuNames：左侧栏的菜单
    #           MenuNames：子菜单
    #           DepartmentName：底部栏的科室名称
    #           OperationName：执行的操作
    #           Operational：执行的操作
    #           TagrgetDepartment:目标科室
    #           OperationalStatus：操作状态
    # 返回结果：
    # 注意事项：通过配置不同的操作实现不同的入出库类型
    # 作者：杨继宏
    # 创建时间：2022-8-6
    # ..............................................................................................................................
    # 进入药房管理界面

    MenuPages = '药房管理'
    ParentMenuNames = '药品入出库'
    MenuNames = '药品入出库'
    DepartmentName = '西药房'
    OperationName = '药房-领药申请'
    TagrgetDepartment = 2
    OperationalStatus = '查询'
    Operational = '审核'

    # 进入药房管理界面
    into_pages(MenuPages)
    # 选择底部操作栏中的科室
    choose_department(DepartmentName)
    # 选择左侧栏中的菜单，点击子菜单操作
    into_menu(ParentMenuNames, MenuNames)
    # 选择操作类型
    choose_type(OperationName)
    # 选择申请的目标科室
    choose_target_department(OperationName, TagrgetDepartment)
    # 查询出入库的订单
    check_order(OperationalStatus, sql)
    # 查询出订单以后，点击审核
    execute_operation(Operational)
    # 关闭弹框
    close_messagebox()


def apply_drugstore(sql):
    MenuPages = '药房管理'
    ParentMenuNames = '药品入出库'
    MenuNames = '药品入出库'
    DepartmentName = '西药房'
    OperationName = '药房-调药申请'
    TagrgetDepartment = 0
    Operational = "添加"
    Submit = "提交"
    OperationalStatus = "查询"
    sql = sql
    # 进入药房管理界面
    into_pages(MenuPages)
    # 选择底部操作栏中的科室
    choose_department(DepartmentName)
    # 选择左侧栏中的菜单，点击子菜单操作
    into_menu(ParentMenuNames, MenuNames)
    # 选择操作类型
    choose_type(OperationName)
    # 选择申请的目标科室
    choose_target_department(OperationName, TagrgetDepartment)
    # 对操作类型进行判断，如何点击添加操作的按钮，则需要书写表单
    # 选择执行的操作
    execute_operation(Operational)
    if Operational == '添加':
        write_call_drugOder(Submit)
        close_messagebox()
    # 执行提交操作
    check_order(OperationalStatus, sql)
    # 关闭弹框
    close_messagebox()


def approval_drugstore(sql):
    # .............................................................................................................................
    # 目的：药房调药核准
    #
    # 输入的参数：MenuPages：顶部栏的菜单
    #           ParentMenuNames：左侧栏的菜单
    #           MenuNames：子菜单
    #           DepartmentName：底部栏的科室名称
    #           OperationName：执行的操作
    #           Operational：执行的操作
    #           TagrgetDepartment:目标科室
    #           OperationalStatus：操作状态
    #
    # 返回结果：
    #
    # 注意事项：通过配置不同的操作实现不同的入出库类型
    #
    # 作者：杨继宏
    # 创建时间：2022-8-6
    # ..............................................................................................................................
    # 进入药房管理界面
    MenuPages = '药房管理'
    ParentMenuNames = '药品入出库'
    MenuNames = '药品入出库'
    DepartmentName = '中草药房'
    OperationName = "药房-调药核准"
    TagrgetDepartment = 0
    OperationalStatus = "查询"
    Operational = "审核"
    # 进入药库管理界面
    into_pages(MenuPages)
    # 选择底部操作栏中的科室
    choose_department(DepartmentName)
    # 选择左侧栏中的菜单，点击子菜单操作
    into_menu(ParentMenuNames, MenuNames)
    # 选择操作类型
    choose_type(OperationName)
    # 选择申请的目标科室
    choose_target_department(OperationName, TagrgetDepartment)
    # 选择执行的操作
    check_order(OperationalStatus, sql)
    # 点击审核按钮
    execute_operation(Operational)
    # 关闭弹框
    close_messagebox()


def call_into_storage(sql):
    # .............................................................................................................................
    # 目的：入库领药申请
    # 输入的参数：MenuPages：顶部栏的菜单
    #           ParentMenuNames：左侧栏的菜单
    #           MenuNames：子菜单
    #           DepartmentName：底部栏的科室名称
    #           OperationName：执行的操作
    #           Operational：执行的操作
    #           TagrgetDepartment:目标科室
    #           OperationalStatus：操作状态
    # 返回结果：
    # 注意事项：通过配置不同的操作实现不同的入出库类型
    # 作者：杨继宏
    # 创建时间：2022-8-6
    # ..............................................................................................................................
    # 进入药房管理界面

    MenuPages = '药房管理'
    ParentMenuNames = '药品入出库'
    MenuNames = '药品入出库'
    DepartmentName = '西药房'
    OperationName = '药房-调药申请'
    TagrgetDepartment = 0
    OperationalStatus = '查询'
    Operational = '审核'

    # 进入药房管理界面
    into_pages(MenuPages)
    # 选择底部操作栏中的科室
    choose_department(DepartmentName)
    # 选择左侧栏中的菜单，点击子菜单操作
    into_menu(ParentMenuNames, MenuNames)
    # 选择操作类型
    choose_type(OperationName)
    # 选择申请的目标科室
    choose_target_department(OperationName, TagrgetDepartment)
    # 查询出入库的订单
    check_order(OperationalStatus, sql)
    # 查询出订单以后，点击审核
    execute_operation(Operational)
    # 关闭弹框
    close_messagebox()


def procurement_order(sql):
    # .............................................................................................................................
    # 目的：采购入库流程
    # 输入的参数：MenuPages：顶部栏的菜单
    #           ParentMenuNames：左侧栏的菜单
    #           MenuNames：子菜单
    #           DepartmentName：底部栏的科室名称
    #           OperationName：执行的操作
    #           Operational：执行的操作
    #           TagrgetDepartment:目标科室
    #           OperationalStatus：操作状态
    # 返回结果：
    # 注意事项：通过配置不同的操作实现不同的入出库类型
    # 作者：杨继宏
    # 创建时间：2022-8-6
    # ..............................................................................................................................
    # 进入药房管理界面
    MenuPages = '药库管理'
    ParentMenuNames = "入出库管理"
    MenuNames = "药品入出库"
    DepartmentName = "西药库"
    OperationName = "药库-采购直接入库"
    TagrgetDepartment = 0
    OperationalStatus = "查询"
    Operational = "添加"
    Submit = "提交"

    # 进入药房管理界面
    into_pages(MenuPages)
    # 选择底部操作栏中的科室
    choose_department(DepartmentName)
    # 选择左侧栏中的菜单，点击子菜单操作
    into_menu(ParentMenuNames, MenuNames)
    # 选择操作类型
    choose_type(OperationName)
    # 选择申请的目标科室
    choose_target_department(OperationName, TagrgetDepartment)
    # 选择执行的操作
    execute_operation(Operational)
    # 对操作类型进行判断，如何点击添加操作的按钮，则需要书写表单
    if Operational == '添加':
        write_purchase_order(Submit)
        close_messagebox()
    # 执行提交操作
    check_order(OperationalStatus, sql)
    # 点击审核按钮
    Operational = "审核"
    execute_operation(Operational)
    # 关闭弹框
    close_messagebox()


def add_drug_nums(sql):
    MenuPages = '药库管理'
    ParentMenuNames = "入出库管理"
    MenuNames = "药品入出库"
    DepartmentName = "西药库"
    OperationName = "药库-盘盈"
    TagrgetDepartment = 0
    Operational = "添加"
    Submit = "提交"
    OperationalStatus = "查询"
    # 进入药库管理界面
    into_pages(MenuPages)
    # 选择底部操作栏中的科室-西药库
    choose_department(DepartmentName)
    # 选择左侧栏中的菜单，点击子菜单操作
    into_menu(ParentMenuNames, MenuNames)
    # 选择操作类型
    choose_type(OperationName)
    # 选择申请的目标科室
    choose_target_department(OperationName, TagrgetDepartment)
    # 选择执行的操作
    execute_operation(Operational)
    # 对操作类型进行判断，如何点击添加操作的按钮，则需要书写表单
    if Operational == '添加':
        write_Acheck_inventory_add(Submit)
        close_messagebox()
    # 执行提交操作
    check_order(OperationalStatus, sql)
    # 点击审核按钮
    Operational = "审核"
    execute_operation(Operational)
    # 关闭弹框
    close_messagebox()


def reduce_drug_nums(sql):
    # 盘盈中所用的XML和药房领药申请是一样的
    MenuPages = '药库管理'
    ParentMenuNames = "入出库管理"
    MenuNames = "药品入出库"
    DepartmentName = "西药库"
    OperationName = "药库-盘亏"
    TagrgetDepartment = 0
    Operational = "添加"
    Submit = "提交"
    OperationalStatus = "查询"
    # 进入药库管理界面
    into_pages(MenuPages)
    # 选择底部操作栏中的科室-西药库
    choose_department(DepartmentName)
    # 选择左侧栏中的菜单，点击子菜单操作
    into_menu(ParentMenuNames, MenuNames)
    # 选择操作类型
    choose_type(OperationName)
    # 选择申请的目标科室
    choose_target_department(OperationName, TagrgetDepartment)
    # 选择执行的操作
    execute_operation(Operational)
    # 对操作类型进行判断，如何点击添加操作的按钮，则需要书写表单
    if Operational == '添加':
        write_order(Submit)
        close_messagebox()
    # 执行提交操作
    check_order(OperationalStatus, sql)
    # 点击审核按钮
    Operational = "审核"
    execute_operation(Operational)
    # 关闭弹框
    close_messagebox()
