import numpy as np
import AI_ImportingNetworkData as ind


class Renumer_CoordinateToFloat:
    def __init__(self, filename):  # 将（动态节点）直角坐标转换为浮点数坐标模块
        self.net_data = ind.Read(filename)
        self.dynamic_num = self.net_data.rows0 - self.net_data.count_static - 1
        self.dynamic_floatcoordinate = np.zeros((self.dynamic_num, 2), dtype=float)
        # dynamic_floatcoordinate矩阵用于储存动态节点的编号和浮点数坐标【重命名，浮点数坐标】
        for i in range(self.dynamic_num):
            self.dynamic_floatcoordinate[i, 0] = self.net_data.dynamic_point[i][0]
            # 浮点数坐标的第一列为读取模块动态节点矩阵的第一列：重命名（重编号）
            self.dynamic_floatcoordinate[i, 1] = \
                float('%.2f' % (self.net_data.dynamic_point[i][2] + self.net_data.dynamic_point[i][3] / 100))
            # 将浮点数存为x.y的形式，第二列数据 = x + y/100，如当x = 2，y = 10时，为避免2.10存为2.1, 需令浮点数坐标保存两位小数
            i += 1

    def get_floatcoordinate(self):  # 该函数用于返回浮点数坐标矩阵（列表）
        return self.dynamic_floatcoordinate


