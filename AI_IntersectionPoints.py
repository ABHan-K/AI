import AI_ImportingNetworkData as ind
import AI_PointCoordinate as pc


class IntersectionPoints:
    def __init__(self, filename):  # 计算交点数模块
        self.get_linedata = ind.Read(filename)
        self.get_line_coordinate = pc.PointCoordinate
        self.d = 0

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
                print(p1.x, p1.y, p2.x, p2.y, p3.x, p3.y, p4.x, p4.y)
                n = IntersectionPoints.isintersec(self, p1, p2, p3, p4)
                print(n)
                self.d += n  # 判断两条边是否相交，若相交啧交点数d加一
                j += 1

            i += 1

    def isintersec(self, p1, p2, p3, p4):  # 判断两线段是否相交

        # 快速排斥，以l1、l2为对角线的矩形必相交，否则两线段不相交

        if (max(p1.x, p2.x) >= min(p3.x, p4.x)  # 矩形1最右端大于矩形2最左端
                and max(p3.x, p4.x) >= min(p1.x, p2.x)  # 矩形2最右端大于矩形最左端
                and max(p1.y, p2.y) >= min(p3.y, p4.y)  # 矩形1最高端大于矩形最低端
                and max(p3.y, p4.y) >= min(p1.y, p2.y)):  # 矩形2最高端大于矩形最低端

            #  若通过快速排斥则进行跨立实验
            if ((((p4.x - p1.x) * (p4.y - p3.y) - (p4.y - p1.y) * (p4.x - p3.x)) *
                 ((p4.x - p2.x) * (p4.y - p3.y) - (p4.y - p2.y) * (p4.x - p3.x))) <= 0
                    and (((p3.x - p1.x) * (p2.y - p1.y) - (p3.y - p1.y) * (p2.x - p1.x)) *
                         ((p4.x - p1.x) * (p2.y - p1.y) - (p4.y - p1.y) * (p2.x - p1.x))) <= 0):
                k = 1  # 通过了快速排斥和跨立实验表明两线相交，交点k = 1
            else:
                k = 0  # 通过了快速排斥而未通过跨立实验表明两线不想交，交点k = 0
        else:
            k = 0  # 未通过快速排斥实验，两线不相交，交点k = 0
        return k

    def get_intersection_num(self):  # 该函数用于返回交点数目
        return self.d


h = IntersectionPoints('自创数据.xlsx')
h.get_intersection_num()
print(h.get_intersection_num())
