#creates sql table
import mysql.connector as sql
import csv

username=input("Enter name of user: ")
pwd =input("Enter Password: ")
conn = sql.connect(host="localhost",user=username,passwd=pwd,database="mysql")
cursor=conn.cursor()

def createtable(file, database, table):
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
        
        plainobject = "a_" + header + " " + "varchar(200)" 
        #added a_ because some of the field names are actual keywords like from,to etc
        bigobject = bigobject + plainobject + ", "
        
    bigobject = bigobject[:-2] #removed the extra comma
    query = "create table " +  table + " ("  + bigobject + " );" 
    
    cursor.execute(query)
    

if __name__ =="__main__":
    filename = (input("Enter location of csv file: "))
    databasename = input("Enter name of Database: ")
    tablename =input("Enter Name of Table")
    createtable(filename,databasename,tablename)