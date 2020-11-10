import numpy as np
import os
import re
import xlrd
import xlwt

#bus_data = np.zeros((36, 3))  # 用于存储第一个工作表内的节点数据：【节点名，坐标x，坐标y】
#line_data = np.zeros((36, 36))  # 用于存储第二个工作表内的线路数据：如两节点间有线路，则对应mat[i，j]和mat[j,i]置1


def read_excel():  # 读取模块
    xl = xlrd.open_workbook(r'F:\360MoveData\Users\DELL\Desktop\数据.xlsx')
    table0 = xl.sheets()[0]  # 读取第一个工作表
    rows0 = table0.nrows
    cols0 = table0.ncols
    bus_data = np.zeros((rows0, cols0+1))
    line_data = np.zeros((rows0,rows0))
    for i in range(rows0):
        if i != 0:  # 略去第一行标题数据
            for j in range(cols0):
                ctype0 = table0.cell(i, j).ctype  # 读取单元格的数据类型:0-空 1-字符串 2-数字 3-日期 4-布尔 5-error
                cell_value0 = table0.cell(i, j).value  # 读取单元格的数据
                if ctype0 == 2 and cell_value0 % 1 == 0:
                    cell_value0 = int(cell_value0)
                    bus_data[i, j] = cell_value0
                elif ctype0 == 1:
                    if j == 1:
                        cell_value0 = re.sub("\D", "  ", cell_value0)  # 从字符串中寻找非数字的字符，用“ ”替代
                        bus_data[i, j] = int(cell_value0.split()[0])
                        bus_data[i, j + 1] = cell_value0.split()[1]
                    elif j == 0:
                        cell_value0 = re.sub("\D", "  ", cell_value0)
                        bus_data[i, j] = int(cell_value0.split()[0]) + 100  # 将trans节点与其他节点区分开来,把节点编号加100
    # table1 = xl.sheets()[1]  # 读取第二个工作表
    # rows1 = table1.nrows
    # cols1 = table1.ncols
    # i = 1
    # while i <= rows1:
    #     ctype1 = table1.cell(i, 1).ctype
    #     cell_value1 = table1.cell(i, 1).value
    #     ctype2 = table1.cell(i, 2).ctype
    #     cell_value2 = table1.cell(i, 2).value
    #     if ctype1 == 2 and cell_value1 % 1 == 0:
    #         start_point = int(cell_value1)
    #     elif ctype1 == 1:
    #         cell_value1 = re.sub("\D", "  ", cell_value1)
    #         start_point = int(cell_value1.split()[0]) + 100
    #     if ctype2 == 2 and cell_value2 % 1 == 0:
    #         end_point = int(cell_value2)
    #     elif ctype2 == 1:
    #         cell_value2 = re.sub("\D", "  ", cell_value2)
    #         end_point = int(cell_value2.split()[0]) + 100
    #     line_data[start_point, end_point] = 1
    #     line_data[end_point, start_point] = 1
    #     i += 1
    print(bus_data)
    print(line_data)


read_excel()
#print(bus_data)
#print(line_data)

