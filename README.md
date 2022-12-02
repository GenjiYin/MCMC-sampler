# MCMC-sampler
## HMC 抽样(简易版)
需求: 利用梯度信息, 从任意一个密度函数f(x)(可以是非正则化的正的一阶可导函数) 抽取样本.

### step 1 标量函数对矩阵求导
定义一一阶可导函数关于向量x可导, 可表示为,
$$\frac{\partial f(\mathbf{x})}{\partial \mathbf{x}}=[\frac{\partial f(x_1)}{\partial x_1},...,\frac{\partial f(x_p)}{\partial x_p}]^T$$

p为向量维度. 其python程序设计思路为, 将向量x纵向复制成p*p的方阵A. A加上一个对角阵记为B, 这个对角阵为单位矩阵乘以一个很小的数. 将A、 B列表化, 如此成为了一种列表结构, 这个列表中含有p个一维数组, 最
最后通过map函数计算每个数组对应的函数值, 然后对应index相减除以之前那个很小的数, 即可得到一阶偏导的数值解.

### step 2 HMC算法讲解
初始化一个多元标准正态分布
$$m(\mathbf{u})=\frac{1}{(2\pi)^{\frac{p}{2}}\lambda^p}\exp(-\frac{\mathbf{u}^T\mathbf{u}}{2\lambda})$$
其中
$\lambda>0$
.这一随机变量称为动量, 动量与被抽样的自变量维度是一致的.
1. 给定步长
$\epsilon$
, 初始化
$u_0$
与
$x_0$
.

2. 更新动量与目标函数值
$$u=u_0+\frac{\epsilon}{2}\frac{\partial f(\mathbf{x_0})}{\partial \mathbf{x_0}}$$
$$\mathbf{x} = \mathbf{x}_0 + \epsilon u$$
$$u = u+\frac{\epsilon}{2}\frac{\partial f(\mathbf{x})}{\partial \mathbf{x}}$$
$$p=\frac{m(\mathbf{u})f(\mathbf{x})}{m(\mathbf{u}_0)f(\mathbf{x}_0)}$$
现从0到1之间随机取一个数
$k$
. 若
$k<p$
则令
$x_0=x$、
$u_0=u$
.
