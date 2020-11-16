import numpy as np
import os
import re
import xlrd
import xlwt

np.set_printoptions(threshold=np.inf)


class Read:
    def __init__(self, filename):  # 读取模块
        self.xl = xlrd.open_workbook(filename)
        self.table0 = self.xl.sheets()[0]  # 读取第一个工作表
        self.rows0 = self.table0.nrows
        self.cols0 = self.table0.ncols
        self.table1 = self.xl.sheets()[1]  # 读取第二个工作表
        self.rows1 = self.table1.nrows
        self.cols1 = self.table1.ncols
        self.bus_data = np.zeros((self.rows0, self.cols0 + 2))
        # bus_data矩阵用于存储第一个工作表内的节点数据：【重命名，原节点名，坐标x，坐标y】
        self.line_data = np.zeros((self.rows0 - 1, self.rows0 - 1))
        # line_data矩阵用于存储第二个工作表内的线路数据：如两节点间有线路，则对应mat[i，j]和mat[j,i]置1
        self.count_static = 0  # 计算节点里面静态节点的个数
        for i in range(self.rows0):
            self.bus_data[i, 0] = i
        for i in range(self.rows0):
            if i != 0:  # 略去第一行标题数据
                for j in range(self.cols0):
                    ctype0 = self.table0.cell(i, j).ctype  # 读取单元格的数据类型:0-空 1-字符串 2-数字 3-日期 4-布尔 5-error
                    cell_value0 = self.table0.cell(i, j).value  # 读取单元格的数据
                    if ctype0 == 2 and cell_value0 % 1 == 0:
                        cell_value0 = int(cell_value0)
                        self.bus_data[i, j + 1] = cell_value0
                    elif ctype0 == 1:  # 单元格为字符串时有两种情况
                        if j == 1:  # 该单元格内容为（*，*）
                            cell_value0 = re.sub("\D", "  ", cell_value0)  # 从字符串中寻找非数字的字符，用“ ”替代
                            self.bus_data[i, j + 1] = int(cell_value0.split()[0])
                            self.bus_data[i, j + 2] = cell_value0.split()[1]
                            self.count_static += 1
                        elif j == 0:  # 该单元格内容为trans*
                            cell_value0 = re.sub("\D", "  ", cell_value0)
                            self.bus_data[i, j + 1] = int(cell_value0.split()[0]) + 100
                            # 将trans节点与其他节点区分开来,把节点编号加100
        self.static_point = np.zeros((self.count_static, 4))  # 该矩阵用于存储静态点数据
        self.dynamic_point = np.zeros((self.rows0 - self.count_static - 1, 4))  # 该矩阵用于存储动态点数据
        self.line_point = np.zeros((self.rows1 - 1, 2))  # 该矩阵用来存储连线两个端点的重编号

    def read_line(self):  # 该函数用来根据第二个工作表的数据生成节点间的线路连线矩阵,同时生成一个记录连线端点重编号的矩阵
        i = 1
        while i < self.rows1:
            ctype1 = self.table1.cell(i, 1).ctype  # 读取起点节点
            cell_value1 = self.table1.cell(i, 1).value
            ctype2 = self.table1.cell(i, 2).ctype  # 读取终点节点
            cell_value2 = self.table1.cell(i, 2).value
            if ctype1 == 2 and cell_value1 % 1 == 0:
                start_point = Read.find(self, int(cell_value1))
            elif ctype1 == 1:
                cell_value1 = re.sub("\D", "  ", cell_value1)
                start_point = Read.find(self, int(cell_value1.split()[0]) + 100)
            if ctype2 == 2 and cell_value2 % 1 == 0:
                end_point = Read.find(self, int(cell_value2))
            elif ctype2 == 1:
                cell_value2 = re.sub("\D", "  ", cell_value2)
                end_point = Read.find(self, int(cell_value2.split()[0]) + 100)
            self.line_data[start_point - 1, end_point - 1] = 1
            self.line_data[end_point - 1, start_point - 1] = 1
            self.line_point[i - 1, 0] = start_point
            self.line_point[i - 1, 1] = end_point
            i += 1

    def find(self, initial_NO):  # 该函数用来寻找节点的重编号
        for i in range(37):
            if self.bus_data[i, 1] == initial_NO:
                return int(self.bus_data[i, 0])

    def split_data(self):  # 把bus_data矩阵分成两个矩阵来储存
        i = 1
        i_static = 0
        i_dynamic = 0
        while i < self.rows0:  # 以下两个矩阵的i-1行对应的是bus_data里面的第i行因为要略去bus_data里面的第一行标题
            if self.bus_data[i, 2] == 0 and self.bus_data[i, 3] == 0:
                self.dynamic_point[i_dynamic, 0] = self.bus_data[i, 0]
                self.dynamic_point[i_dynamic, 1] = self.bus_data[i, 1]
                self.dynamic_point[i_dynamic, 2] = self.bus_data[i, 2]
                self.dynamic_point[i_dynamic, 3] = self.bus_data[i, 3]
                i_dynamic += 1
            else:
                self.static_point[i_static, 0] = self.bus_data[i, 0]
                self.static_point[i_static, 1] = self.bus_data[i, 1]
                self.static_point[i_static, 2] = self.bus_data[i, 2]
                self.static_point[i_static, 3] = self.bus_data[i, 3]
                i_static += 1
            i += 1

    def get_data_for_iteration(self):
        return self.count_dynamic, np.delete(self.count_dynamic, 1, axis=1)