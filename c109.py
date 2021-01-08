import csv 
import random as rd
import pandas as pd  
import statistics as st
import plotly.express as pe
import plotly.figure_factory as pf
import plotly.graph_objects as go
dicerst = []
for i in range(0,1000):
    dice1 = rd.randint(1,6)
    dice2 = rd.randint(1,6)
    dicerst.append(dice1+dice2)
mean = sum(dicerst)/len(dicerst)  
median = st.median(dicerst)
mode = st.mode(dicerst)
standarddev = st.stdev(dicerst)
print(mean)
print(median)
print(mode) 
print(standarddev)
firstsdstart,firstsdend = mean-standarddev,mean+standarddev
secdevstart,secstend = mean-(2*standarddev),mean+(2*standarddev)
thirddevstart,thirddevend = mean-(3*standarddev),mean+(3*standarddev)

fig = pf.create_distplot([dicerst],["result"],show_hist = False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name = "mean"))
fig.add_trace(go.Scatter(x=[firstsdstart,firstsdstart],y=[0,0.17],mode="lines",name="standard deviation1"))
fig.add_trace(go.Scatter(x=[firstsdend,firstsdend],y=[0,0.17],mode="lines",name="standard deviation1"))
fig.add_trace(go.Scatter(x=[secdevstart,secdevstart],y=[0,0.17],mode="lines",name="standard deviation2"))
fig.add_trace(go.Scatter(x=[secstend,secstend],y=[0,0.17],mode="lines",name="standard deviation2"))
#printing the result
listofdatawithinfirststandarddeviation = [result for result in dicerst if result>firstsdstart and result<firstsdend]
listofdatawithinsecondstandarddeviation = [result for result in dicerst if result>secdevstart and result<secstend]
listofdatawithinthirdstandarddeviation = [result for result in dicerst if result>thirddevstart and result<thirddevend]
print("{}% of data lies within first standard deviation".format(len(listofdatawithinfirststandarddeviation)*100.0/len(dicerst)))
print("{}% of data lies within second standard deviation".format(len(listofdatawithinsecondstandarddeviation)*100.0/len(dicerst)))
print("{}% of data lies within third standard deviation".format(len(listofdatawithinthirdstandarddeviation)*100.0/len(dicerst)))
fig.show()