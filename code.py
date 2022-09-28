# importing libraries
import numpy as np # linear algebra
import pandas as pd # primary data structure library
traffic_data = pd.read_csv(r'/kaggle/input/traffice-violations2022/Traffic_Violations1.csv')
vok = pd.DataFrame (traffic_data, columns = ['Date Of Stop'])
print ('number of duplicate rows is:',vok)

# Finding Color of the car
df = pd.DataFrame (traffic_data, columns = ['Color'])
total_color = df.pivot_table(columns=['Color'], aggfunc='size')
print (total_color)
max_color_voil = max(total_color)
print (max_color_voil)


# Model of the car
df = pd.DataFrame (traffic_data, columns = ['Make'])
data_of_make = df.pivot_table(columns=['Make'], aggfunc='size')
print = (data_of_make)

max_model = max(dups_data_of_sto1)
print (max_model)
