"""calculate gravity shape"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

pritn("I am gonna show you gravity shape")

# Создаем плоскую сетку
x = np.arange(0, 11, 1)  # от 0 до 10 включительно
y = np.arange(0, 11, 1)
X, Y = np.meshgrid(x, y)

# Вычисляем значения суммы в каждой точке
S = X + Y

# Центр сетки (полюс)
center_x, center_y = 5, 5

# Смещение от центра
dx = X - center_x
dy = Y - center_y

# Полярные координаты на плоскости
r = np.sqrt(dx**2 + dy**2)
phi = np.arctan2(dy, dx)

# Максимальное расстояние от центра (до угловых точек)
max_r = np.sqrt(5**2 + 5**2)  # 5√2 ≈ 7.07

# Нормируем расстояние от 0 до 1
r_norm = r / max_r

# Вычисляем полярный угол θ (от 0 до π/2)
theta = r_norm * (np.pi / 2)

# Преобразуем в декартовы координаты на сфере радиуса 1
R = 1
x_sph = R * np.sin(theta) * np.cos(phi)
y_sph = R * np.sin(theta) * np.sin(phi)
z_sph = R * np.cos(theta)

# Визуализация
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Отображаем точки с цветом, соответствующим значению S
scatter = ax.scatter(
    x_sph, y_sph, z_sph,
    c=S.flatten(),
    cmap='viridis',
    s=50,
    edgecolor='k'
)

# Настройка меток и заголовка
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Проекция сетки X+Y на сферу')

# Цветовая шкара
cbar = plt.colorbar(scatter, pad=0.1)
cbar.set_label('Значение X + Y')

# Установка одинакового масштаба по осям
ax.set_box_aspect([1, 1, 1])

# Угол обзора
ax.view_init(elev=20, azim=30)

plt.show()
