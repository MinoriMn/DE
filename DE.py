#!/usr/bin/env python
# coding: utf-8

# # DE

# In[4]:


import random
import numpy as np


# In[14]:


class DE:
    # D入力次元数, N集団サイズ, up/lo_lim上限, func評価関数, crossover交叉法, CR交叉率, Fケーリング係数
    def __init__(self, D, N, up_lim, lo_lim, func, crossover, CR, F):
        self.D = D
        self.N = N
        self.up_lim = up_lim
        self.lo_lim = lo_lim
        self.func = func
        self.crossover = crossover
        self.CR = CR
        self.F = F
        
    def init_phase(self):
        self.xs = np.array([[self.lo_lim + random.random() * (self.up_lim - self.lo_lim) for _j in range(self.D)] for _i in range(self.N)])
        
    def solution_search_phase(self):
        # 評価値算出
        self.evaluation = [self.func(*x) for x in self.xs]
        
        # 子生成
        for i in range(self.N):
            # rand/1
            p = list(range(self.N))
            p.pop(i)
            p = random.sample(p, 3)
            # 突然変異個体
            x_i_dash = [self.xs[p[0]] + self.F * (self.xs[p[1]] - self.xs[p[2]])]
            
            # /bin
            ys = []
            r = random.randrange(self.D)
            for j in range(self.D):
                if (j == r) and (random.random() < self.CR):
                    ys.append(x_i_dash)
                else:
                    ys.append(list(self.xs[i]))
                    
        # 子の評価値算出
        ys_evaluation = [self.func(*y) for y in ys]
        # 親子選択
        self.xs = np.array([self.xs[i] if self.evaluation[i] >= ys_evaluation[i] else ys[i] for i in range(self.N)])


# In[ ]:




