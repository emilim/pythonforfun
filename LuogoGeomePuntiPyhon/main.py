import numpy as np
import matplotlib.colors as mcolors
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
import math
import PySimpleGUI as sg

def circle(x, y, a, b):
    zInsieme = x ** 2 + y ** 2
    xScat = np.array([[]])
    yScat = np.array([[]])

    for i in range(int(math.sqrt(x.size))):
        for j in range(int(math.sqrt(x.size))):
            if x[i][j]**2 + y[i][j]**2 < 1.05 and x[i][j]**2 + y[i][j]**2 > 0.95:
                yScat = np.append(yScat, y[i][j])
                xScat = np.append(xScat, x[i][j])
    return xScat, yScat, zInsieme, 1

def line(x, y, a, b):
    zInsieme = x - y
    xScat = np.array([[]])
    yScat = np.array([[]])
    
    for i in range(int(math.sqrt(x.size))):
        for j in range(int(math.sqrt(x.size))):
            if x[i][j] - y[i][j] < 0.05 and x[i][j]- y[i][j] > -0.05:
                yScat = np.append(yScat, y[i][j])
                xScat = np.append(xScat, x[i][j])
    return xScat, yScat, zInsieme, 0

def parable(x, y, a, b):
    zInsieme = x**2 + x - y
    xScat = np.array([[]])
    yScat = np.array([[]])
    for i in range(int(math.sqrt(x.size))):
        for j in range(int(math.sqrt(x.size))):
            if x[i][j]**2 + x[i][j] - y[i][j] < 0.05 and x[i][j]**2 + x[i][j] - y[i][j] > -0.05:
                yScat = np.append(yScat, y[i][j])
                xScat = np.append(xScat, x[i][j])
    return xScat, yScat, zInsieme, 0

def hyperbola(x, y, a, b):
    zInsieme = (x ** 2 / a ** 2) - (y ** 2 / b ** 2)
    xScat = np.array([[]])
    yScat = np.array([[]])

    for i in range(int(math.sqrt(x.size))):
        for j in range(int(math.sqrt(x.size))):
            if (x[i][j]**2 / a ** 2) - (y[i][j]**2 / b**2) < 1.05 and (x[i][j]**2 / a ** 2) - (y[i][j]**2 / b**2) > 0.95:
                yScat = np.append(yScat, y[i][j])
                xScat = np.append(xScat, x[i][j])
    return xScat, yScat, zInsieme, 1

def onde(x, y, a, b):
    zInsieme = np.sin(x ** 2 + y ** 2) / (x**2 + y**2)
    xScat = np.array([[]])
    yScat = np.array([[]])
    for i in range(int(math.sqrt(x.size))):
        for j in range(int(math.sqrt(x.size))):
            if np.sin(x[i][j] ** 2 + y[i][j] ** 2) / (x[i][j]**2 + y[i][j]**2) < 0.05 and np.sin(x[i][j] ** 2 + y[i][j] ** 2) / (x[i][j]**2 + y[i][j]**2) > -0.05:
                yScat = np.append(yScat, y[i][j])
                xScat = np.append(xScat, x[i][j])
    return xScat, yScat, zInsieme, 0

def sigmoid(x, y, a, b):
    zInsieme = (1 / (1 + (math.e ** -x))) - y
    xScat = np.array([[]])
    yScat = np.array([[]])
    for i in range(int(math.sqrt(x.size))):
        for j in range(int(math.sqrt(x.size))):
            if (1 / (1 + (math.e ** -x[i][j]))) - y[i][j] < 0.05 and (1 / (1 + (math.e ** -x[i][j]))) - y[i][j] > -0.05:
                yScat = np.append(yScat, y[i][j])
                xScat = np.append(xScat, x[i][j])
    return xScat, yScat, zInsieme, 1

X = np.linspace(-6, 6, 150)
Y = np.linspace(-6, 6, 150)
x, y = np.meshgrid(X, Y)

xScat, yScat, z, h = sigmoid(x, y, 1, 2)







matplotlib.use("TkAgg")

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg

# Define the window layout
layout = [
    [sg.Text("Plot test")],
    [sg.Canvas(key="-CANVAS-")],
    [sg.Button("Ok")],
]

# Create the form and show it without the plot
window = sg.Window(
    "Matplotlib Single Graph",
    layout,
    location=(0, 0),
    finalize=True,
    element_justification="center",
    font="Helvetica 18",
)

import matplotlib.pyplot as plt
#UI GRAPH
fig, axes = plt.subplots(nrows=2, ncols=2)
ax = plt.subplot(224, projection='3d')

#2dMesh
im = axes[0][0].pcolormesh(x, y, z.reshape(x.shape), shading='auto')

#2dEasyPlot
axes[1][0].scatter(xScat, yScat, s = 1)
axes[1][0].grid(True)

#3dGraph
ax.view_init(elev=15., azim=50)
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='viridis', edgecolor='none', alpha=0.8)
ax.scatter(xScat, yScat, h)


#STUFF FOR THE WORK
fig.subplots_adjust(right=0.8)
cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
fig.colorbar(im, cax=cbar_ax)

# Add the plot to the window
draw_figure(window["-CANVAS-"].TKCanvas, fig)
fig.savefig('temp.png', dpi=fig.dpi)

event, values = window.read()

window.close()
