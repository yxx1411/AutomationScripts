from CheckSql import SQL, Purchase_SQL
from Mid_AppDrug import (apply_drugMain,
                         approval_Drug,
                         approval_into_storage,
                         apply_drugstore,
                         approval_drugstore,
                         call_into_storage,
                         procurement_order,
                         procurement_order,
                         add_drug_nums,
                         reduce_drug_nums)



def test_apply_drug():
    """
        药品领药申请的入口函数
    :return: None
    创建时间：2022-7-26
    """
    ParentMenuNames = '药品入出库'
    MenuNames = '药品入出库'
    DepartmentName = '西药房'
    OperationName = '药房-领药申请'
    Operational = '添加'
    Submit = "提交"
    TagrgetDepartment = 2
    OperationalStatus = '查询'
    sql = SQL
    apply_drugMain(
                    MenuPages,
                    ParentMenuNames,
                    MenuNames,
                    DepartmentName,
                    OperationName,
                    Operational,
                    Submit,
                    TagrgetDepartment,
                    OperationalStatus,
                    sql
                    )
    approval_Drug(sql)
    approval_into_storage(sql)





  
def test_call_drug():
    '''
        调药申请流程的主函数
    :return: None
    '''
    sql = SQL
    #向中草药房提供调药申请
    apply_drugstore(sql)
    #审核调药申请
    approval_drugstore(sql)
    #调药申请核准入库
    call_into_storage(sql)




def test_purchase_process():
    '''
        采购入库的流程
    :return:
    '''

    sql = Purchase_SQL
    procurement_order(sql)



def test_check_inventory_add():
    '''
        盘盈主流程的函数
    :return:
    '''
    sql = Purchase_SQL
    add_drug_nums(sql)





def test_check_inventory_reduce():
    '''
        盘亏的主流程
    :return:
    '''
    sql = SQL
    reduce_drug_nums(sql)





