'''
Created on 2015年7月28日

@author: hainan
'''

import mysql.connector
from urllib.parse import urlencode
from _ast import Store
from pip.commands import completion
from bs4 import BeautifulSoup
from pip.download import InsecureHTTPAdapter
from encodings.punycode import insertion_unsort


def process_degree():
    user = 'test'
    pwd = '123456'
    host = '127.0.0.1'
    db = 'reported_fall_event'
    cnx = mysql.connector.connect(user=user, password=pwd, host=host, database=db)
    cursor = cnx.cursor()
    
    query_sql = "select Degree from case_employees order by ID"
    cursor.execute(query_sql)
    degree_list = cursor.fetchall()
    degree_dictionary = {}
    degree_dictionary_p = {}
    for item in degree_list:
        current_degree = item[0]
        if len(current_degree) == 0:
            current_degree = "Non record"
        if current_degree not in degree_dictionary:
            degree_dictionary[current_degree] = 1
        else:
            degree_dictionary[current_degree] = degree_dictionary[current_degree] + 1
    
    degree_level = {"Non record": 1, "Non Hospitalized injury":2 , "Hospitalized injury":3, "Fatality":4}
    
    total_record = 0
    for item in degree_dictionary:
        total_record = total_record + degree_dictionary[item]
        
    for item in degree_dictionary:
        degree_dictionary_p[item] = degree_dictionary[item] / total_record
        
    cursor.close()
    cnx.close()
    print(degree_dictionary)
    print(degree_dictionary_p)
    return degree_dictionary, degree_dictionary_p

# {'Non Hospitalized injury': 954, 'Non record': 2003, 'Hospitalized injury': 6617, 'Fatality': 5664}
# {'Non Hospitalized injury': 0.06260664129150807, 'Hospitalized injury': 0.43424333902086887, 'Non record': 0.13144769654810343, 'Fatality': 0.3717023231395196}


    
def process_nature():
    user = 'test'
    pwd = '123456'
    host = '127.0.0.1'
    db = 'reported_fall_event'
    cnx = mysql.connector.connect(user=user, password=pwd, host=host, database=db)
    cursor = cnx.cursor()
    
    query_sql = "select Nature from case_employees order by ID"
    cursor.execute(query_sql)
    nature_list = cursor.fetchall()
    nature_dictionary = {}
#     nature_dictionary_p = {}
    for item in nature_list:
        current_nature = item[0]
        if len(current_nature) == 0:
            current_nature = "Non record"
            
#         nature_list = current_degree.split('/')
        if current_nature not in nature_dictionary:
            nature_dictionary[current_nature] = 1
        else:
            nature_dictionary[current_nature] = nature_dictionary[current_nature] + 1
#         for nature_item in nature_list:
#             if nature_item not in nature_dictionary:
#                 nature_dictionary[nature_item] = 1
#             else:
#                 nature_dictionary[nature_item] = nature_dictionary[nature_item] + 1
    
#     total_record = 0
#     for item in nature_dictionary:
#         total_record = total_record + nature_dictionary[item]
#         
#     for item in nature_dictionary:
#         nature_dictionary_p[item] = nature_dictionary[item] / total_record
        
    cursor.close()
    cnx.close()
    print(nature_dictionary)
#     print(nature_dictionary_p)
    return nature_dictionary

def process_level():
    user = 'test'
    pwd = '123456'
    host = '127.0.0.1'
    db = 'reported_fall_event'
    cnx = mysql.connector.connect(user=user, password=pwd, host=host, database=db)
    cursor = cnx.cursor()
    
    query_sql = "select ID, Degree from case_employees order by ID"
    cursor.execute(query_sql)
    record_list = cursor.fetchall()
    
    [degree_dictionary, degree_dictionary_p] = process_degree()
    [nature_dictionary, nature_dictionary_p] = process_nature()
    
    degree_l_dic = {"Non record":1, "Non Hospitalized injury":2, "Hospitalized injury":3, "Fatality":4}
    
    for item in record_list:
        item_id = item[0]
        print(item_id)
        degree_str = item[1]
        #nature_str = item[2]
        
        degree_L_value = 0
        degree_P_value = 0
        
#         degree_r_value = 0
#         nature_r_value = 0
        
        if len(degree_str) == 0:
            degree_str = "Non record"
            
        degree_L_value = degree_l_dic[degree_str]
        degree_P_value = degree_dictionary_p[degree_str]
