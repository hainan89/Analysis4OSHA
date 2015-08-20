'''
Created on 2015年8月14日

@author: hainan
'''
import numpy as np
import neurolab as nl
from decimal import Decimal as D

import csv


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
        y_num = int(one_item[1])
        y_code = []
        if y_num == 1:
            y_code = [0 ,1]  #0.5
        if y_num == 2:
            y_code = [1 ,0]     #0.42
        if y_num == 3:
            y_code = [1 ,1]     #0.08
        y.append(y_code)
        one_row = []
        for in_item_i in range(0, len(one_item)):
            if need_analysis_flag[in_item_i] == 0:
                continue
            one_row.append(int(one_item[in_item_i]))
            col_num += 1
        x.append(one_row)
        row_num += 1
    
    x_n = np.array(x)
    y_n = np.array(y)
    
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
# Create train samples
# input = np.array([[-3, 0], [-2, 1], [-2, -1], [0, 2], [0, 1], [0, -1], [0, -2], 
#                                                         [2, 1], [2, -1], [3, 0]])
# target = np.array([[1, 0], [1, 0], [1, 0], [0, 1], [0, 1], [0, 1], [0, 1], 
#                                                         [1, 0], [1, 0], [1, 0]])

# Train network
sample_p = 0.75
sample_flag = np.random.choice([True, False], p=[sample_p, 1-sample_p], 
                                size=len(y))
input = x[sample_flag]
target = y[sample_flag]


# Create network with 2 layers:4 neurons in input layer(Competitive)
# and 2 neurons in output layer(liner)
# print(nl.tool.minmax(input))

class_p = [D('0.5'), D('0.5')]
net = nl.net.newlvq(nl.tool.minmax(input), 5, class_p)

# print(nl.tool.minmax(input))
# Train network
error = net.train(input, target, epochs=1000, goal=-1)

print(error)

sim_input = x[~sample_flag]
real_out = y[~sample_flag]
sim_out = net.sim(sim_input) 

current_accu = (sim_out == real_out).mean()

print(real_out)
print(sim_out)
print(current_accu)

# # Plot result
# import pylab as pl
# xx, yy = np.meshgrid(np.arange(-3, 3.4, 0.2), np.arange(-3, 3.4, 0.2))
# xx.shape = xx.size, 1
# yy.shape = yy.size, 1
# i = np.concatenate((xx, yy), axis=1)
# o = net.sim(i)
# grid1 = i[o[:, 0]>0]
# grid2 = i[o[:, 1]>0]
#  
# class1 = input[target[:, 0]>0]
# class2 = input[target[:, 1]>0]
#  
# pl.plot(class1[:,0], class1[:,1], 'bo', class2[:,0], class2[:,1], 'go')
# pl.plot(grid1[:,0], grid1[:,1], 'b.', grid2[:,0], grid2[:,1], 'gx')
# pl.axis([-3.2, 3.2, -3, 3])
# pl.xlabel('Input[:, 0]')
# pl.ylabel('Input[:, 1]')
# pl.legend(['class 1', 'class 2', 'detected class 1', 'detected class 2'])
# pl.show()