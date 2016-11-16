import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import Tkinter as tk
import tkFileDialog

#set the figure text to be editable in Illustrator
mpl.rcParams['pdf.fonttype'] = 42
#GUI file request to user
root = tk.Tk()
root.withdraw()
file_path = tkFileDialog.askopenfilename()

#read data into panda table
data_req = pd.read_table(file_path, sep=",")

#sort values per column
arr = data_req.values
arr.sort(axis=0)
data_req = pd.DataFrame(arr, index=data_req.index, columns=data_req.columns)

#plot with matplotlib
#note that you have to drop the Na's on columns to have appropriate
#dimensions per variable.
for col in data_req.columns:
    y = np.linspace(0.,1., len(data_req[col].dropna()))
    plt.plot(data_req[col].dropna(), y, drawstyle='steps',label=str(col) +" (n = " + str(len(data_req[col].dropna())) + ")")
plt.xlim([200,500])
plt.legend(loc='best', fontsize = 12)

#GUI request for file name and location for saving output
file_name = tkFileDialog.asksaveasfilename()
plt.savefig(file_name, format='pdf', dpi=1000)
