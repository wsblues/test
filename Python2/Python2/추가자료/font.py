# -*- coding: euc-kr -*-
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(np.random.randn(1000).cumsum())


ticks = ax.set_xticks([0, 250, 500, 750, 1000])
labels = ax.set_xticklabels([u'�ϳ�',u'��',u'��',u'��',u'�ټ�'], rotation=30, fontsize='small')
matplotlib.rc('font',family='Dotum')
fig.show()
