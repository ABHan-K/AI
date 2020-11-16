import numpy as np
import math
import AI_ImportingNetworkData as ind
import AI_Renumber_CoordinateToFloat as rctf


class Renumber_FloatToCoordinate:
    def __init__(self, filename):
        self.dynamic_floatdata = rctf.Renumer_CoordinateToFloat(filename)
        self.xycoordinate_data = np.zeros((self.dynamic_floatdata.dynamic_num, 3))
        # 将动态节点浮点数坐标重新转为直角坐标，初始化动态节点直角坐标矩阵xycoordinate_data：【重命名，坐标x，坐标y】
        self.d = 0  # 交点数: d
        for i in range(self.dynamic_floatdata.dynamic_num):
            self.xycoordinate_data[i][0] = self.dynamic_floatdata.dynamic_floatcoordinate[i][0]
            # 动态节点矩阵第一列为重命名的编号
            self.xycoordinate_data[i][1] = int(self.dynamic_floatdata.dynamic_floatcoordinate[i][1] \
                                               - math.floor(self.dynamic_floatdata.dynamic_floatcoordinate[i][1]))
            # 第二列x为浮点数坐标的整数部分
            self.xycoordinate_data[i][2] = int((self.dynamic_floatdata.dynamic_floatcoordinate[i][1] \
                                                - self.xycoordinate_data[i][1]) * 100)
            # 第三列y为浮点数坐标的小数部分
            i += 1