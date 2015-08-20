'''
Created on 2015年8月12日

@author: hainan
'''


from sklearn.tree import DecisionTreeClassifier
# from sklearn import datasets
import numpy as np

import matplotlib.pyplot as plt

import csv
from sklearn import tree
# from io import BytesIO
import pydotplus

def generate_decesion_tree_dot(dt, f_path_name):
    tree.export_graphviz(dt, out_file = f_path_name)

def decision_tree_analysis(feature_data, target_class, sample_p, tree_max_depth):
    
    sample_flag = np.random.choice([True, False], p=[sample_p, 1-sample_p], 
                                size=len(target_class))
    
    dt = DecisionTreeClassifier(max_depth=tree_max_depth)
    dt.fit(feature_data[sample_flag], target_class[sample_flag])
    
    preds = dt.predict(feature_data[~sample_flag])
    current_accu = (preds == target_class[~sample_flag]).mean()
    
    return dt, current_accu, dt.feature_importances_

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
    
    x_n = np.array(x)
    y_n = np.array(y)
    
    return x_n, y_n
    
if __name__ == '__main__':
    
    
    
    analysis_headers   = ["SummaryNr","Degree"      ,"Nature"      ,"Occupation" ,"FallDist",
                          "Cause"    ,"FatCause"    ,"TaskAssigned","HumanFactor","EnvironmentFactor",
                          "EventType","SourceInjury","PartBody"    ,"ProjType"   ,"ProjCost"         ,"EndUse"]
    
    need_analysis_flag = [0          ,0             ,0             ,1            ,1         ,
                          1          ,1             ,1             ,1            ,1         ,
                          1          ,1             ,0             ,1            ,1         ,         1]
    
    
    
    x , y = generate_decesion_data_set("coded_data_set_based_5_items.csv", need_analysis_flag)
    
    sample_p_test = np.arange(50, 100, 5) / 100
    
    
    one_test_size = 0
    test_times = 2
    multi_test_result = []
    multi_test_import_feature_r = []
    for test_i in np.arange(1, test_times, 1):
        accuracy_test = []
        
        feature_importance_test = []
        
        for each_p in sample_p_test:
            
            current_dt, current_accu, current_feature_importances = decision_tree_analysis(x, y, each_p, 3)
            accuracy_test.append(current_accu)
            feature_importance_test.append(current_feature_importances)
            print("SampleP :", each_p, "  Accuracy :", current_accu, "current_feature_importances", current_feature_importances)
               
        
        one_test_size = np.size(np.array(accuracy_test))
        multi_test_result.append(np.array(accuracy_test))
#         multi_test_import_feature_r.append(np.array(feature_importance_test))
    
#     temp_sum_np_array = np.zeros(one_test_size)
#     
#     multi_test_array = np.array(multi_test_result)
#     
#     print(np.size(multi_test_array[:, 1]))
#     
#     for each_item in multi_test_result:
#         temp_sum_np_array = temp_sum_np_array + each_item
#         
#     mean_accuracy = temp_sum_np_array / (test_times - 1)
#         
#     
#     
# 
# #     
#     f, ax = plt.subplots(figsize=(7,5))
#     ax.plot(sample_p_test, mean_accuracy, color="k")
#     ax.set_title("Decision Tree Accuracy")
#     ax.set_ylabel("% Correct")
#     ax.set_xlabel("Sample Probability")
#     f.show()
    

#     y_comp = dt_ci.feature_importances_
#     x_comp = np.arange(len(y_comp))
#     f_ci, ax_ci = plt.subplots(figsize=(7,5))
#     ax_ci.bar(x_comp, y_comp)
#     f_ci.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
