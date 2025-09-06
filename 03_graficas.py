
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 20)
y = x ** 2
y2 = x ** 3

# plt.plot(x,y,'ro--')
# plt.plot(x,y2,'b-')
# plt.plot(x,y,'b+')

# plt.subplot(1,2,1)  #rows - columns - plot refering to. 
# plt.plot(x,y,'r')
# plt.subplot(1,2,2)
# plt.plot(x,y2,'b')

# fig = plt.figure()
# ax1 = fig.add_axes([0.1, 0.1, 0.85, 0.85])#left - buttom, width, heigth
# ax2 = fig.add_axes([0.35, 0.5, 0.3, 0.3])
# ax1.plot(x,y)
# ax2.plot(x, y2)
# ax1.set_title('Grafica 1')
# ax2.set_title('Grafica 2')


# fig, axes = plt.subplots(nrows=1, ncols=2)
# plt.tight_layout()
# axes[0].plot(x,y,'r')
# axes[1].plot(x,y2,'bo')


# fig = plt.figure(figsize=(5,5), dpi=200) #width, higth  inches
# ax = fig.add_axes([0.1,0.1,0.8,0.8])
# ax.plot(x,y, 'r', label='X cuadrada')
# ax.plot(x,y2, 'go', label='X cúbica')
# ax.legend(loc=(0.2,0.7))
# fig.savefig('./imagen.png', dpi=200)


# fig = plt.figure(figsize=(5,5), dpi=200) #width, higth  inches
# ax = fig.add_axes([0.1,0.1,0.8,0.8])
# ax.plot(x,y, color='#FF8C88', linewidth=4, linestyle='--') # -. : solid


# fig = plt.figure(figsize=(5,5), dpi=200) #width, higth  inches
# ax = fig.add_axes([0.1,0.1,0.8,0.8])
# ax.plot(x,y, color='purple', lw=2, ls='-', marker='o', markersize=20, 
#         markerfacecolor='yellow', markeredgewidth=3, markeredgecolor='green') # -. : solid
# plt.show()

'''
Referencias: 
http://www.matplotlib.org - The project web page for matplotlib.
https://github.com/matplotlib/matplotlib - The source code for matplotlib.
http://matplotlib.org/gallery.html - A large gallery showcaseing various types of plots matplotlib can create. Highly recommended!
'''
