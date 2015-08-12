'''
Created on 2015年8月9日

@author: hainan
'''

from StatisticAnalysis.OriginalItemClassification import ItemClassification 
from DataObtain.BrowserShadow import BrowserShadow
from urllib.parse import urlencode

import csv
import json
from _sqlite3 import Row
from audioop import reverse

def get_similar_matrix(data_dic, storage_file_name): #'ocup_comp_result' without postfix
    
#     storage_txt_f_name = storage_file_name + ".txt"
    storage_csv_f_name = storage_file_name + ".csv"
    
#     output_f = open(storage_txt_f_name, 'w+')   
    comp_element = list(data_dic.keys())

    with open(storage_csv_f_name, 'w', newline='') as comp_r_csv:
        spamwriter = csv.writer(comp_r_csv,dialect='excel')
        spamwriter.writerow(comp_element)

        url = "https://www.metamind.io/language/relatedness/test?{test_p_str}"
        brw = BrowserShadow()
        similar_matrix_dic = {}
        for each_item_r  in comp_element:
            r_list = []
            for each_item_c in comp_element:
                test_data = {"text_2":each_item_r, "text_1":each_item_c}
                test_data_str = urlencode(test_data)
    
                comp_url = url.format(test_p_str = test_data_str)
    
                res = brw.open_url(comp_url)

                page_content = res.read()
                
                compar_result = page_content.decode()
                result = eval(compar_result)
                r_list.append(result["score"])
                r_str = "row, col, comp_r, %s, %s, %s" % (each_item_r, each_item_c, result["score"])
#                 output_f.write(r_str + "\n")
                print(r_str)
            similar_matrix_dic[each_item_r] = r_list
            spamwriter.writerow(r_list)
#     output_f.close()
#     return similar_matrix_dic
    print("Comparing has Done!", storage_file_name)


# classify the items according to the similarity
def classify_similarity(simi_matrix_f_name):
    matrix_header = []
    data_row = []
    with open(simi_matrix_f_name, 'r') as simi_f:
        reader = csv.reader(simi_f)
        index_i = 1
        for row in reader:
            if index_i == 1:
                matrix_header = row
                index_i += 1
            else:
                index_i += 1
                data_row.append(row)
    
#     header_counter_dict = {}
#     for each_header in matrix_header:
#         current_index = matrix_header.index(each_header)
#         current_count = 0
#         for each_v in data_row[current_index]:
#             similirity_v = float(each_v)
#             if similirity_v > 3:
#                 current_count += 1
#         header_counter_dict[each_header] = current_count
#     
#     header_counter_dict = sorted(header_counter_dict.items(), key=lambda header_counter_dict:header_counter_dict[1], reverse=True)
#     
#     matrix_header = []
#     for each_item in header_counter_dict:
#         matrix_header.append(each_item[0])
#         
#     print(header_counter_dict)
#     print(matrix_header)
#     return
    
    classifity_result = [[matrix_header[0]]]
    for item in matrix_header:
        
        print("Current Item", item)
        
        if item == matrix_header[0]:
            continue
        
        is_in_classifity_result = 0
        for class_item in classifity_result:
            
            is_in_this_class = 0
            for in_class_item in class_item:
                non_class_i = matrix_header.index(item)
                current_in_class_item_i = matrix_header.index(in_class_item)
                similirity_v = float(data_row[current_in_class_item_i][non_class_i])
#                 print(similirity_v)
                if similirity_v > 3:
                    is_in_this_class = 1
                    continue
                else:
                    is_in_this_class = 0
                    break
                
            if is_in_this_class == 1:
                is_in_classifity_result = 1
                classifity_result[classifity_result.index(class_item)].append(item)
                break
                
        if is_in_classifity_result == 0:
            new_class = [item]
            classifity_result.append(new_class)
        
#         print(classifity_result)
    print("It's done!")
    return classifity_result


if __name__ == '__main__':
    
    
#     classification_object = ItemClassification()
#     cause_classification_dict = classification_object.cause_classification
#     fat_cause_classification_dict = classification_object.fat_cause_classification
#     print(cause_classification_dict)
#     print(fat_cause_classification_dict)
#     get_similar_matrix(cause_classification_dict, "cause_comp_result")
#     get_similar_matrix(fat_cause_classification_dict, "fat_cause_comp_result")
    
#     nature_classification_dict = classification_object.nature_classification
#     get_similar_matrix(nature_classification_dict, "nature_comp_result")
    
    
    similarity_class = classify_similarity("ocup_comp_records.csv")
    
#     print(bin(4))
#    
    class_code_dict = {}
    classes_amount = len(similarity_class)
    class_code = 1
    for one_class in similarity_class:
        
        for item in one_class:
            class_code_dict[item] = class_code
        class_code += 1
    
    print(json.dumps(class_code_dict, ensure_ascii=False, indent=1))
#     total_item = 0
#     for one_class in similarity_class:
#         total_item = total_item + len(one_class)
#            
#         print("[")
#         for item in one_class:
#             print("'"+item+"'")
#         print("]")
#         print(",")
#     print(total_item)
#     print(len(similarity_class))

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    