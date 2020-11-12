import numpy as np
import AI_ImportingNetworkData as ind
import AI_CreateIndividual as ci  # todo 预留创建个体文件
import random


class PopIni:
    def __init__(self, filename):
        self.net_data = ind.Read(filename)
        self.dynamic_num, self.dynamic_dat = self.net_data.bus_data()
        self.pop = np.zeros((self.dynamic_num * 100, self.dynamic_num))  # 初始化节点坐标矩阵
        self.individual = ci.individual()  # todo 预留创建个体文件

    def rand_location(self):  # return 横纵坐标
        x = random.randint(0, 24)
        y = random.randint(0, 29)
        return x, y

    def pop_ini(self):
        for i in range(self.dynamic_num * 100):
            for j in range(self.dynamic_num):
                self.dynamic_dat[j, 1], self.dynamic_dat[j, 2] = self.rand_location()  # 生成个体随机坐标
            self.individual[i] = self.individual.DNA(self.dynamic_dat) # todo 预留创建个体文件
