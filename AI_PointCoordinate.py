import AI_ImportingNetworkData as ind
import AI_Renumber_FloatToCoordinate as rftc


class PointCoordinate:
    def __init__(self, m, filename):  # 定义类,根据重命名（重编号）得到对应的x、y坐标
        self.dynamic_or_static = ind.Read(filename)
        self.pc = rftc.Renumber_FloatToCoordinate(filename)
        if ((self.dynamic_or_static.bus_data[m-1][2] != 0) and (self.dynamic_or_static.bus_data[m-1][3] != 0)):
            # 判断是否为静态节点
            self.x = self.dynamic_or_static.bus_data[m - 1][2]  # 由busdata读取静态节点的坐标
            self.y = self.dynamic_or_static.bus_data[m - 1][3]

        else:
            for i in range(self.dynamic_or_static.rows0 - self.dynamic_or_static.count_static - 1):
                if (self.dynamic_or_static.dynamic_point[i][0] == m):  # 由动态节点直角坐标矩阵得到对应的x，y坐标
                    self.x = self.pc.xycoordinate_data[i][1]
                    self.y = self.pc.xycoordinate_data[i][2]
                else:
                    i += 1