import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_req = pd.read_table("C:\Google Drive\PhD\Data\Detrital mica\Onshore_DM_ages_inc_Ennis2015_exc_Kiltorcan.csv", sep=",")
#sort values per column
arr = data_req.values
arr.sort(axis=0)
data_req = pd.DataFrame(arr, index=data_req.index, columns=data_req.columns)

#plot with matplotlib
#note that you have to drop the Na's on columns to have appropriate
#dimensions per variable.

for col in data_req.columns:
    y = np.linspace(0.,1., len(data_req[col].dropna()))
    plt.plot(data_req[col].dropna(), y, drawstyle='steps',label=str(col))
plt.legend(loc='lower right', fontsize = 12)
plt.show()
