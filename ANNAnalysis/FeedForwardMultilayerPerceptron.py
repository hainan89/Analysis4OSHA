'''
Created on 2015年8月13日

@author: hainan
'''
import neurolab as nl
import numpy as np
import csv
from numpy import dtype

def normalization_go(unit_up, unit_down, data_array):
    global_min = np.min(data_array)
    global_max = np.max(data_array)
    norm_r = unit_down + (data_array - global_min) / (global_max - global_min) * (unit_up - unit_down)
    return norm_r, global_min, global_max

def normalization_back(unit_up, unit_down, global_min, global_max, data_array):
    norm_back = global_min + (data_array - unit_down) / (unit_up - unit_down) * (global_max - global_min)
    return norm_back
    


def generate_decesion_data_set(csv_f_name, need_analysis_flag):
    dataset_list = csv.reader(open(csv_f_name))
    x = []
    y = []
    isheader = 1
    col_num = 0
    row_num = 0
    for one_item in dataset_list:
        if isheader == 1:
            isheader = 0
            continue
        y.append(int(one_item[1]))
        one_row = []
        for in_item_i in range(0, len(one_item)):
            if need_analysis_flag[in_item_i] == 0:
                continue
            one_row.append(int(one_item[in_item_i]))
            col_num += 1
        x.append(one_row)
        row_num += 1
    
    x_n = np.array(x, dtype = 'float64')
    y_n = np.array(y, dtype = 'float64')
    
    return x_n, y_n

# Create train samples
analysis_headers   = ["SummaryNr","Degree"      ,"Nature"      ,"Occupation" ,"FallDist",
                          "Cause"    ,"FatCause"    ,"TaskAssigned","HumanFactor","EnvironmentFactor",
                          "EventType","SourceInjury","PartBody"    ,"ProjType"   ,"ProjCost"         ,"EndUse"]
    
need_analysis_flag = [0          ,0             ,0             ,1            ,1         ,
                          0          ,1             ,0             ,0            ,0         ,
                          0          ,0             ,0             ,1            ,1         ,         0]
    
    
    
x , y = generate_decesion_data_set("../DecisionTree/coded_data_set_based_5_items.csv", need_analysis_flag)

# print(x)
# print(y)
    
# sample_p_test = np.arange(50, 100, 5) / 100
# x = np.linspace(-7, 7, 20)
# y = np.sin(x) * 0.5
# 
# size = len(x)
# 
# inp = x.reshape(size,1)
# tar = y.reshape(size,1)

# Create network with 2 layers and random initialized
# origianl_min_max = [[1, 4], [1,3], [1,6], [1,3], [1, 7]]
# original_min_max_array = np.array(origianl_min_max)
unit_up = 0.9
unit_down = 0.1


norm_x, g_x_min, g_x_max = normalization_go(unit_up, unit_down, x)
# orig_x = normalization_back(unit_up, unit_down, g_x_min, g_x_max, norm_x)



norm_y, g_y_min, g_y_max = normalization_go(unit_up, unit_down, y)
# orig_y = normalization_back(unit_up, unit_down, g_y_min, g_y_max, norm_y)
# print(y)
# print(norm_y)
# print(orig_y)


min_max = []
for col_index in np.arange(0, np.sum(need_analysis_flag)):
    col_min = np.min(norm_x[: , col_index])
    col_max = np.max(norm_x[: , col_index])
    min_max.append([col_min, col_max])

# min_max_array = np.array(min_max)
# orig_min_max_x = normalization_back(unit_up, unit_down, g_x_min, g_x_max, min_max_array)
# print(orig_min_max_x)

#       
net = nl.net.newff(min_max,[10, 10, 1])
 
# Train network
sample_p = 0.75
sample_flag = np.random.choice([True, False], p=[sample_p, 1-sample_p], 
                                size=len(norm_y))
train_x = norm_x[sample_flag]
train_y = norm_y[sample_flag]
train_y = train_y.reshape(len(train_y), 1)
  
error = net.train(train_x, train_y, epochs=6000, show=100, goal=0.02)
 
print("Train Error :",  error)
#  
# #  
# # Simulate network
sim_x = norm_x[~sample_flag]
sim_y = norm_y[~sample_flag]
sim_out = net.sim(sim_x)
 
orig_true_y = normalization_back(unit_up, unit_down, g_y_min, g_y_max, sim_y)
orig_sim_y = normalization_back(unit_up, unit_down, g_y_min, g_y_max, sim_out)
    
print(orig_true_y)
print(orig_sim_y)
#    
current_accu = (sim_out == sim_y).mean()
print(current_accu)
 
# # Plot result
# import pylab as pl
# pl.subplot(211)
# pl.plot(error)
# pl.xlabel('Epoch number')
# pl.ylabel('error (default SSE)')
#  
# x2 = np.linspace(-6.0,6.0,150)
# y2 = net.sim(x2.reshape(x2.size,1)).reshape(x2.size)
#  
# y3 = out.reshape(size)
#  
# pl.subplot(212)
# pl.plot(x2, y2, '-',x , y, '.', x, y3, 'p')
# pl.legend(['train target', 'net output'])
# pl.show()