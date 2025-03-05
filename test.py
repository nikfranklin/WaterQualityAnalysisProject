import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

data =  np.genfromtxt("BKB_WaterQualityData_2020084.csv",
                            skip_header=1, skip_footer=3, delimiter=",", usecols=(2,3,6),
                            dtype=[('readdate','U10'),('salinity',float),('secchidepth',float)],
                            names=['readdate','salinity','secchidepth'], 
                            missing_values={'salinity':'','secchidepth':''}, 
                            filling_values={'salinity':0.0,'secchidepth':0.0},
                            )

fig, (ax_sal,ax_sec) = plt.subplots(2,1, figsize=(10,7), sharex='all', layout='constrained')
plt.xticks(np.arange(0, 109, step=5))
plt.yticks(np.arange(0, 109, step=2,))
x = data['readdate']
y_sal = data['salinity']
y_sec = data['secchidepth']


# Salinity Plot

ax_sal.plot(x[0:109],y_sal[0:109],'red',label="A-Pool") #A-Pool
ax_sal.plot(x[0:109],y_sal[435:544],'purple',label="B-Pool") #B-Pool
ax_sal.plot(x[0:109],y_sal[1220:1329],'blue',label="Bay") #Bay
ax_sal.legend()
ax_sal.set_ylabel("Salinity (ppt)")

# Secchi Depth Plot

ax_sec.plot(x[0:109],y_sec[0:109],'red',label="A-Pool") #A-Pool
ax_sec.plot(x[0:109],y_sec[435:544],'purple',label="B-Pool") #B-Pool
ax_sec.plot(x[0:109],y_sec[1220:1329],'blue',label="Bay") #Bay
ax_sec.legend()
ax_sec.set_xlabel("Report Date")
ax_sec.tick_params(axis='x', rotation=45,)
ax_sec.set_ylabel("Secchi Depth (m)")

#for i in data:
#print(i)
plt.tight_layout
fig.savefig("test.png")
