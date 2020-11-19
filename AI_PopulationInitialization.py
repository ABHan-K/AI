import numpy as np
import AI_ImportingNetworkData as ind
import AI_Renumber_CoordinateToFloat as CtF  # todo 预留创建个体文件
from random import randint
from numba import jit


@jit(nopython=True)
def rand_location():  # return 横纵坐标
    x = randint(0, 24)
    y = randint(0, 29)
    return x, y


class PopIni:
    """
    种群初始化类
    """

    def __init__(self, filename):
        self.net_data = ind.Read(filename)
        self.dynamic_num = self.net_data.get_data_for_iteration()
        self.dynamic_dat = np.zeros((self.dynamic_num, 2), dtype=np.int)
        self.pop = np.zeros((self.dynamic_num * 100, self.dynamic_num))  # 初始化节点坐标矩阵
        self.individual = CtF.Renumber_CoordinateToFloat(filename)  # todo 预留创建个体文件
        self.pop_ini()

    def pop_ini(self):  # 初始化初始种群
        for i in range(self.dynamic_num * 90):
            for j in range(self.dynamic_num):
                self.dynamic_dat[j][0], self.dynamic_dat[j][1] = rand_location()  # 生成个体随机坐标

            self.pop[i] = self.individual.floatlist(self.dynamic_dat)  # todo 预留创建个体文件

    def pop_data_get(self):  # return 种群数量和种群矩阵和动态节点个数
        return self.dynamic_num * 90, self.pop, self.dynamic_num
