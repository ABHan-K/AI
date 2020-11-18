import numpy as np
import AI_ImportingNetworkData as ind
import AI_Renumber_CoordinateToFloat as CtF  # todo 预留创建个体文件
import random


class PopIni:
    """
    种群初始化类
    """
    def __init__(self, filename):
        self.net_data = ind.Read(filename)
        self.dynamic_num, self.dynamic_dat = self.net_data.get_data_for_iteration()
        self.pop = np.zeros((self.dynamic_num * 100, self.dynamic_num))  # 初始化节点坐标矩阵
        self.individual = CtF.Renumber_CoordinateToFloat(filename)  # todo 预留创建个体文件
        self.pop_ini()

    def rand_location(self):  # return 横纵坐标
        x = random.randint(0, 24)
        y = random.randint(0, 29)
        return x, y

    def pop_ini(self):  # 初始化初始种群
        for i in range(self.dynamic_num * 100):
            for j in range(self.dynamic_num):
                self.dynamic_dat[j, 1], self.dynamic_dat[j, 2] = self.rand_location()  # 生成个体随机坐标
            self.individual[i] = self.individual.floatlist(self.dynamic_dat)  # todo 预留创建个体文件

    def pop_data_get(self):  # return 种群数量和种群矩阵和动态节点个数
        return self.dynamic_num * 100, self.individual, self.dynamic_num



