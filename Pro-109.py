import csv
import pandas as pd
import plotly.express as px
import plotly.graph_objects as pg
import plotly.figure_factory as pf
import statistics as st

f = pd.read_csv("StudentsPerformance.csv")
column_name = input("Enter the column name : ")
df = f[column_name].tolist()

mean = st.mean(df)
print("mean : ", mean)
# mode = st.mode(df)
# print(mode)
median = st.median(df)
print("median : " ,median )

deviation = st.stdev(df)
print("standard deviation : ",deviation)
# Range 1
start_dev_1 = mean - deviation
end_dev_1 = mean + deviation
dev_range_1 = [result for result in df if result > start_dev_1 and result < end_dev_1] 
dev_p_1 = format(len(dev_range_1) * 100.0 / len(df))
print("1st deviation percentage : ",dev_p_1)

# Range 2
start_dev_2 = mean - 2*deviation
end_dev_2 = mean + 2*deviation
dev_range_2 = [result for result in df if result > start_dev_2 and result < end_dev_2] 
dev_p_2 = format(len(dev_range_2) * 100.0 / len(df))
print("2nd deviation percentage : ",dev_p_2)

# Range 3
start_dev_3 = mean - 3*deviation
end_dev_3 = mean + 3*deviation
dev_range_3 = [result for result in df if result > start_dev_3 and result < end_dev_3] 
dev_p_3 = format(len(dev_range_3) * 100.0 / len(df))
print("3rd deviation percentage : ",dev_p_3)

fig = pf.create_distplot([df],["label"],show_hist=False)
fig.add_trace(pg.Scatter(x = [mean,mean],y=[0,0.25],mode = "lines",name = "mean"))
fig.add_trace(pg.Scatter(x = [start_dev_1,start_dev_1],y=[0,0.25],mode = "lines",name = "stdev1_start"))
fig.add_trace(pg.Scatter(x = [start_dev_2,start_dev_2],y=[0,0.25],mode = "lines",name = "stdev2_start"))
fig.add_trace(pg.Scatter(x = [start_dev_3,start_dev_3],y=[0,0.25],mode = "lines",name = "stdev3_start"))
fig.add_trace(pg.Scatter(x = [end_dev_1,end_dev_1],y=[0,0.25],mode = "lines",name = "stdev1_end"))
fig.add_trace(pg.Scatter(x = [end_dev_2,end_dev_2],y=[0,0.25],mode = "lines",name = "stdev2_end"))
fig.add_trace(pg.Scatter(x = [end_dev_3,end_dev_3],y=[0,0.25],mode = "lines",name = "stdev3_end"))
fig.show()
