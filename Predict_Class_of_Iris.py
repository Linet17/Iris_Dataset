import pandas as pd
import numpy as nm

irisfile = r"C:\Users\lgacheri\Datasets\Iris_Dataset\iris.data"

#irisContent = [i.strip().split() for i in open("C:\Users\lgacheri\Datasets\Iris_Dataset\iris.data").readlines()]
#print(irisContent)

irisdata = pd.read_csv(irisfile, delimiter=",")
print(irisdata)

irisdata.columns = ['sepal_length(cm)','sepal_width(cm)','petal_length(cm)','petal_width(cm)','flower_class']
print(irisdata)