#         degree_r_value = degree_dictionary_p[degree_str]
            
#         if len(nature_str) == 0:
#             nature_str = "Non record"
#         nature_list = nature_str.split('/')
#         for nature_item in nature_list:
#             nature_r_value = nature_r_value + nature_dictionary_p[nature_item]
        
            
        update_sql = ("update case_employees set "
                      "Degree_L = %s, Degree_P = %s "
                      "where ID = %s")
        update_sql_value = (degree_L_value, degree_P_value, item_id)
        
        cursor.execute(update_sql, update_sql_value)
        cnx.commit() 
        #print(degree_r_value)
        #print(nature_r_value)
    
    cursor.close()
    cnx.close()
    print("Update Done!")
        
def process_construction():
    user = 'test'
    pwd = '123456'
    host = '127.0.0.1'
    db = 'reported_fall_event'
    cnx = mysql.connector.connect(user=user, password=pwd, host=host, database=db)
    cursor = cnx.cursor()
    
    query_sql = "select ID, Construction from case_employees order by ID"
    cursor.execute(query_sql)
    construction_list = cursor.fetchall()
    
    for c_item in construction_list:
        item_id = c_item[0]
        item_str = c_item[1]
   
        in_item_list = item_str.split("', '") 
        update_value = {}

        for c_one in in_item_list:
            
            c_one = c_one.replace("['" , '')
            c_one = c_one.replace("']" , '')
            
            c_one_list = c_one.split(':')
            if len(c_one_list) > 1:
                update_value[c_one_list[0]] = c_one_list[1]
            
        if "FallDist" not in update_value:
            update_value['FallDist'] = 0
        else:
            update_value['FallDist'] = update_value['FallDist'].replace(" ", "")
            if len(update_value['FallDist']) == 0:
                update_value['FallDist'] = 0
        
        if "FallHt" not in update_value:
            update_value['FallHt'] = 0
        else:
            update_value['FallHt'] = update_value['FallHt'].replace(" ", "")
            if len(update_value['FallHt']) == 0:
                update_value['FallHt'] = 0
        
        if "Cause" not in update_value:
            update_value['Cause'] = ""
        
        if "FatCause" not in update_value:
            update_value['FatCause'] = ""
        
        #print(update_value['FallDist'] + "--")
        update_value['FallDist'] = int(update_value['FallDist'])
        #print(update_value['FallHt'] + "--")
        update_value['FallHt'] = int(update_value['FallHt'])
    
        update_sql = ("update case_employees set "
                      "FallDist = %s, FallHt = %s, Cause = %s, FatCause = %s "
                      "where ID = %s")
        
        update_sql_value = (update_value['FallDist'], update_value['FallHt'], update_value['Cause'], update_value['FatCause'], item_id)
        cursor.execute(update_sql, update_sql_value)
        cnx.commit()
        print("Update Done!")
        
        
    cursor.close()
    cnx.close()


def occupation_statistic():
    user = 'test'
    pwd = '123456'
    host = '127.0.0.1'
    db = 'reported_fall_event'
    cnx = mysql.connector.connect(user=user, password=pwd, host=host, database=db)
    cursor = cnx.cursor()
    
    query_sql = "select Occupation from case_employees order by ID"
    cursor.execute(query_sql)
    occupation_list = cursor.fetchall()
    occupation_dictionary = {}
    occupation_dictionary_p = {}
    for item in occupation_list:
        current_item = item[0]
        if len(current_item) == 0:
            current_item = "Non record"
        if current_item not in occupation_dictionary:
            occupation_dictionary[current_item] = 1
        else:
            occupation_dictionary[current_item] = occupation_dictionary[current_item] + 1
        
    
    return occupation_dictionary
    print(occupation_dictionary)


from DataObtain.BrowserShadow import BrowserShadow
def compare_2_sentences(text_1, text_2):
    
    url = "https://www.metamind.io/language/relatedness/test?{text}"
    data_dic = {"text_1":text_1, "text_2":text_2}
    text_str = urlencode(data_dic)
    url = url.format(text = text_str)
    brw = BrowserShadow()
    res = brw.open_url(url)
    page_content = res.read()
    compar_result = page_content.decode()
    result = eval(compar_result)
    return result["score"]


