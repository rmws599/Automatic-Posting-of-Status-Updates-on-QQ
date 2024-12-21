import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    try:
        手机, _, _ = xbot_visual.mobile.connect_device(connect_source="specific", connect_mode="appium", ingore_failed_device=True, auto_unlock=False, unlockType="pin", mobile_password=xbot_visual.decrypt(""), custom_name="23049RAD8C", _block=("main", 1, "连接手机"))
        excel_instance = xbot_visual.excel.get_active_workbook(_block=("main", 2, "获取当前激活的Excel对象"))
        excel_data = xbot_visual.excel.read_data_from_workbook(workbook=excel_instance, read_way="used_range", range=None, cell_row_num=None, cell_column_name=None, area_begin_row_num=None, area_begin_column_name=None, area_end_row_num=None, area_end_column_name=None, row_row_num=None, get_display_text=False, has_header_row=False, column_column_name=None, sheet_name="", using_text=False, text_cols="", clear_space=False, _block=("main", 3, "读取Excel内容"))
        for loop_item_index, row_data in enumerate(xbot_visual.workflow.list_iterator(list=excel_data, loop_start_index="1", loop_end_index="-1", output_with_index=True, _block=("main", 4, "ForEach列表循环"))):
            if xbot_visual.workflow.test(operand1=row_data[2], operator="==", operand2="正常", operator_options="{}", _block=("main", 5, "IF 条件")):
                continue
            #endif
            xbot_visual.mobile.element.click(session=手机, element=package.selector("打开发布按钮"), clicks="click", delay_after="1", anchor_type="center", _block=("main", 8, "点击元素(手机)"))
            xbot_visual.mobile.element.click(session=手机, element=package.selector("发说说"), clicks="click", delay_after="1", anchor_type="center", _block=("main", 9, "点击元素(手机)"))
            xbot_visual.mobile.element.click(session=手机, element=package.selector("选择图片"), clicks="click", delay_after="1", anchor_type="center", _block=("main", 10, "点击元素(手机)"))
            if xbot_visual.workflow.test(operand1=row_data[1], operator="==", operand2="1", operator_options="{}", _block=("main", 11, "IF 条件")):
                xbot_visual.mobile.element.click(session=手机, element=package.selector("图片1"), clicks="click", delay_after="1", anchor_type="center", _block=("main", 12, "点击元素(手机)"))
            elif xbot_visual.workflow.test(operand1=row_data[1], operator="==", operand2="2", operator_options="{}", _block=("main", 13, "Else IF")):
                xbot_visual.mobile.element.click(session=手机, element=package.selector("复选框"), clicks="click", delay_after="1", anchor_type="center", _block=("main", 14, "点击元素(手机)"))
            elif xbot_visual.workflow.test(operand1=row_data[1], operator="==", operand2="3", operator_options="{}", _block=("main", 15, "Else IF")):
                xbot_visual.mobile.element.click(session=手机, element=package.selector("复选框_1"), clicks="click", delay_after="1", anchor_type="center", _block=("main", 16, "点击元素(手机)"))
            #endif
            xbot_visual.mobile.element.click(session=手机, element=package.selector("按钮_下一步(1)"), clicks="click", delay_after="1", anchor_type="center", _block=("main", 18, "点击元素(手机)"))
            xbot_visual.mobile.element.click(session=手机, element=package.selector("输入框_分享新鲜事..."), clicks="click", delay_after="1", anchor_type="center", _block=("main", 19, "点击元素(手机)"))
            xbot_visual.mobile.element.input(session=手机, input_object="input", element=package.selector("输入框_分享新鲜事..."), text=lambda: row_data[0], append=False, end_with_enter=False, delay_after="1", _block=("main", 20, "输入文本(手机)"))
            xbot_visual.mobile.session.click(session=手机, click_postion="by_axios", point_x="800", point_y="50", template_images=None, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", clicks="click", delay_after="3", _block=("main", 21, "点击屏幕(手机)"))
            xbot_visual.mobile.element.click(session=手机, element=package.selector("文本框_发表"), clicks="click", delay_after="1", anchor_type="center", _block=("main", 22, "点击元素(手机)"))
            xbot_visual.excel.write_data_to_workbook(workbook=excel_instance, write_range="area", write_way="append", write_column_way="override", row_num=lambda: loop_item_index+2, column_name="C", begin_row_num="1", begin_column_name="", content="正常", sheet_name="", write_as_text_cols=None, _block=("main", 23, "写入内容至Excel工作表"))
        #endloop
    finally:
        pass
