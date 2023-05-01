import numpy as np
import plot

from math import *

plot.plot_point([0, 0, 0], color='black')


def xyz_to_lat_long(x, y, z):
    lat = asin(z)
    lon = atan2(y, x)
    return lat, lon, 1


def lat_long_to_xyz(lat, lon):
    x = cos(lat) * cos(lon)
    y = cos(lat) * sin(lon)
    z = sin(lat)
    return x, y, z

# M = np.array(
#     [
#         [1, 0, 0],
#         [0, 1, 0],
#         [0, 0, 1]
#     ]
# )

# p = np.array(
#     [
#         [1, 1, 1]
#     ]
# )


p = [1, 1, 1]
p2 = [0.5, 0.5, 0.5]

l1 = xyz_to_lat_long(*p)
l2 = xyz_to_lat_long(*p2)

plot.plot_point(l1, color='purple')
plot.plot_point(l2, color='orange')

plot.plot_point(p, color='red')
plot.plot_point(p2, color='green')

plot.show()
