import numpy as np
import AI_PopulationInitialization as pi
import AI_FitnessCount as fc  # todo 预留适应度计算
from random import randint


class Iteration:
    def __init__(self, filename):
        self.pop_ini = pi.PopIni(filename)
        self.individual_num, self.individual_dat, self.dynamic_num = self.pop_ini.pop_data_get()
        self.fitness = np.zeros(self.individual_num)
        self.dead = np.zeros(self.individual_num)
        self.fit = fc.fitness()  # todo 预留适应度计算
        self.pick_list = np.zeros(self.individual_num * 1 / 3)
        self.dead_list = np.zeros(self.individual_num * 2 / 3)

    def fit_count(self):
        for i in range(self.individual_num):
            self.fitness[i] = self.fit.fitcount(self.individual_dat[i])
        if 0 in self.fitness:
            return np.where(self.fitness <= 0)
        else:
            return -1

    def compare(self, a, b, c):
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
        a = self.fit_count()
        while a == -1:
            self.killing()
            a = randint(0, self.individual_num * 1 / 3 - 1)
            b = randint(0, self.individual_num * 1 / 3 - 1)
            self.reproduction(a, b)
            a = self.fit_count()

        return self.individual_dat[a[0]]
