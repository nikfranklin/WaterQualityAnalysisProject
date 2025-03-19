import numpy as np
import matplotlib.pyplot as plt

# Importing the Data

data =  np.genfromtxt("BKB_WaterQualityData_2020084.csv",
                            skip_header=1, skip_footer=3, delimiter=",", usecols=(2,3,8),
                            dtype=[('readdate','U10'),('salinity',float),('watertemp',float)],
                            names=['readdate','salinity','watertemp'], 
                            missing_values={'salinity':'','watertemp':''}, 
                            filling_values={'salinity':0.0,'watertemp':0.0},
                            )

fig, (ax_sal,ax_sec) = plt.subplots(2,1, figsize=(10,7), sharex='all', layout='constrained')
plt.xticks(np.arange(0, 50, step=2))
plt.yticks(np.arange(0, 50, step=5,))
x = data['readdate']
y_sal = data['salinity']
y_sec = data['watertemp']


# Salinity Plot

ax_sal.plot(x[0:50],y_sal[0:50],'blue',label="A-Pool") #A-Pool
ax_sal.plot(x[0:50],y_sal[435:485],'purple',linestyle='--',label="B-Pool") #B-Pool
ax_sal.plot(x[0:50],y_sal[1220:1270],'red',linestyle=':',label="Bay") #Bay
ax_sal.legend()
ax_sal.set_ylabel("Salinity (ppt)")

# Water Temperature Plot

ax_sec.plot(x[0:50],y_sec[0:50],'blue',label="A-Pool") #A-Pool
ax_sec.plot(x[0:50],y_sec[435:485],'purple',linestyle='--',label="B-Pool") #B-Pool
ax_sec.plot(x[0:50],y_sec[1220:1270],'red',linestyle=':',label="Bay") #Bay
ax_sec.legend()
ax_sec.set_xlabel("Report Date")
ax_sec.set_ylabel("Water Temperature (C)")
ax_sec.tick_params(axis='x', rotation=45,)

plt.tight_layout
plt.show()
