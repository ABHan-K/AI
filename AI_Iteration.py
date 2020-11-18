import numpy as np
import AI_PopulationInitialization as pi
import AI_IntersectionPoints as ItP  # todo 预留适应度计算
from random import randint


class Iteration:
    """
    *运算迭代
    *计划每一代仅保留三分之一的种群个体数量
    """

    def __init__(self, filename):
        self.pop_ini = pi.PopIni(filename)
        self.individual_num, self.individual_dat, self.dynamic_num = self.pop_ini.pop_data_get()
        self.fitness = np.zeros(self.individual_num)
        self.dead = np.zeros(self.individual_num)
        self.fit = ItP.IntersectionPoints(filename)  # todo 预留适应度计算
        self.pick_list = np.zeros(self.individual_num * 1 / 3)
        self.dead_list = np.zeros(self.individual_num * 2 / 3)

    def fit_count(self, j):
        """
        :param j: 允许交点个数
        :return:当存在无交点图时 个体编号
                当存在交点图时   -1
        """
        for i in range(self.individual_num):
            self.fitness[i] = self.fit.float_intersection_num(self.individual_dat[i])
        m = 0
        while m <= j:
            if m in self.fitness:
                return np.where(self.fitness <= m)
            m += 1
        return -1

    def compare(self, a, b, c):
        """
        :param a: 个体a
        :param b: 个体b
        :param c: 个体c
        :return: 最适应个体
        """
        if self.individual_dat[a] < self.individual_dat[b]:
            if self.individual_dat[a] < self.individual_dat[c]:
                return a
            else:
                return c
        else:
            if self.individual_dat[b] < self.individual_dat[c]:
                return b
            else:
                return c

    def killing(self):
        """
        每一次选取3个个体进行竞争
        失败个体放回等待选取
        直至选择足够数量后停止
        """
        i = 0
        while i < self.individual_num / 3:
            a = randint(0, self.individual_num - 1)
            b = randint(0, self.individual_num - 1)
            c = randint(0, self.individual_num - 1)
            pick = self.compare(a, b, c)
            if pick not in self.pick_list:
                self.pick_list[i] = pick
                i += 1
        i = 0
        for dead in range(self.individual_num - 1):
            if dead not in self.pick_list:
                self.dead_list[i] = dead
                i += 1

    def reproduction(self, a, b):
        """
        万分之一的概率基因突变
        :param a: 父个体
        :param b: 母个体
        :return: 子个体
        """
        father = self.individual_dat[a]
        mother = self.individual_dat[b]
        son = np.zeros(self.dynamic_num - 1)
        for i in range(self.dynamic_num - 1):
            if randint(0, 10000) == 1:
                son[i] = randint(0, 24) + randint(0, 30) / 100
            elif randint(0, 1) == 0:
                son[i] = mother[i]
            else:
                son[i] = father[i]
        return son

    def main(self):
        """
        param: i : 迭代次数
        param: j : 允许交点个数
        :return: 迭代结束最优个体
        """
        i = 0
        j = 0

        a = self.fit_count(j)
        while a == -1:
            self.killing()
            a = randint(0, self.individual_num * 1 / 3 - 1)
            b = randint(0, self.individual_num * 1 / 3 - 1)
            self.reproduction(a, b)
            a = self.fit_count(j)
            i += 1
            if not (i % 20):
                j += 1

        return self.individual_dat[a[0]]
