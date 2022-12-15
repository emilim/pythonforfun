import matplotlib.pyplot as plt
import numpy as np

MAX_ITER = 80
fig, ax = plt.subplots(1, 1)

def scat(rs, re, cs, ce):
    ax.clear()
    for x in np.linspace(rs, re, q):
        for y in np.linspace(cs, ce, q):
            c = complex(x, y)
            m = mandelbrot(c)
            color = 255 - int(m * 255 / MAX_ITER)
            ax.scatter(x, y, edgecolors='none', color=rgb2hex(color, color, color))


def rgb2hex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(r,g,b)

def on_lims_change(event_ax):
    xl = event_ax.get_xlim()
    yl = event_ax.get_ylim()
    print(xl)
    scat(xl[0], xl[1], yl[0], yl[1])

def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z**2 + c
        n += 1
    return n

RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1
q = 25

for x in np.linspace(RE_START, RE_END, q):
    for y in np.linspace(IM_START, IM_END, q):
        c = complex(x, y)
        m = mandelbrot(c)
        # The color depends on the number of iterations
        color = 255 - int(m * 255 / MAX_ITER)
        ax.scatter(x, y, edgecolors='none', color=rgb2hex(color, color, color))
        
ax.callbacks.connect('xlim_changed', on_lims_change)
plt.show()
