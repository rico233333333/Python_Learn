import time
import pandas as pd  # 处理数据文件
import os
from prettytable import PrettyTable  # 美化输出表格


# 定义员工文件新建
def add_employee(employee_num, employee_name, employee_age_num, employee_department, employee_offer):
    # employee_num : 员工工号
    # employee_name : 员工姓名
    # employee_age_num : 员工年龄
    # employee_department : 员工部门
    # employee_offer : 员工职务
    # employee_message : 员工信息 工号不变
    employee_message = {employee_num: [employee_num, employee_name, employee_age_num, employee_department, employee_offer]}
    return employee_message


# 定义文件格式转换函数  此函数使用pandas库进行文件格式进行转换
# 文件不存在的情况 使用此函数创建
def format_conversion(data):
    # data : 字典类型的数据
    employee_index = list(data.keys())  # index
    employee_data = list(data.values())  # data
    # 此函数只需要传入字典类型的数据即可
    # 新建pandas的DATAFRAME类型数据
    employee_columns = ["工号", "姓名", "年龄", "部门", "职务"]
    file_data_frame = pd.DataFrame(data=employee_data, index=employee_index, columns=employee_columns)
    return file_data_frame


# 判断文件是否存在函数
def judge_the_file(path_road, file_name):
    # 此处需要传入父目录 path_road
    # 此处需要传入被判断目录 file_name
    file_list = os.listdir(path_road)
    if file_name in file_list:
        return True
    else:
        return False


