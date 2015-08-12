import mysql.connector
import csv

from DecisionTree.ClassesCode import ClasesCode

def purify_dataset():
    user = "test"
    pwd = "123456"
    host = "127.0.0.1"
    db = "reported_fall_event"
    cnx = mysql.connector.connect(user=user, password=pwd, host=host, database=db)
    cursor = cnx.cursor()

    query_sql = "select SummaryNr, Degree, Nature, Occupation, FallDist, Cause, FatCause from case_employees order by ID"
    cursor.execute(query_sql)

    data_list = cursor.fetchall()

    storage_data_header = ["SummaryNr", "Degree", "Nature", "Occupation", "FallDist", "Cause", "FatCause"]
    
    clases_code = ClasesCode()
    
    with open('coded_data_set.csv', 'w', newline='') as comp_r_csv:
        spamwriter = csv.writer(comp_r_csv, dialect='excel')
        spamwriter.writerow(storage_data_header)
        for row in data_list:
            print(row[1], "--", row[2], "--", row[3], "--", row[4], "--", row[5], "--", row[6])
            if len(row[1]) == 0: # degree
                continue
            if len(row[2]) == 0: # nature
                continue
            if len(row[3]) == 0: # Occupation
                continue
            if int(row[4]) == 0: # FallDist
                continue
            if len(row[5].strip()) == 0: # cause
                continue
            if len(row[6].strip()) == 0: # cause
                continue

            SummaryNr = row[0]
            Degree = clases_code.DegreeTypeCode[row[1]]
            Nature = clases_code.NatureTypeCode[row[2]]
            Occupation = clases_code.OccupationTypeCode[row[3]] #OccupationTypeCode[row[3]]

            if row[4] < 12:
                FallDist = 1
            elif row[4] >= 12 and row[4] < 24:
                FallDist = 2
            else:
                FallDist = 3

            Cause = clases_code.CauseTypeCode[row[5]] #CauseTypeCode[row[5]]
            FatCause = clases_code.FatCauseTypeCode[row[6]] #FatCauseTypeCode[row[6]]
                
            
            record_row = [SummaryNr, Degree, Nature, Occupation, FallDist, Cause, FatCause]
            spamwriter.writerow(record_row)
            print(record_row)
    print("Data Purifying has Done!")
    return 
            
        

if __name__ == '__main__':
    
    purify_dataset()
