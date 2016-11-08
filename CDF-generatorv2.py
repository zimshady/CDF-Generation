import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_req = pd.read_table("E:\GoogleDrive\PhD\Data\Detrital mica\All_onshore_DM_ages.csv", sep=",")
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
plt.legend(loc='lower right')
plt.show()
