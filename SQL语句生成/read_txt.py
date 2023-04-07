from PyQt5 import *
import pymysql



# SQL 语句解析生成器
def read_sql_txt(file_read):
    '''
    读取SQL文件函数
    file_read:SQL文件路径
    return:SQL_list
    '''
    with open(rf"{file_read}",mode='r') as r:
        SQL_list = r.readlines()
        return SQL_list

def sql_split(sql):
    '''
    处理单行SQL语句函数
    sql:等待处理SQL语句
    return:sql写入字段列表
    '''
    return sql.strip('\n').split()

def sql_generate(field_name_list,field_value_list,table_name,storage_road):
    '''
    SQL拼接函数
    field_name_list:字段列表传入
    field_value_list:字段值的传入
    table_name:表名
    storage_road:存储路径
    '''
    field_name_num = len(field_name_list)
    for field_value in field_value_list:
        field_name = ''
        field_values = ''
        for num in range(field_name_num):
            if num == field_name_num -1 :
                field_name += field_name_list[num]
            else :
                field_name += field_name_list[num] +','
        
        for num in range(len(field_value)):
            if num == len(field_value) -1 :
                field_values += f'"{field_value[num]}"'
            else :
                field_values += f'"{field_value[num]}"'+','

        sql = 'INSERT INTO '+ table_name + f'({field_name}) VALUES ' + f'({field_values});\n'
        with open(rf"{storage_road}",mode='a+',) as w:
            w.write(sql)

if __name__ == "__main__":
    sql_r_road = input('请输入SQL数据写读取路径：')
    sql_field_list = input('请输入写入SQL的字段中间使用空格分开：').split()
    sql_w_road = input('请输入SQL语句存储路径：')
    sql_table_name = input('请输入表名：')
    sql_data_list = [sql_split(sql) for sql in read_sql_txt(sql_r_road)]
    sql_generate(sql_field_list,sql_data_list,sql_table_name,sql_w_road)