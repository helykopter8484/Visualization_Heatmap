
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.style.use('ggplot')       # Use ggplot style plots*


# Pair Names:

Row_labels = (
	'A - B', 
	'B - C',
	'B - F',
	'B - M',
	'B - M',
	'B - H',
	'B - N',
	'B - K',
	'B - Z',
	'C - M',
	'C - H',
	'C - K',
	'C - Z',
	'C - F',
	'Z - P'
)

# Averages
data = (
	(94.59, 94.81, 95.09, 94.76, 94.89, 95.17, 94.01, 93.78, 93.78, 95.43, 95.26, 95.46, 92.64, 94.78, 95.12),
	(84.89, 84.06, 85.89, 85.18, 84.57, 86.22, 75.02, 76.38, 74.96, 86.72, 85.61, 86.79, 79.58, 83.65, 85.49),
	(57.33, 56.27, 58.98, 57.43, 56.81, 59.13, 53.54, 53.5, 53.47, 60.13, 57.75, 59.6, 55.37, 56.41, 57.18),
	(90.45, 90.62, 91.45, 90.41, 90.95, 91.18, 86.36, 86.34, 86.39, 90.77, 90.12, 90.22, 86.15, 88.67, 89.86),
	(91.42, 92.15, 92.34, 91.56, 92.47, 92.23, 86.9, 86.99, 86.91, 92.37, 92.28, 92.09, 88.19, 91.23, 91.65),
	(91.81, 92.51, 92.67, 91.75, 92.53, 92.38, 87.39, 87.28, 87.42, 93.01, 92.53, 92.76, 88.72, 91.59, 92.43),
	(78.61, 76.39, 79.78, 78.87, 77.01, 80.21, 71.22, 72.39, 71.28, 80.69, 78.6, 80.55, 72.2, 75.66, 78.58),
	(91.83, 92.13, 92.71, 91.97, 92.53, 92.65, 89.56, 89.51, 89.56, 92.95, 92.65, 92.87, 89.2, 91.64, 92.27),
	(94.01, 93.77, 94.34, 94.11, 94.16, 94.41, 93.65, 93.47, 93.45, 94.51, 94.37, 94.48, 90.72, 93.73, 94.19),
	(86.99, 87.77, 88.3, 87.26, 88.04, 88.38, 85.31, 85.21, 85.32, 88.81, 88.38, 88.63, 83.22, 86.7, 87.71),
	(77.37, 78.79, 80.57, 77.72, 79.47, 80.72, 69.12, 71.36, 69.09, 80.49, 79.7, 80.49, 72.45, 76.38, 78.22),
	(71.23, 69.52, 72.91, 71.42, 69.79, 73.44, 62.17, 65.59, 62.28, 73.76, 71.51, 73.71, 65.46, 68.12, 70.71),
	(89.34, 89.49, 90.39, 89.62, 89.81, 90.6, 85.77, 85.78, 85.74, 90.64, 90.27, 90.57, 86.19, 88.82, 89.68),
	(92.57, 92.62, 93.06, 92.67, 92.85, 93.22, 91.77, 91.61, 91.62, 93.55, 93.14, 93.52, 89.88, 92.37, 92.95),
	(78.71, 81.0, 81.4, 78.99, 81.33, 81.69, 62.51, 67.14, 63.7, 83.22, 83.16, 83.03, 76.9, 80.65, 81.52)
)


