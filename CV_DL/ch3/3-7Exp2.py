# 1차원, 2차원 가우시안 함수 그리기 -> GPT 작성
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, multivariate_normal

# 1차원 가우시안 함수
x = np.linspace(-5, 5, 1000)
sigma_1d = 1.0
y_1d = norm.pdf(x, scale=sigma_1d)

plt.figure(figsize=(8, 4))
plt.plot(x, y_1d, label=f'1D Gaussian (σ={sigma_1d})')
plt.title('1D Gaussian Function')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()

# 2차원 가우시안 함수
sigma_2d = 1.0
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
pos = np.dstack((x, y))
rv = multivariate_normal([0, 0], [[sigma_2d**2, 0], [0, sigma_2d**2]])
z = rv.pdf(pos)

plt.figure(figsize=(8, 6))
plt.contourf(x, y, z, levels=50, cmap='viridis')
plt.title('2D Gaussian Function')
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar(label='Probability Density')
plt.grid(True)
plt.show()