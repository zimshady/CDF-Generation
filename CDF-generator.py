import matplotlib.pyplot as plt
import numpy as np
import csv
#Import data from csv file
def getdata ():
    with open('C:\GitHub Folders\Python-KDE-project\BF11Ages1s.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        ages = [map(float, row) for row in reader]

        return ages

def getmoredata ():
    with open('C:\GitHub Folders\Python-KDE-project\BF12Ages1s.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        ages = [map(float, row) for row in reader]

        return ages

# sort the data:
dataBF11_sorted = np.sort(getdata())
dataBF12_sorted = np.sort(getmoredata())

# calculate the proportional values of samples
p1 = 1. * np.arange(len(dataBF11_sorted)) / (len(dataBF11_sorted) - 1)
p2 = 1. * np.arange(len(dataBF12_sorted)) / (len(dataBF12_sorted) - 1)
difference = [a - b for a,b in zip(p1,p2)]
#diff = p1-p2
np.savetxt('C:\GitHub Folders\CDF-subtraction\pdf.txt',difference)

x_grid = np.linspace(0, 4000, 4000)

# plot the sorted data:
fig = plt.figure()
ax1 = fig.add_subplot(122)
ax1.plot(dataBF11_sorted, p1)
ax1.set_xlabel('$x$')
ax1.set_ylabel('$p$')

ax2 = fig.add_subplot(122)
ax2.plot(dataBF12_sorted, p2)
ax2.set_xlabel('$x$')
ax2.set_ylabel('$p$')

ax3 = fig.add_subplot(122)
ax3.plot(dataBF11_sorted, difference)
ax3.set_xlabel('$x$')
ax3.set_ylabel('$p$')
print np.trapz(p1)
print np.trapz(p2)
'''bf11, = plt.plot(dataBF11_sorted, p1, label="BF11",color='blue', alpha=0.5, lw=1)
bf12, = plt.plot(dataBF12_sorted, p2, label="BF12",color='red', alpha=0.5, lw=1)'''
#diff, = plt.plot(x_grid,difference, label="Difference", color='purple', alpha=0.5, lw=1)

plt.legend()
plt.title("BF11-BF12")
plt.show()
