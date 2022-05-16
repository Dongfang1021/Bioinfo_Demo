import matplotlib.pylab as plt
import numpy as np
import matplotlib.gridspec as gridspec

x = np.r_[0:1:0.1, 9:10:0.1]
y = np.sin(x)

n = 5; m = 1;
gs = gridspec.GridSpec(1,2, width_ratios = [n,m])

plt.figure(figsize=(10,8))

ax = plt.subplot(gs[0,0])
ax2 = plt.subplot(gs[0,1], sharey = ax)
plt.setp(ax2.get_yticklabels(), visible=False)
plt.subplots_adjust(wspace = 0.1)

ax.plot(x, y, 'bo')
ax2.plot(x, y, 'bo')

ax.set_xlim(0,1)
ax2.set_xlim(10,8)

# hide the spines between ax and ax2
ax.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax.yaxis.tick_left()
ax.tick_params(labeltop='off') # don't put tick labels at the top
ax2.yaxis.tick_right()

d = .015 # how big to make the diagonal lines in axes coordinates
# arguments to pass plot, just so we don't keep repeating them
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)

on = (n+m)/n; om = (n+m)/m;
ax.plot((1-d*on,1+d*on),(-d,d), **kwargs) # bottom-left diagonal
ax.plot((1-d*on,1+d*on),(1-d,1+d), **kwargs) # top-left diagonal
kwargs.update(transform=ax2.transAxes) # switch to the bottom axes
ax2.plot((-d*om,d*om),(-d,d), **kwargs) # bottom-right diagonal
ax2.plot((-d*om,d*om),(1-d,1+d), **kwargs) # top-right diagonal
plt.savefig("discontinuous_axis_method5.png")