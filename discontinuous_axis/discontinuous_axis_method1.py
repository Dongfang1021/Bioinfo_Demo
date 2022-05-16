import matplotlib.pylab as plt
import numpy as np

# If you're not familiar with np.r_, don't worry too much about this. It's just 
# a series with points from 0 to 1 spaced at 0.1, and 9 to 10 with the same spacing.
x = np.r_[0:1:0.1, 9:10:0.1]
y = np.sin(x)

fig,(ax,ax2) = plt.subplots(1, 2, sharey=True)

# plot the same data on both axes
ax.plot(x, y, 'bo')
ax2.plot(x, y, 'bo')

# zoom-in / limit the view to different portions of the data
ax.set_xlim(0,1) # most of the data
ax2.set_xlim(9,10) # outliers only

# hide the spines between ax and ax2
ax.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax.yaxis.tick_left()
ax.tick_params(labeltop='off') # don't put tick labels at the top
ax2.yaxis.tick_right()

# Make the spacing between the two axes a bit smaller
plt.subplots_adjust(wspace=0.15)
plt.savefig("discontinuous_axis_method1.png")