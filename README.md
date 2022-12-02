# MCMC-sampler
## HMC 抽样
需求: 利用梯度信息, 从任意一个密度函数$\pi(\mathbf{x})$(可以是非正则化的正的一阶可导函数) 抽取样本.

### step 1 标量函数对矩阵求导
定义一一阶可导函数关于向量x可导, 可表示为,
$$\frac{\partial f(\mathbf{x})}{\partial \mathbf{x}}=[\frac{\partial f(x_1)}{\partial x_1},...,\frac{\partial f(x_p)}{\partial x_p}]^T$$

p为向量维度. 其python程序设计思路为, 将向量x纵向复制成p*p的方阵A. A加上一个对角阵记为B, 这个对角阵为单位矩阵乘以一个很小的数. 将A、 B列表化, 如此成为了一种列表结构, 这个列表中含有p个一维数组, 最
最后通过map函数计算每个数组对应的函数值, 然后对应index相减除以之前那个很小的数, 即可得到一阶偏导的数值解.

### step 2 HMC算法讲解
初始化一个