# Standard Deviations
stdevs = (
	(0.26, 0.34, 0.28, 0.25, 0.35, 0.24, 0.31, 0.33, 0.33, 0.22, 0.37, 0.24, 0.6, 0.36, 0.32),
	(0.8, 1.1, 0.95, 0.78, 0.74, 0.88, 1.43, 0.55, 1.52, 0.69, 0.89, 0.75, 1.12, 1.08, 0.88),
	(1.13, 1.14, 1.31, 1.1, 0.99, 1.19, 1.09, 0.8, 0.94, 1.03, 1.3, 1.1, 0.9, 1.08, 0.89),
	(0.61, 0.48, 0.53, 0.7, 0.43, 0.48, 0.51, 0.49, 0.51, 0.45, 0.41, 0.33, 0.68, 0.46, 0.4),
	(0.58, 0.64, 0.54, 0.53, 0.58, 0.45, 0.44, 0.53, 0.43, 0.41, 0.43, 0.45, 0.62, 0.51, 0.51),
	(0.39, 0.54, 0.43, 0.31, 0.48, 0.35, 0.87, 0.77, 0.84, 0.43, 0.66, 0.45, 0.68, 0.47, 0.5),
	(0.98, 1.05, 0.95, 0.97, 0.62, 0.89, 0.89, 0.84, 0.93, 0.83, 1.08, 0.83, 1.29, 1.12, 0.9),
	(0.35, 0.48, 0.39, 0.37, 0.38, 0.32, 0.55, 0.6, 0.59, 0.4, 0.54, 0.46, 0.56, 0.5, 0.59),
	(0.49, 0.41, 0.39, 0.47, 0.39, 0.38, 0.35, 0.34, 0.36, 0.35, 0.48, 0.32, 0.5, 0.56, 0.51),
	(0.5, 0.51, 0.47, 0.51, 0.44, 0.42, 0.51, 0.59, 0.51, 0.46, 0.62, 0.48, 0.78, 0.5, 0.55),
	(1.17, 0.94, 0.79, 1.17, 0.72, 0.72, 0.64, 0.67, 0.62, 0.71, 1.01, 0.58, 1.07, 0.81, 0.81),
	(1.12, 1.03, 1.1, 1.1, 1.0, 1.07, 0.59, 0.84, 0.74, 1.03, 0.85, 0.9, 1.17, 0.96, 1.19),
	(0.55, 0.57, 0.42, 0.48, 0.69, 0.44, 0.41, 0.41, 0.4, 0.39, 0.51, 0.4, 0.64, 0.53, 0.52),
	(0.5, 0.47, 0.39, 0.5, 0.38, 0.39, 0.48, 0.49, 0.48, 0.45, 0.42, 0.41, 0.61, 0.51, 0.56),
	(0.91, 0.82, 0.82, 0.85, 0.77, 0.71, 1.55, 1.08, 1.37, 0.63, 0.7, 0.61, 0.87, 0.89, 0.95)
	)

Column_labels = (
	"Item-A",
	"Item-B",
	"Item-V",
	"Item-D",
	"Item-E",
	"Item-F",
	"Item-G",
	"Item-H",
	"Item-I",
	"Item-J",
	"Item-K",
	"Item-L",
	"Item-M",
	"Item-N",
	"Item-O",
	)

# Set data dimensions.
D_array = np.asarray(data).reshape((15,15))
Stdev_A = np.asarray(stdevs).reshape((15,15))

# Plot.
fig, ax = plt.subplots()
heatmap = ax.pcolor(D_array, cmap = plt.cm.winter, alpha = 1.0, facecolor='w', edgecolor='k')
for y in range(Stdev_A.shape[0]):
    for x in range(Stdev_A.shape[1]):
        plt.text(x + 0.5, y + 0.5, '%.2f' % Stdev_A[y, x], horizontalalignment='center',
                 verticalalignment='center', size = 8.5)
                 
# Set the format for the plot.
fig = plt.gcf()
fig.set_size_inches(15,10)

# Turn off the frame.
ax.set_frame_on(True)

# Put the axis ticks in the moddle of each cell.
ax.set_yticks(np.arange(D_array.shape[0]) + 0.5, minor=False)
ax.set_xticks(np.arange(D_array.shape[1]) + 0.5, minor=False)

# Invert the axis if required.
# ax.invert_yaxis()

v = np.linspace(0, 100, 100, endpoint=False )
cb = fig.colorbar(heatmap, ticks = v, pad = 0.02)#, orientation = 'vertical')#, shrink = 1.0)#, cax = cax)
cb.ax.set_ylabel('Plot for generating Heatmap using Matplotlib. Background color represents averages, and values represent std. dev. ', fontsize = 9.5)
cb.ax.tick_params(labelsize = 8.5) 

# Adding tick labels.
ax.set_xticklabels(Column_labels, minor = False, fontsize = 8.5)
ax.set_yticklabels(Row_labels, minor = False, fontsize = 8.5)
ax.set_aspect(1.0/ax.get_data_ratio())

# Set the x axis
plt.xticks()
plt.ylim(0,15)
plt.tight_layout()

# Adding plot title.
# plt.title("Python3 Heatmap: Matplotlib.".upper(), fontsize = 7.5)
ax.grid(False)

# Turn off all the ticks
ax = plt.gca()

for t in ax.xaxis.get_major_ticks():
    t.tick1On = False
    t.tick2On = False
for t in ax.yaxis.get_major_ticks():
    t.tick1On = False
    t.tick2On = False

plt.savefig('heatmap.png', dpi = 500)
# plt.show()
