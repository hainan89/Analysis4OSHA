import mysql.connector
import csv

from ToolKits.NicePrint import NicePrint

from StatisticAnalysis.OriginalItemClassification import ItemClassification
from DecisionTree.ClassesCode import ClasesCode

# statistic for the classification of data items
def process_items(item_name):
    user = 'test'
    pwd = '123456'
    host = '127.0.0.1'
    db = 'reported_fall_event'
    cnx = mysql.connector.connect(user=user, password=pwd, host=host, database=db)
    cursor = cnx.cursor()
    
    query_sql = ("select %s from case_employees order by ID" % item_name)
    query_sql_value = (item_name)
    
    cursor.execute(query_sql, query_sql_value)
    item_list = cursor.fetchall()
    item_dictionary = {}

    for item in item_list:
        current_item = item[0]
        if type(current_item) == type(None) or len(current_item.strip()) == 0:
            current_item = "Non record"
            
        if current_item not in item_dictionary:
            item_dictionary[current_item] = 1
        else:
            item_dictionary[current_item] = item_dictionary[current_item] + 1
    cursor.close()
    cnx.close()
    return item_dictionary

def obtain_class_code(classification_dict_v):
    class_code = {}
    
    total_records = 0
    for k, v in classification_dict_v.items():
        total_records = total_records + v
    valid_records = total_records - classification_dict_v["Non record"]
    
    sorted_dict_by_v = sorted(classification_dict_v.items(), key=lambda classification_dict_v:classification_dict_v[1], reverse = True)
    iterate_code_v = 0
    class_p = 0
    
    for (k, v) in sorted_dict_by_v:
        
        if k == "Non record":
            code_v = 0
            class_p = 0
        else:
            class_p = v / valid_records
            if class_p < 0.05:
                code_v = 0
            else:
                iterate_code_v += 1
                code_v = iterate_code_v
        print("|", k, "|" ,code_v, "|" , classification_dict_v[k], "|", valid_records,"|", class_p, "|",total_records)
        class_code[k] = code_v
    
    # print the probability of the classification
    return class_code

def obtian_class_code_by_item_name(item_name):
    item_classes = process_items(item_name)
    classes_code = obtain_class_code(item_classes)
    return classes_code

def purify_dataset():
    user = "test"
    pwd = "123456"
    host = "127.0.0.1"
    db = "reported_fall_event"
    cnx = mysql.connector.connect(user=user, password=pwd, host=host, database=db)
    cursor = cnx.cursor()

    query_sql = ("select "
                " SummaryNr, Degree, Nature, Occupation, FallDist, Cause, FatCause, "
                " TaskAssigned, HumanFactor, EnvironmentFactor, EventType, SourceInjury, PartBody, ProjType, ProjCost, EndUse "
                "from case_employees order by ID")
    cursor.execute(query_sql)

    data_list = cursor.fetchall()

    storage_data_header = ["SummaryNr", "Degree", "Nature", "Occupation", "FallDist", "Cause", "FatCause",
                           "TaskAssigned", "HumanFactor", "EnvironmentFactor", "EventType", "SourceInjury", "PartBody", "ProjType", " ProjCost", "EndUse"]
    
