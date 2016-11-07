import matplotlib.pyplot as plt
import numpy as np
import csv


def isfloat(value):
    '''make sure sample values are floats
    (problem with different number of values per sample)'''
    try:
      float(value)
      return True
    except ValueError:
      return False

def createCDFs (dataset):
    '''create a dictionary with sample name as key and data for each
    sample as one list per key'''
    dataset = dataset
    num_headers = len(list(dataset))
    dict_CDF = {}
    for a in dataset.keys():
        dict_CDF["{}".format(a)]= 1. * np.arange(len(dataset[a])) / (len(dataset[a]) - 1)
    return dict_CDF

def getdata ():
    '''retrieve data from a CSV file - file must have sample names in first row
    and data below'''

    with open('E:\GoogleDrive\PhD\Data\Detrital mica\All_onshore_DM_ages.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter = ',' )
        #create a dict that has sample names as key and associated ages as lists
        dataset = {}
        for row in reader:
            for column, value in row.iteritems():
                if isfloat(value):
                    dataset.setdefault(column, []).append(value)
                else:
                    break
        return dataset

x = getdata()
y = createCDFs(x)

#plot data
for i in x.keys():
    ax1 = plt.subplot(1,1,1)
    ax1.plot(x[i],y[i],label=str(i))


plt.legend(loc='upper left')
plt.show()
