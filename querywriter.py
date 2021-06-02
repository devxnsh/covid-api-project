import mysql.connector as sql
from create_sql_table import username,pwd
conn = sql.connect(host="localhost",user=username,passwd=pwd,database="covid")
cursor=conn.cursor()
def query_session(age, dose):    
    
    if age >= 45:
        min_age_limit = "45"
    elif age>=18 and age<45:
        min_age_limit = "18"
    else:
        print("noneligible")
        min_age_limit = 0
    #to display results for specified age field only
    if dose == 'y':
        dosedet = "a_available_capacity_dose2"
    elif dose == 'n':
        dosedet = "a_available_capacity_dose1"
    #to display only relevant dose info
    if min_age_limit!=0 :
            cursor.execute("use covid;")
            query = "Select a_vaccine, " +dosedet+", a_slots, " + dosedet + " from session_details where a_min_age_limit = " + min_age_limit + " and "+dosedet+">0;"
            #shows vaccine type, available capacity,time slots,
            
            cursor.execute(query)
            
            result = cursor.fetchall()
            return result

def query_datahead(block_name):
    cursor.execute("use covid;")
    query = "select a_name,a_address,a_fee_type,a_block_name from data_head where a_block_name=\" " + block_name + "\" " 
    cursor.execute(query)
    blocks = cursor.fetchall()
    return blocks
if __name__ == "__main__" :
    age = int(input("enter age"))
    doser = input("have you taken covid dose before y/n")
    blockname = ("Please enter your main city area or block name")
    result = query_session(age,doser)   
    print(result)
    blockresult = query_datahead(blockname)
    print(blockresult)    