if __name__ == '__main__':
    print("欢迎使用员工管理系统 V1.0版本")
    print("-" * 30)
    file_data_frame = pd.DataFrame()  # 定义全局变量
    if judge_the_file("./", "职工信息管理系统.xlsx") == True:
        file_data_frame = pd.read_excel("./职工信息管理系统.xlsx")
    # 设置对齐
    # pd.set_option('display.unicode.ambiguous_as_wide', True)
    pd.set_option('display.unicode.east_asian_width', True)
    while True:
        pt1 = PrettyTable()
        pt1.field_names = ["操作模式：", "1", "2", "3"]
        pt1.align["1"] = 'l'
        pt1.align["2"] = 'l'
        pt1.align["3"] = 'l'
        pt1.add_row(["1.录入员工信息", "2.删除员工信息", "3.修改员工信息", "4.查看所有员工信息"])
        pt1.add_row(["5.排序员工信息", "6.导出员工信息", "7.关于作者", "8.退出"])
        print(pt1)
        user_input = input("请输入操作模式代号：")
        if user_input == "1":
            if len(file_data_frame.values) == 0:
                file_data_dict = {}  # 定义变量存储字典
                while True:
                    print("操作模式：")
                    print("1.录入完毕\t2.继续录入")
                    e_choice = input("请输入操作模式代号：")
                    if e_choice == "1":
                        break
                    elif e_choice == "2":
                        while True:
                            try:
                                employee_num = int(input("工号："))
                                if employee_num not in list(file_data_dict.keys()):
                                    break
                                else:
                                    print("输入有误，员工工号不可重复")
                            except:
                                print("输入错误，请输入正确的工号，此工号仅限数字，不带任何符号！！！")
                        employee_name = input("姓名：")
                        while True:
                            try:
                                employee_age_num = int(input("年龄："))
                                break
                            except:
                                print("输入错误，请输入正确的年龄，此年龄仅限数字，不带任何符号！！！")
                        employee_department = input("部门：")
                        employee_offer = input("职务：")
                        print("-" * 30)
                        employee_message = add_employee(employee_num, employee_name, employee_age_num,
                                                        employee_department,
                                                        employee_offer)
                        file_data_dict.update(employee_message)
                        file_data_frame = format_conversion(file_data_dict)  # 此处讲DATAFRAME类型数据存储
                    else:
                        print("您的输入有误，将返回上级操作")
            else:
                file_data_dict = {}  # 定义全局变量存储字典
                index = []
                value = []
                while True:
                    print("操作模式：")
                    print("1.录入完毕\t2.继续录入")
                    e_choice = input("请输入操作模式代号：")
                    if e_choice == "1":
                        break
                    elif e_choice == "2":
                        list_data_frame_num = []
                        for list_data_frame in list(file_data_frame.values):
                            list_data_frame_num.append(list_data_frame[0])
                        while True:
                            try:
                                employee_num = int(input("工号："))
                            except:
                                print("输入错误，请输入正确的工号，此工号仅限数字，不带任何符号！！！")
                                continue
                            if employee_num in list_data_frame_num:
                                print("输入有误，员工工号不可重复")
                                continue
                            elif employee_num not in list_data_frame_num:
                                break
                        employee_name = input("姓名：")
                        while True:
                            try:
                                employee_age_num = int(input("年龄："))
                                break
                            except:
                                print("输入错误，请输入正确的年龄，此年龄仅限数字，不带任何符号！！！")
                        employee_department = input("部门：")
                        employee_offer = input("职务：")
                        print("-" * 30)
                        employee_message = add_employee(employee_num, employee_name, employee_age_num,
                                                        employee_department,
                                                        employee_offer)
                        dict_keys = list(employee_message.keys())
                        dict_index = dict_keys[0]
                        file_data_frame.loc[dict_index] = list(employee_message.values())[0]
                    else:
                        print("您的输入有误 将返回上级")
            file_data_frame.to_excel('./职工信息管理系统.xlsx', sheet_name="员工信息表", index=False)
        elif user_input == "2":
            # 删除员工信息
            while True:
                if len(file_data_frame.values) == 0:
                    print("您尚未录入员工信息，无法操作，将返回上级")
                    break
                else:
                    print("请选择您需要删除的工号")
                    pt2 = PrettyTable()
                    pt2.field_names = ["工号", "姓名", "年龄", "部门", "职务"]
                    file_data_frame_drop_list = file_data_frame.values
                    for i in range(len(list(file_data_frame.index))):
                        pt2.add_row(file_data_frame_drop_list[i])
                    print(pt2)
                    drop_list = list(file_data_frame.values)
                    drop_num = []
                    for drop_choice in drop_list:
                        drop_num.append(drop_choice[0])
                    while True:
                        try:
                            doop_choice = int(input("请输入需要删除员工的工号："))
                        except:
                            print("输入错误，请输入正确的工号，此工号仅限数字，不带任何符号！！！")
                            continue
                        if doop_choice in drop_num:
                            break
                        else:
                            print("工号不存在")
                            continue
                    drop_index = drop_num.index(doop_choice)
                    file_data_frame.drop(drop_index, inplace=True)
                    file_data_frame.to_excel('./职工信息管理系统.xlsx', sheet_name="员工信息表", index=False)
                    print("已删除")
                    pt3 = PrettyTable()
                    pt3.field_names = ["工号", "姓名", "年龄", "部门", "职务"]
                    file_data_frame_drop_list = file_data_frame.values
                    for i in range(len(list(file_data_frame.index))):
                        pt3.add_row(file_data_frame_drop_list[i])
                    print(pt3)
                    time.sleep(2)
                    break
        elif user_input == "3":
            # 修改员工信息
            while True:
                if len(file_data_frame.values) == 0:
                    print("您尚未录入员工信息，无法操作，将返回上级")
                    break
                else:
                    print("请选择您需要修改的工号")
                    pt2 = PrettyTable()
                    columns = ["工号", "姓名", "年龄", "部门", "职务"]
                    pt2.field_names = columns
                    file_data_frame_drop_list = file_data_frame.values
                    for i in range(len(list(file_data_frame.index))):
                        pt2.add_row(file_data_frame_drop_list[i])
                    print(pt2)
                    drop_list = list(file_data_frame.values)
                    drop_num = []
                    for drop_choice in drop_list:
                        drop_num.append(drop_choice[0])
                    while True:
                        try:
                            doop_choice1 = int(input("请输入需要修改员工的工号："))
                        except:
                            print("输入错误，请输入正确的工号，此工号仅限数字，不带任何符号！！！")
                            continue
                        if doop_choice1 in drop_num:
                            break
                        else:
                            print("工号不存在")
                            continue
                    while True:
                        try:
                            doop_choice2 = input("请输入需要修改员工的标签：")
                        except:
                            print("输入错误，请输入正确的工号，此工号仅限数字，不带任何符号！！！")
                            continue
                        if doop_choice2 in columns:
                            break
                        else:
                            print("标签不存在")
                            continue
                    input_choice = input("请输入更改后的值：")
                    drop_index = drop_num.index(doop_choice1)
                    columns_index = columns.index(doop_choice2)
                    file_data_frame.iat[drop_index, columns_index] = input_choice
                    file_data_frame.to_excel('./职工信息管理系统.xlsx', sheet_name="员工信息表", index=False)
                    break
        elif user_input == "4":
            # 查看所有员工信息
            # 创建表格
            if judge_the_file("./", "职工信息管理系统.xlsx") == True:
                file_data_frame = pd.read_excel("./职工信息管理系统.xlsx")
            else:
                print("还未创建职工信息管理系统.xlsx")
            while True:
                if len(file_data_frame.values) == 0:
                    print("您尚未录入员工信息，无法操作，将返回上级")
                    break
                else:
                    pt = PrettyTable()
                    pt.field_names = ["工号", "姓名", "年龄", "部门", "职务"]
                    # 遍历pandas 的 dataFrame类型数据
                    pt_write_table_list = []
                    list_data_frame_num = []
                    for list_data_frame in list(file_data_frame.values):
                        list_data_frame_num.append(list_data_frame[0])
                    for value in range(0, len(list_data_frame_num)):
                        list_value = [list_data_frame_num[value],
                                      file_data_frame.iloc[value]['姓名'],
                                      file_data_frame.iloc[value]['年龄'],
                                      file_data_frame.iloc[value]['部门'],
                                      file_data_frame.iloc[value]['职务']]
                        pt_write_table_list.append(list_value)
                    for pt_write_table in pt_write_table_list:
                        pt.add_row(pt_write_table)
                    print(pt)
                    print("将在两秒后返回上级")
                    break
        elif user_input == "5":
            # 排序员工信息
            while True:
                if len(file_data_frame.values) == 0:
                    print("您尚未录入员工信息，无法操作，将返回上级")
                    break
                else:
                    file_indedx = file_data_frame.sort_values(by='工号')
                    pt = PrettyTable()
                    pt.field_names = ["工号", "姓名", "年龄", "部门", "职务"]
                    # 遍历pandas 的 dataFrame类型数据
                    pt_write_table_list = []
                    list_data_frame_num = []
                    for list_data_frame in list(file_indedx.values):
                        list_data_frame_num.append(list_data_frame[0])
                    for value in range(0, len(list_data_frame_num)):
                        list_value = [list_data_frame_num[value],
                                      file_indedx.iloc[value]['姓名'],
                                      file_indedx.iloc[value]['年龄'],
                                      file_indedx.iloc[value]['部门'],
                                      file_indedx.iloc[value]['职务']]
                        pt_write_table_list.append(list_value)
                    for pt_write_table in pt_write_table_list:
                        pt.add_row(pt_write_table)
                    print("已排序：")
                    print(pt)
                    break
        elif user_input == "6":
            # 导出员工信息
            while True:
                print("案例输入格式：./职工信息管理系统.xlsx")
                file_road = input("请输入存储的文件存储路径：")
                try:
                    file_data_frame.to_excel(file_road, sheet_name="员工信息表", index=False)
                except:
                    print("输入错误，案例输入格式：./职工信息管理系统.xlsx")
        elif user_input == "7":
            # 关于作者
            print("好的系统主程序就几行，我的面向对象功底还不太深厚")
        elif user_input == "8":
            file_data_frame.to_excel('./职工信息管理系统.xlsx', sheet_name="员工信息表", index=False)
            break  # 退出
        else:
            print("您输入的编号有误 将在两秒后返回重新操作")
            time.sleep(2)
            continue
