#!/usr/bin/python3
import sys
import time
import numpy as np
import pandas as pd
#import Adafruit_DHT as adht
from sht_sensor import Sht
# https://pypi.org/project/sht-sensor/

# ========================================
# https://docs.microsoft.com/en-us/windows/iot-core/learn-about-hardware/pinmappings/pinmappingsrpi
volt_read = '3.5V' # Sht.VDDLevel.vdd_5v
print(volt_read)
yellow_clock_pin = 21
blue_data_pin = 17
sht = Sht(yellow_clock_pin, blue_data_pin, voltage=volt_read)
T_C = sht.read_t()
rh = sht.read_rh(T_C)
dew_point = sht.read_dew_point(T_C, rh)
print(T_C,rh,dew_point)
print('======= RECORDING NOW! ==========')

# ========================================

temp_ls = []
hum_ls = []
time_ls = []
time0 = time.time()

t_now=0.0
t_stop = 20.0
while t_now<=t_stop:
#    try:
    t = time.time()
    t_now = round(t-time0,4)
    T_C = round(sht.read_t(),3)
    rh = round(sht.read_rh(T_C),3)
    time_ls.append(t_now)
    temp_ls.append(T_C)
    hum_ls.append(rh)
    print(t_now,T_C,rh)
#    except KeyboardInterrupt:
print('stopped recording, now saving pickle')

time_s = np.array(time_ls)
temp_C = np.array(temp_ls)
hum = np.array(hum_ls)

# =========================================
# write to panda and pickle it !

data = pd.DataFrame({'time_s':time_s, 'temp_C':temp_C, 'hum':hum})
data.to_pickle('./WOOHOOO.pkl')



