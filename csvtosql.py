import mysql.connector as sql
import csv
from create_sql_table import username,pwd
hostname="localhost"

dbName="covid"
conn = sql.connect(host=hostname, password=pwd, user=username, database=dbName)
cursor = conn.cursor()

cursor.execute('set global max_allowed_packet=67108864;')
#awares mySQL that the query may be bigger than its default limit
def colonify(string):
    string = "\"" + string  + "\""
    return string 
    #adds little "" in front of the string.
def listintoquery(list, table):
    query = "insert into " + table + " values("
    for i in list:
        ist=colonify(i)
        query = query + ist +" , "
    query =  query[:-2]  + " );"
    return query
    #takes in list, throws out a well-written ready-to-execute mySQL query
def convert(location, table, databaseName):
    query = "use "+databaseName+";"
    cursor.execute(query)
    with open(location, 'r') as csvfile:
        hobj = csv.reader(csvfile)
        for row in hobj:
            exec = listintoquery(row,table)
            #half the rows in the csv files are blank. in that case, this affects the structure of the query.
            if len(exec)>50:
                
                cursor.execute(exec)
        
    conn.commit()

if __name__=="__main__":
        loc=input("Enter file location: ")
        
        databaseName = input("What is the name of database you want to write this data in?")
        tabledata = input("What is the name of table you want to write this data in?")
        print("Working on it...")
        convert(loc, tabledata,databaseName)
        print("Successful!")
        
    