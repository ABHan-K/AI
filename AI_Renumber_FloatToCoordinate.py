import numpy as np
import math
import AI_Renumber_CoordinateToFloat as rctf
import AI_ImportingNetworkData as ind


class Renumber_FloatToCoordinate:
    def __init__(self, filename):
        self.dynamic_floatdata = rctf.Renumber_CoordinateToFloat(filename)
        self.xycoordinate_data = np.zeros((self.dynamic_floatdata.dynamic_num, 3))
        self.ind = ind.Read(filename)
        self.static_list = self.ind.static_point.T[0]

        # 将动态节点浮点数坐标重新转为直角坐标，初始化动态节点直角坐标矩阵xycoordinate_data：【重命名，坐标x，坐标y】
        '''
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
        '''

    '''
    def coordinatelist(self, *float_list):  # 建立输入浮点数列表输出xy坐标矩阵的函数coordinatelist

        coordinatelist = np.zeros((self.dynamic_floatdata.dynamic_num, 2))  # 建立n行2列的矩阵储存xy坐标【x，y】
        float_list=float_list[0]
        for i in range(self.dynamic_floatdata.dynamic_num):
            coordinatelist[i][0] = int(math.floor(float_list[i]))  # 第一列为浮点数的整数部分
            coordinatelist[i][1] = int((float_list[i] % 1) * 100)  # 第二列为浮点数的小数部分
            i += 1

        return coordinatelist
    '''

    def complete_node(self, float_list):

        print(float_list)
        coordinatelist = np.zeros((self.ind.rows0 - 1, 2))
        s_flag = 0
        d_flag = 0
        for i in range(self.ind.rows0 - 1):
            if i + 1 in self.static_list:
                coordinatelist[i][0] = self.ind.static_point[s_flag][1]
                coordinatelist[i][1] = self.ind.static_point[s_flag][2]
                s_flag += 1
            else:
                coordinatelist[i][0] = int(math.floor(float_list[d_flag]))  # 第一列为浮点数的整数部分
                coordinatelist[i][1] = int((float_list[d_flag] % 1) * 100)  # 第二列为浮点数的小数部分
                d_flag += 1
        return coordinatelist
