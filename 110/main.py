import csv
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go
import random
import statistics
 
df = pd.read_csv("data.csv")
dv = df["average"].tolist()

avg_mean=statistics.mean(dv)
print("Mean",avg_mean)
avg_mode=statistics.mode(dv)
print("Mode",avg_mean)
avg_median=statistics.median(dv)
print("Median",avg_median)
avg_std=statistics.stdev(dv)
print("Standard Deviation",avg_std)

def random_set_of_mean(counter):
    datalist=[]
    for i in range(counter):
         random_index=random.randint(0,len(dv))
         value=dv[random_index]
         datalist.append(value)
    data_mean=statistics.mean(datalist)
    return data_mean

def show_fig(mean_list):
    df=mean_list
    fig = ff.create_distplot([dv],["Average"],show_hist=False)
    fig.show()
def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
setup()