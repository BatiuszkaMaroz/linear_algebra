# %%
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# %%[markdown]
# ### 2D vector

# %%
%matplotlib widget

# 2-dimensional vector
v2 = [2, 3]

# plot marker
plt.plot(v2[0], v2[1], '*')
# plot vector
# [x0, x1] [y0, y1]
plt.plot([0, v2[0]], [0, v2[1]])
# plot x, y axes
size = 4
plt.plot([-size, size], [0, 0], 'k--')
plt.plot([0, 0], [-size, size], 'k--')

# square plot
plt.axis('square')
# divide plot
plt.axis((-size, size, -size, size))

plt.grid()
plt.show()

# %%[markdown]
# ### 3D vector

# %%
%matplotlib widget

# 3-dimensional vector
v3 = [1, 1, 1]

# row to column (or vice-versa):
v3t = np.transpose(v3)

plt.figure(figsize=(5, 5))
ax = plt.axes(projection='3d')

# plot vector
ax.plot([0, v3[0]], [0, v3[1]], [0, v3[2]], linewidth=3)
# plot x, y, z axes
size = 4
ax.plot([0, 0], [0, 0], [-size, size], 'k--')
ax.plot([0, 0], [-size, size], [0, 0], 'k--')
ax.plot([-size, size], [0, 0], [0, 0], 'k--')

plt.show()

# %%[markdown]
# ### Vector addition

# %%
%matplotlib widget

# two vectors in R2
v1 = np.array([3, -1])
v2 = np.array([2, 4])

v3 = v1 + v2

# plot them
plt.plot([0, v1[0]], [0, v1[1]], 'b', label='v')
# plot v2 moved by v1 on x and y axes
plt.plot([0, v2[0]] + v1[0], [0, v2[1]] + v1[1], 'r', label='w')
plt.plot([0, v3[0]], [0, v3[1]], 'y', label='v + w')
# plot axes
size = 8
plt.plot([-size, size], [0, 0], 'k--')
plt.plot([0, 0], [-size, size], 'k--')

plt.axis('square')
plt.axis((-size, size, -size, size))

plt.grid()
plt.legend()
plt.show()

# %%[markdown]
# ### Vector scalar multiplication

# %%
%matplotlib widget

v1 = np.array([2, 1])
v2 = -3 * v1

plt.plot([0, v1[0]], [0, v1[1]], 'b', label='v1')
plt.plot([0, v2[0]], [0, v2[1]], 'r:', label='v2')

axlim = max([max(abs(v1)), max(abs(v2))]) * 1.5
plt.axis('equal')
plt.axis((-axlim, axlim, -axlim, axlim))
plt.grid()
plt.legend()
plt.show()

# %%[markdown]
# ### Vector dot product
# A<sup>T</sup>B

# %%
