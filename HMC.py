"""
HMC对其中步骤进行细分
"""
import numpy as np

class HMC():
    def __init__(self, f, df, x, lr, labmda_):
        """
        :params f: 被抽样函数(对数化密度函数)
        :params df: f的一阶导
        :params x: 初始值
        :params lr: 学习率
        :params lambda_: 平滑性参数
        """
        self.x = x
        self.f = f
        self.df = df
        self.lr = lr
        self.lambda_ = labmda_

    def gradient_(self, func, x):
        """
        关于x的一阶导
        """
        x_ = np.reshape(x, (1, -1))
        x_ = np.tile(x_, [len(x), 1])
        x_2 = x_ + np.eye(len(x_))*1e-6
        x_2 = list(x_2)
        out1 = np.array(list(map(func, x_)))
        out2 = np.array(list(map(func, x_2)))
        return (out2-out1)/1e-6

    def momentum(self, r):
        """
        动量联合分布(负对数形式)
        """
        return 0.5*r@r
    
    def H(self, x, r):
        out = -self.f(x)+self.momentum(r)
        return out
    
    def iteration(self):
        """
        一次迭代
        """
        x = self.x
        e = self.lr
        r_t = np.random.multivariate_normal(mean=np.zeros_like(x), cov=np.eye(len(x))*self.lambda_)
        if self.df:
            r_0 = r_t + e*self.df(self.x)/2
        else:
            r_0 = r_t + e*self.gradient_(self.x)/2

        x = x + e*r_0/self.lambda_

        if self.df:
            df_x_star = self.df(x)
        else:
            df_x_star = self.gradient_(x)

        r_0 = r_0 + e*df_x_star/2
        u = np.random.uniform(0, 1)
        p = self.H(x, r_0) - self.H(self.x, r_t)
        if np.log(u) < p:
            self.x = x
    
    def sampling(self, num):
        for _ in range(num):
            self.iteration()
        return self.x

if __name__ == '__main__':
    def f(x):
        return -5-5/8*(x-5)@(x-5)
    
    # 可以不设置导函数
    def u(x):
        return -5*(x-5)/8
    h = HMC(f, u, np.array([-1, 3]), 0.8, 20)
    print(h.sampling(40))