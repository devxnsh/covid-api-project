import mysql.connector as sql
import Tracker
import showslots
from create_sql_table import createtable,UserName, UserPassword
from csvtosql import convert

conn = sql.connect(host="localhost",user=UserName,passwd=UserPassword,database="covid")
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

#Can be updated in next version with availability of entire data altogether.
# def query_datahead(block_name):
#     cursor.execute("use covid;")
#     query = "select a_name,a_address,a_fee_type,a_block_name from data_head where a_block_name=\" " + block_name + "\" " 
#     cursor.execute(query)
#     blocks = cursor.fetchall()
#     return blocks

def show_data(distcode,age,dose,date):
    try:  
        Tracker.tracker(distcode,date)
        showslots.save_slots()
        createtable("session_details.csv","covid","session_details")
        createtable("data_head.csv","covid","data_head")
        convert("session_details.csv","session_details", "covid")
        convert("data_head.csv","data_head", "covid")
        result = query_session(age,dose)
        if result!=[]:
            
            print(result)
            fh = open("yay.csv","w")
            fh.write(str(result))
        else:
            print("sorry,perhaps another time.")
    except UnboundLocalError:
        print("NO DATA FOUND")