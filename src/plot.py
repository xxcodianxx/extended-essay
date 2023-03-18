import matplotlib.pyplot as plt
from quaternion import Quaternion, point_rotate
from mpl_toolkits.mplot3d import axes3d
from math import sin, cos, pi, e

def gen_data():
    V = 5
    X, Y, Z = [], [], []
    for x in range(-V, V+1,):
        for y in range(-V, V+1):
            for z in range(-V, V+1):
                if sum([
                    abs(x) == V, 
                    abs(y) == V, 
                    abs(z) == V]
                ) >= 2:
                    X.append(x)
                    Y.append(y)
                    Z.append(z)
    return X, Y, Z

def vec3_normalized(x, y, z):
    length = (x**2 + y**2 + z**2)**0.5
    return x/length, y/length, z/length

def vec3_mul(v3, k):
    return [v3[0]*k, v3[1]*k, v3[2]*k]

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

def plot_point(p, *args, **kwargs):
    ax.scatter([p[0]], [p[1]], [p[2]], *args, **kwargs)

def plot_line(from_, to_, *args, **kwargs):
    ax.plot([from_[0], to_[0]], [from_[1], to_[1]], [from_[2], to_[2]], *args, **kwargs)


around = vec3_normalized(*[0, 1, 1])
angle = pi / 4

plot_point([0, 0, 0], color='black')
plot_line([0, 0, 0], vec3_mul(around, 10), color='green')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')              # type: ignore

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)            # type: ignore
X, Y, Z = gen_data()
ax.scatter(X, Y, Z)

X_R, Y_R, Z_R = [], [], []

for x, y, z in zip(X, Y, Z):
    p = point_rotate([x, y, z], around, angle)
    X_R.append(p[0])
    Y_R.append(p[1])
    Z_R.append(p[2])

ax.scatter(X_R, Y_R, Z_R, color='red')

ax.set_proj_type('persp', 0.2)   # type: ignore
ax.set_box_aspect([1, 1, 1])     # type: ignore

plt.show()