import numpy as np
import os
import re
import xlrd
import xlwt

global bus_data  # 用于存储第一个工作表内的节点数据：【重命名，原节点名，坐标x，坐标y】
global line_data  # 用于存储第二个工作表内的线路数据：如两节点间有线路，则对应mat[i，j]和mat[j,i]置1

np.set_printoptions(threshold=np.inf)




def read_excel():  # 读取模块
    xl = xlrd.open_workbook(r'F:\360MoveData\Users\DELL\Desktop\数据.xlsx')
    table0 = xl.sheets()[0]  # 读取第一个工作表
    rows0 = table0.nrows
    cols0 = table0.ncols
    global bus_data
    global line_data
    bus_data = np.zeros((rows0, cols0 + 2))  # 初始化节点数据记录矩阵
    line_data = np.zeros((rows0 - 1, rows0 - 1))
    for i in range(rows0):
        bus_data[i, 0] = i
    for i in range(rows0):
        if i != 0:  # 略去第一行标题数据
            for j in range(cols0):
                ctype0 = table0.cell(i, j).ctype  # 读取单元格的数据类型:0-空 1-字符串 2-数字 3-日期 4-布尔 5-error
                cell_value0 = table0.cell(i, j).value  # 读取单元格的数据
                if ctype0 == 2 and cell_value0 % 1 == 0:
                    cell_value0 = int(cell_value0)
                    bus_data[i, j + 1] = cell_value0
                elif ctype0 == 1:
                    if j == 1:
                        cell_value0 = re.sub("\D", "  ", cell_value0)  # 从字符串中寻找非数字的字符，用“ ”替代
                        bus_data[i, j + 1] = int(cell_value0.split()[0])
                        bus_data[i, j + 2] = cell_value0.split()[1]
                    elif j == 0:
                        cell_value0 = re.sub("\D", "  ", cell_value0)
                        bus_data[i, j + 1] = int(cell_value0.split()[0]) + 100  # 将trans节点与其他节点区分开来,把节点编号加100
    table1 = xl.sheets()[1]  # 读取第二个工作表
    rows1 = table1.nrows
    cols1 = table1.ncols
    i = 1
    while i < rows1:
        ctype1 = table1.cell(i, 1).ctype  # 读取起点节点
        cell_value1 = table1.cell(i, 1).value
        ctype2 = table1.cell(i, 2).ctype  # 读取终点节点
        cell_value2 = table1.cell(i, 2).value
        if ctype1 == 2 and cell_value1 % 1 == 0:
            start_point = find(int(cell_value1))
        elif ctype1 == 1:
            cell_value1 = re.sub("\D", "  ", cell_value1)
            start_point = find(int(cell_value1.split()[0]) + 100)
        if ctype2 == 2 and cell_value2 % 1 == 0:
            end_point = find(int(cell_value2))
        elif ctype2 == 1:
            cell_value2 = re.sub("\D", "  ", cell_value2)
            end_point = find(int(cell_value2.split()[0]) + 100)
        line_data[start_point - 1, end_point - 1] = 1
        line_data[end_point - 1, start_point - 1] = 1
        i += 1
    print(bus_data)
    print(line_data)


def find(initial_NO):  # 该函数用来寻找节点的重编号
    global bus_data
    for i in range(37):
        if bus_data[i, 1] == initial_NO:
            return int(bus_data[i, 0])


read_excel()
