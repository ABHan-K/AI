import numpy as np
import AI_ImportingNetworkData as ind
import AI_Renumber_FloatToCoordinate as rftc


class PointCoordinate:
    def __init__(self, filename):  # 定义类,根据重命名（重编号）得到对应的x、y坐标
        self.dynamic_or_static = ind.Read(filename)
        self.dynamic_number = self.dynamic_or_static.rows0 - self.dynamic_or_static.count_static - 1
        self.pc = rftc.Renumber_FloatToCoordinate(filename)
        '''
        if (self.dynamic_or_static.bus_data[m][2] != 0) and (self.dynamic_or_static.bus_data[m][3] != 0):
            # 判断是否为静态节点
            self.x = self.dynamic_or_static.bus_data[m][2]  # 由busdata读取静态节点的坐标
            self.y = self.dynamic_or_static.bus_data[m][3]

        else:
            for i in range(self.dynamic_number):
                if self.dynamic_or_static.dynamic_point[i][0] == m:  # 由动态节点直角坐标矩阵得到对应的x，y坐标
                    self.x = self.pc.xycoordinate_data[i][1]
                    self.y = self.pc.xycoordinate_data[i][2]
                else:
                    i += 1
        '''

    def get_coordinate(self, n, *floatlist):
        ftclist_nonumber = self.pc.coordinatelist(*floatlist)  # 将浮点数列表转回为两列的xy坐标矩阵，存为ftclist_nonumber矩阵
        ftclist_withnumber = np.zeros((self.dynamic_number, 3))  # 建立一个n行3列的矩阵，其中n为动态节点个数，三列分别储存【重编号，x，y】
        for i in range(self.dynamic_number):
            ftclist_withnumber[i][0] = self.dynamic_or_static.dynamic_point[i][0]  # 第一列利用Read模块的动态节点矩阵的第一列数据（重编号）进行赋值
            ftclist_withnumber[i][1] = ftclist_nonumber[i][0]  # 第二列为floatlist的整数部分，ftclist_nonumber矩阵的第一列
            ftclist_withnumber[i][2] = ftclist_nonumber[i][1]  # 第三列为floatlist的小数部分，ftclist_nonumber矩阵的第二列
            i += 1

        if (self.dynamic_or_static.bus_data[n][2] != 0) and (self.dynamic_or_static.bus_data[n][3] != 0):
            # 判断是否为静态节点
            self.xc = self.dynamic_or_static.bus_data[n][2]  # 由busdata读取静态节点的坐标
            self.yc = self.dynamic_or_static.bus_data[n][3]

        else:
            for i in range(self.dynamic_number):
                if self.dynamic_or_static.dynamic_point[i][0] == n:  # 由ftclist_withnumber矩阵得到对应的x，y坐标
                    self.xc = ftclist_withnumber[i][1]
                    self.yc = ftclist_withnumber[i][2]
                else:
                    i += 1

        return self.xc, self.yc
