import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_pickle('WOOHOOO.pkl')

ax1 = plt.subplot(111)
ax1.plot(data['time_s'],data['temp_C'])
ax1.set_ylabel('temperature oC')

ax2 = plt.twinx(ax1)
ax2.plot(data['time_s'],data['hum'],'r')
ax2.set_ylabel('humidity %')
ax2.set_xlabel('time s')

plt.figure(2)
plt.scatter(data['temp_C'],data['hum'],c = data['time_s'])
plt.xlabel('temperature oC')
plt.ylabel('humidity %')
plt.show()