#creates sql table
import mysql.connector as sql
import csv

UserName=input("Enter Name of the User: ")
UserPassword=input("Enter Database Password: ")
conn = sql.connect(host="localhost",user=UserName, passwd=UserPassword,database="covid")
cursor=conn.cursor()

def createtable(file, database, table):
    try:
        dataquery = "create database if not   exists " + database+ ";" 
        cursor.execute(dataquery)    
        #creates database if it doesnt already exist in mysql command line.
        cursor.execute("use "+  database + ";")
        cursor.execute("drop table if exists " +  table+ ";")
        
        fh = open(file, "r")
        lineobj = csv.reader(fh)
        for i in lineobj:
            headings = i
            break 

        bigobject = " "
        for header in headings:
            
            plainobject = "a_" + header + " " + "varchar(200)"   #added a_ because some of the field names are actual keywords like from,to etc
            bigobject = bigobject + plainobject + ", "
            
        bigobject = bigobject[:-2] #removed the extra comma
        query = "create table " +  table + " ("  + bigobject + " );" 
        
        cursor.execute(query)
    except UnboundLocalError:
        print("No Sessions Found")
        query = "create table " +  table + "(Nil bool);" 
        cursor.execute(query)