#     clases_code = ClasesCode()
    
    nature_classes_code = obtian_class_code_by_item_name("Nature")
    degree_classes_code = obtian_class_code_by_item_name("Degree")
    occupation_classes_code = obtian_class_code_by_item_name("Occupation")
    cause_classes_code = obtian_class_code_by_item_name("Cause")
    fat_cause_classes_code = obtian_class_code_by_item_name("FatCause")
    task_assigned_classes_code = obtian_class_code_by_item_name("TaskAssigned")
    human_factor_classes_code = obtian_class_code_by_item_name("HumanFactor")
    env_factor_classes_code = obtian_class_code_by_item_name("EnvironmentFactor")
    event_type_classes_code = obtian_class_code_by_item_name("EventType")
    source_injury_classes_code = obtian_class_code_by_item_name("SourceInjury")
    part_body_classes_code = obtian_class_code_by_item_name("PartBody")
    proj_type_classes_code = obtian_class_code_by_item_name("ProjType")
    proj_cost_classes_code = obtian_class_code_by_item_name("ProjCost")
    end_use_classes_code = obtian_class_code_by_item_name("EndUse")
    
    with open('coded_data_set.csv', 'w', newline='') as comp_r_csv:
        spamwriter = csv.writer(comp_r_csv, dialect='excel')
        spamwriter.writerow(storage_data_header)
        for row_v in data_list:
            row = []
            for in_row_index in range(0, len(row_v)):
                if type(row_v[in_row_index]) == type(None):
                    row.append("Non record")
                elif isinstance(row_v[in_row_index], str) and len(row_v[in_row_index].strip()) == 0:
                    row.append("Non record")
                else:
                    row.append(row_v[in_row_index])
            print(row)
    
            SummaryNr = row[0]
            Degree = degree_classes_code[row[1]]
            if Degree == 0:
                continue
            Nature = nature_classes_code[row[2]]
            if Nature == 0:
                continue
            Occupation = occupation_classes_code[row[3]]
            if Occupation == 0:
                continue
            if row[4] < 12:
                FallDist = 1
            elif row[4] >= 12 and row[4] < 24:
                FallDist = 2
            else:
                FallDist = 3

            Cause = cause_classes_code[row[5]] #CauseTypeCode[row[5]]
            if Cause == 0:
                continue
            FatCause = fat_cause_classes_code[row[6]] #FatCauseTypeCode[row[6]]
            if FatCause == 0:
                continue
            TaskAssigned = task_assigned_classes_code[row[7]]
            if TaskAssigned == 0:
                continue
            HumanFactor = human_factor_classes_code[row[8]]
            if HumanFactor == 0:
                continue
            EnvironmentFactor = env_factor_classes_code[row[9]]
            if EnvironmentFactor == 0:
                continue
            EventType = event_type_classes_code[row[10]]
            if EventType == 0:
                continue
            SourceInjury = source_injury_classes_code[row[11]]
            if SourceInjury == 0:
                continue
            PartBody = part_body_classes_code[row[12]]
            if PartBody == 0:
                continue
            ProjType = proj_type_classes_code[row[13]]
            if ProjType == 0:
                continue
            ProjCost = proj_cost_classes_code[row[14]]
            if ProjCost == 0:
                continue
            EndUse = end_use_classes_code[row[15]]
            if EndUse == 0:
                continue
            
            
            record_row = [SummaryNr, Degree, Nature, Occupation, FallDist, Cause, FatCause,
                          TaskAssigned, HumanFactor, EnvironmentFactor, EventType, SourceInjury, PartBody, ProjType,  ProjCost, EndUse]
            spamwriter.writerow(record_row)
            print(record_row)
    print("Data Purifying has Done!")
    return 
            
        

if __name__ == '__main__':
    # obtain the original classification statistics data 
    
    purify_dataset()
    
#     #### print the statistics data
#     print("Nature")
#     nature_classes_code = obtian_class_code_by_item_name("Nature")
#     print("Degree")
#     degree_classes_code = obtian_class_code_by_item_name("Degree")
#     print("Occupation")
#     occupation_classes_code = obtian_class_code_by_item_name("Occupation")
#     print("Cause")
#     cause_classes_code = obtian_class_code_by_item_name("Cause")
#     print("FatCause")
#     fat_cause_classes_code = obtian_class_code_by_item_name("FatCause")
#     print("TaskAssigned")
#     task_assigned_classes_code = obtian_class_code_by_item_name("TaskAssigned")
#     print("HumanFactor")
#     human_factor_classes_code = obtian_class_code_by_item_name("HumanFactor")
#     print("EnvironmentFactor")
#     env_factor_classes_code = obtian_class_code_by_item_name("EnvironmentFactor")
#     print("EventType")
#     event_type_classes_code = obtian_class_code_by_item_name("EventType")
#     print("SourceInjury")
#     source_injury_classes_code = obtian_class_code_by_item_name("SourceInjury")
#     print("PartBody")
#     part_body_classes_code = obtian_class_code_by_item_name("PartBody")
#     print("ProjType")
#     proj_type_classes_code = obtian_class_code_by_item_name("ProjType")
#     print("ProjCost")
#     proj_cost_classes_code = obtian_class_code_by_item_name("ProjCost")
#     print("EndUse")
#     end_use_classes_code = obtian_class_code_by_item_name("EndUse")
