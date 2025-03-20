import numpy as np
import matplotlib.pyplot as plt

# 生成时间轴
t = np.linspace(0, 2*np.pi, 400)  # 连续时间
n = np.arange(0, 10, 1)  # 离散时间

# 生成信号
continuous_signal = np.cos(2 * np.pi * t)  # 余弦信号
discrete_signal = np.heaviside(n, 1)  # 单位阶跃信号

# 创建子图
plt.figure(figsize=(10, 4))

# 绘制连续信号
plt.subplot(1, 2, 1)
plt.plot(t, continuous_signal, 'b', label='cos(2πt)')
plt.title("连续信号")
plt.xlabel("时间 t")
plt.ylabel("幅值")
plt.grid()
plt.legend()

# 绘制离散信号
plt.subplot(1, 2, 2)
plt.stem(n, discrete_signal, basefmt=" ")  
plt.title("离散信号")
plt.xlabel("时间 n")
plt.ylabel("幅值")
plt.grid()
plt.legend()

# 显示图像
plt.tight_layout()
plt.show()

