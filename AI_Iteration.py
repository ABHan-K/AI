import numpy as np
import AI_PopulationInitialization as pi
import AI_FitnessCount as fc


class Iteration:
    def __init__(self, filename):
        self.pop_ini = pi.PopIni(filename)
        self.individual_num, self.individual_dat = self.pop_ini.pop_data_get()
        self.fitness = np.zeros(self.individual_num)
        self.dead = np.zeros(self.individual_num)
        self.fit = fc.fitness()  # todo 预留适应度计算
        self.fit_sum = 0

    def fit_count(self):
        for i in range(self.individual_num):
            self.fitness[i] = self.fit.fitcount(self.individual_dat[i])

    def killing(self):
        self.fit_sum = 0
        for i in range(self.individual_num):
            self.fit_sum += self.fitness[i]