import csv
def get_similar_matrix(data_dic):
    
    output_f = open('ocup_comp_result.txt', 'w+')
    
    comp_element = list(data_dic.keys())

    with open('ocup_comp_records.csv', 'w', newline='') as comp_r_csv:
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
                output_f.write(r_str + "\n")
                print(r_str)
            similar_matrix_dic[each_item_r] = r_list
            spamwriter.writerow(r_list)
    output_f.close()
    return similar_matrix_dic

  
  
  
def cause_fatcause_statistic():
    user = 'test'
    pwd = '123456'
    host = '127.0.0.1'
    db = 'reported_fall_event'
    cnx = mysql.connector.connect(user=user, password=pwd, host=host, database=db)
    cursor = cnx.cursor()
    
    query_sql = "select Cause, FatCause from case_employees order by ID"
    cursor.execute(query_sql)
    cause_list = cursor.fetchall()
    cause_dictionary = {}
    fat_cause_dictionary = {}
    for item in cause_list:
        current_item = item[0]
        if len(current_item) == 0:
            current_item = "Non record"
        if current_item not in cause_dictionary:
            cause_dictionary[current_item] = 1
        else:
            cause_dictionary[current_item] = cause_dictionary[current_item] + 1
            
        current_fat_item = item[1]
        if len(current_fat_item) == 0:
            current_fat_item = "Non record"
        if current_fat_item not in fat_cause_dictionary:
            fat_cause_dictionary[current_fat_item] = 1
        else:
            fat_cause_dictionary[current_fat_item] = fat_cause_dictionary[current_fat_item] + 1
        
    
    return cause_dictionary, fat_cause_dictionary


def update_employee_from_cases_info():
    user = 'test'
    pwd = '123456'
    host = '127.0.0.1'
    db = 'reported_fall_event'
    cnx = mysql.connector.connect(user=user, password=pwd, host=host, database=db)
    cursor = cnx.cursor()
    
    query_sql = "select SummaryNr, ProjType, ProjCost, EndUse, SIC from cases_info order by ID"
    
    cursor.execute(query_sql)
    cases_list = cursor.fetchall()
    
    for each_case in cases_list:
        
        update_sql = ("update case_employees set "
                      "ProjType = %s, ProjCost = %s, EndUse = %s, SIC = %s "
                      "where SummaryNr = %s")
        update_sql_value = (each_case[1],each_case[2],each_case[3],each_case[4],each_case[0])
        print(update_sql_value)
        cursor.execute(update_sql, update_sql_value)
        cnx.commit()
    print("Update has done!")
    
    cursor.close()
    cnx.close()
    return 1


