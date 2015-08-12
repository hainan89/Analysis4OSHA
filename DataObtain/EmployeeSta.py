'''
Created on 2015年7月28日

@author: hainan
'''

import mysql.connector
import sys, os


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
    for item in degree_list:
        current_degree = item[0]
        if len(current_degree) == 0:
            current_degree = "Non record"
        if current_degree not in degree_dictionary:
            degree_dictionary[current_degree] = 1
        else:
            degree_dictionary[current_degree] = degree_dictionary[current_degree] + 1
    
    cursor.close()
    cnx.close()
    print(degree_dictionary)

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
    for item in nature_list:
        current_degree = item[0]
        if len(current_degree) == 0:
            current_degree = "Non record"
            
        degree_list = current_degree.split('/')
        
        for degree_item in degree_list:
            if degree_item not in nature_dictionary:
                nature_dictionary[degree_item] = 1
            else:
                nature_dictionary[degree_item] = nature_dictionary[degree_item] + 1
    
    cursor.close()
    cnx.close()
    print(nature_dictionary)
    print(nature_dictionary['Non record'])

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

if __name__ == '__main__':
    #process_degree()
    process_nature()
    
    