#controller
import Tracker
import showslots
from create_sql_table import createtable,username,pwd
from csvtosql import convert
import querywriter
import mysql.connector as sql
conn = sql.connect(host="localhost",user=username,passwd=pwd)
cursor=conn.cursor()
ch=0
def show_data(distcode,age,dose,date):
    try:  
        Tracker.tracker(distcode,date)
        showslots.save_slots()
        createtable("session_details.csv","covid","session_details")
        createtable("data_head.csv","covid","data_head")
        convert("session_details.csv","session_details", "covid")
        convert("data_head.csv","data_head", "covid")
        result = querywriter.query_session(age,dose )
        if result!=[]:
            
            print(result)
            fh = open("yay.csv","w")
            fh.write(str(result))
        else:
            print("sorry,perhaps another time.")
    except UnboundLocalError:
        print("NO DATA FOUND")

if __name__=="__main__":
    distcodeint =input("Enter District Code")
    ageint = int(input("Enter age"))
    datestr=input("Enter the date you wish to search data for as dd-mm-yyyy")
    dosestr = input("Have you been vaccinated before? y/n")
    show_data(distcode=distcodeint,age=ageint,dose=dosestr,date=datestr)