def update_employee_detail_info_from_OSHA():
    
    
    user = 'test'
    pwd = '123456'
    host = '127.0.0.1'
    db = 'reported_fall_event'
    cnx = mysql.connector.connect(user=user, password=pwd, host=host, database=db)
    cursor = cnx.cursor()
    
    query_sql = "select SummaryNr from case_employees order by ID"
    cursor.execute(query_sql)
    employee_list = cursor.fetchall()
    
    brw = BrowserShadow()
    
    need_update = 0
    for each_employee in employee_list:
        SummaryNr_value = each_employee[0].strip()
        
        if SummaryNr_value != "202315776" and need_update == 0:
            continue
        else:
            need_update = 1
    
        print("SummaryNr :" , SummaryNr_value)
        employee_detail_info_url = "https://www.osha.gov/pls/imis/accidentsearch.accident_detail?id={SummaryNr}"
        
        employee_detail_info_url = employee_detail_info_url.format(SummaryNr = SummaryNr_value)

        res = brw.open_url(employee_detail_info_url)
        page_content = res.read()
        page_soup = BeautifulSoup(page_content, "html.parser")
        
        event_content_details = page_soup.find_all('tr')
        keyword_position = -1
        for index in range(0, len(event_content_details)):
            if event_content_details[index].get_text().find('Keywords') > -1 :
                keyword_position = index

        # do not process if there is no keyword
        if keyword_position == -1:
            continue
        
        proj_type_has = 1
        if event_content_details[keyword_position + 1].find_all('th')[0].get_text().find('End Use') < 0:
            proj_type_has = 0
        
        if proj_type_has == 0:
            index_employee_start = keyword_position + 2
        else:
            index_employee_start = keyword_position + 4
        for index in range(index_employee_start, len(event_content_details)):
            current_employee_eid = event_content_details[index].find_all('td')[0].get_text().strip()
            
            current_employee_href = event_content_details[index].find_all('td')[0].find('a')['href']
            current_employee_url_str = 'https://www.osha.gov/pls/imis/' + current_employee_href
            print(current_employee_url_str)
            
            res_employee_info = brw.open_url(current_employee_url_str)
            page_content_employee = res_employee_info.read()
            page_soup_employee = BeautifulSoup(page_content_employee, "html.parser")
            employee_content_details = page_soup_employee.find_all('tr')
            inspection_Nr_position = -1
            for index in range(0, len(employee_content_details)):
                if employee_content_details[index].get_text().find('Inspection') > -1 :
                    inspection_Nr_position = index
                    break
            if inspection_Nr_position == -1:
                continue
            
            TaskAssigned = employee_content_details[inspection_Nr_position + 13].find_all('td')[1].get_text()
            HumanFactor = employee_content_details[inspection_Nr_position + 10].find_all('td')[1].get_text()
            EnvironmentFactor = employee_content_details[inspection_Nr_position + 9].find_all('td')[1].get_text()
            EventType = employee_content_details[inspection_Nr_position + 8].find_all('td')[1].get_text()
            SourceInjury = employee_content_details[inspection_Nr_position + 7].find_all('td')[1].get_text()
            PartBody = employee_content_details[inspection_Nr_position + 6].find_all('td')[1].get_text()
            
            update_employee_injury_info_sql = ("update case_employees set "
                      "TaskAssigned = %s, HumanFactor = %s, EnvironmentFactor = %s, EventType = %s, SourceInjury = %s, PartBody = %s"
                      "where EID = %s and SummaryNr = %s")
            update_values = (TaskAssigned, HumanFactor, EnvironmentFactor, EventType, SourceInjury, PartBody, current_employee_eid, SummaryNr_value)
            
            cursor.execute(update_employee_injury_info_sql, update_values)
            cnx.commit()
            print(TaskAssigned, '--', HumanFactor, '--', EnvironmentFactor, '--', EventType, '--', SourceInjury, '--', PartBody)
    print("Update has done!")       
    return 1 

def query_multi_records_from_case_employees():
    user = 'test'
    pwd = '123456'
    host = '127.0.0.1'
    db = 'reported_fall_event'
    cnx = mysql.connector.connect(user=user, password=pwd, host=host, database=db)
    cursor = cnx.cursor()
    
    query_sql = ("select ID,EID, SummaryNr, SIC from case_employees "
                "where (EID, SummaryNr) in  (select EID, SummaryNr from case_employees group by EID, SummaryNr having count(*) > 1) "
                "and ID not in (select min(ID) from case_employees group by EID,SummaryNr having count(*)>1);")
    cursor.execute(query_sql)
    employee_list = cursor.fetchall()
    
    for each_employee in employee_list:
        delID = int(each_employee[0])
        EID = each_employee[1]
        SummaryNr = each_employee[2]
        SIC = each_employee[3]
        
        insert_sql_str = ("insert into temp_del_table "
                          "(delID, EID, SummaryNr, SIC) "
                          "values (%s, %s, %s, %s)")
        
        insert_values = (delID, EID, SummaryNr, SIC)
        print(insertion_unsort)
        cursor.execute(insert_sql_str, insert_values)
        cnx.commit()
    print("done")


if __name__ == '__main__':
    
    

# obtain the similar matrix of the occupation classes
#     occupatio_dic = occupation_statistic()
#     simi_r = get_similar_matrix(occupatio_dic)
#     print(simi_r)
    
#     process_degree()
#     process_nature()
#     occupation_dictionary = occupation_statistic()
#     process_construction()

#     cause_dict, fat_cause_dict = cause_fatcause_statistic()
#     print(cause_dict)
#     print(fat_cause_dict)
    
#     x_row = []
#     x_ticks = []
#     y_row = []
#     i = 1
#     for each_occu in occupation_dictionary:
#         if each_occu == "Occupation not reported":
#             continue
#         x_row.append(i)
#         x_ticks.append(each_occu)
#         i = i + 1
#         y_row.append(occupation_dictionary[each_occu])
#     
# 
#     plt.xticks(x_row, x_ticks, rotation='vertical')
#     plt.bar(x_row, y_row)
#     plt.show()


#     update_employee_from_cases_info()
#       
    update_employee_detail_info_from_OSHA()
    
    
    