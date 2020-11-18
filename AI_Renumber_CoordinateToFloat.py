import numpy as np
import AI_ImportingNetworkData as ind


class Renumber_CoordinateToFloat:
    def __init__(self, filename):  # 将（动态节点）直角坐标转换为浮点数坐标模块
        self.net_data = ind.Read(filename)
        self.dynamic_num = self.net_data.rows0 - self.net_data.count_static - 1
        self.dynamic_floatcoordinate = np.zeros(self.dynamic_num, dtype=float)
        # dynamic_floatcoordinate矩阵用于储存动态节点的编号和浮点数坐标【重命名，浮点数坐标】
        '''
        for i in range(self.dynamic_num):
            self.dynamic_floatcoordinate[i, 0] = self.net_data.dynamic_point[i][0]
            # 浮点数坐标的第一列为读取模块动态节点矩阵的第一列：重命名（重编号）
            self.dynamic_floatcoordinate[i, 1] = \
                float('%.2f' % (self.net_data.dynamic_point[i][2] + self.net_data.dynamic_point[i][3] / 100))
            # 将浮点数存为x.y的形式，第二列数据 = x + y/100，如当x = 2，y = 10时，为避免2.10存为2.1, 需令浮点数坐标保存两位小数
            i += 1
        '''

    def floatlist(self, *coordinatearray):  # 建立将xy坐标转为浮点数数列的函数floatlist
        floatlist = np.zeros(self.dynamic_num)  # 建立1行n列的数列存储浮点数坐标

        for i in range(self.dynamic_num):
            floatlist[i] = float('%.2f' % (coordinatearray[i][0] + coordinatearray[i][1] / 100))  # 将浮点数存为x.y的形式
            i += 1

        return floatlist  # 返回浮点数坐标列表
