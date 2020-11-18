import AI_ImportingNetworkData as ind
import AI_PointCoordinate as pc


class IntersectionPoints:
    def __init__(self, filename):  # 计算交点数模块
        self.get_linedata = ind.Read(filename)
        self.get_line_coordinate = pc.PointCoordinate(filename)
        self.d = 0

        '''
        for i in range(self.get_linedata.rows1 - 1):
            m1 = int(self.get_linedata.line_point[i][0])
            m2 = int(self.get_linedata.line_point[i][1])  # 得到第一条边的头尾两节点对应的重命名（重编号）

            for j in range(i + 1, self.get_linedata.rows1 - 1):
                m3 = int(self.get_linedata.line_point[j][0])
                m4 = int(self.get_linedata.line_point[j][1])  # 得到第二条边的头尾两节点对应的重命名（重编号）

                p1 = self.get_line_coordinate(m1, filename)  # 利用重命名（重编号）得到两条边四个节点的坐标
                p2 = self.get_line_coordinate(m2, filename)
                p3 = self.get_line_coordinate(m3, filename)
                p4 = self.get_line_coordinate(m4, filename)

                n = IntersectionPoints.isintersec(self, p1, p2, p3, p4)
                self.d += n  # 判断两条边是否相交，若相交啧交点数d加一
                j += 1

            i += 1
        '''

    def isintersec(self, p1_x, p1_y, p2_x, p2_y, p3_x, p3_y, p4_x, p4_y):  # 判断两线段是否相交

        # 快速排斥，以l1、l2为对角线的矩形必相交，否则两线段不相交

        if (max(p1_x, p2_x) >= min(p3_x, p4_x)  # 矩形1最右端大于矩形2最左端
                and max(p3_x, p4_x) >= min(p1_x, p2_x)  # 矩形2最右端大于矩形最左端
                and max(p1_y, p2_y) >= min(p3_y, p4_y)  # 矩形1最高端大于矩形最低端
                and max(p3_y, p4_y) >= min(p1_y, p2_y)):  # 矩形2最高端大于矩形最低端

            #  若通过快速排斥则进行跨立实验
            if ((((p4_x - p1_x) * (p4_y - p3_y) - (p4_y - p1_y) * (p4_x - p3_x)) *
                 ((p4_x - p2_x) * (p4_y - p3_y) - (p4_y - p2_y) * (p4_x - p3_x))) <= 0
                    and (((p3_x - p1_x) * (p2_y - p1_y) - (p3_y - p1_y) * (p2_x - p1_x)) *
                         ((p4_x - p1_x) * (p2_y - p1_y) - (p4_y - p1_y) * (p2_x - p1_x))) <= 0):
                k = 1  # 通过了快速排斥和跨立实验表明两线相交，交点k = 1
            else:
                k = 0  # 通过了快速排斥而未通过跨立实验表明两线不想交，交点k = 0
        else:
            k = 0  # 未通过快速排斥实验，两线不相交，交点k = 0
        return k

    def float_intersection_num(self, *floatlist):
        t = 0
        h = self.get_linedata.rows1 - 1  # linedata的行数-1 即为连线的条数h
        for i in range(h):
            m1 = int(self.get_linedata.line_point[i][0])
            m2 = int(self.get_linedata.line_point[i][1])  # 得到第一条边的头尾两节点对应的重命名（重编号）

            for j in range(i + 1, h):
                m3 = int(self.get_linedata.line_point[j][0])
                m4 = int(self.get_linedata.line_point[j][1])  # 得到第二条边的头尾两节点对应的重命名（重编号）

                p1_x, p1_y = self.get_line_coordinate.get_coordinate(m1, *floatlist)  # 利用重命名（重编号）得到两条边四个节点的坐标
                p2_x, p2_y = self.get_line_coordinate.get_coordinate(m2, *floatlist)
                p3_x, p3_y = self.get_line_coordinate.get_coordinate(m3, *floatlist)
                p4_x, p4_y = self.get_line_coordinate.get_coordinate(m4, *floatlist)

                n = IntersectionPoints.isintersec(self, p1_x, p1_y, p2_x, p2_y, p3_x, p3_y, p4_x, p4_y)
                t += n  # 判断两条边是否相交，若相交啧交点数t加一
                j += 1

            i += 1

        return t  # 返回交点个数t

    def get_intersection_num(self):  # 该函数用于返回交点数目
        return self.d



h = IntersectionPoints('自创数据.xlsx')
h.get_intersection_num()
print(h.get_intersection_num())