# from multiprocessing import connection
import mysql.connector
from datetime import date

def date_exp(string):
    string.replace(" ","")
    date=string[:2]
    month=string[2:len(string)-4]
    year=string[-4:]
    year=str(int(year)+1)
    # if (date="29" and month="February"):
    #     date=str(int(date)-1)
    new_date=date+" "+ month+" "+year

    return new_date

def DataUpdate(name,registration_date,driving_license,license_plate,types,price):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="insurance_info"
    )
    today=date.today()
    d=today.strftime("%d%B%Y")
    expiry_date=date_exp(d)

    mycursor = mydb.cursor()
    # sql="CREATE TABLE car_insurance (name VARCHAR(255) ,registration_date  VARCHAR(255) , driving_license VARCHAR(255),license_plate VARCHAR(255),types VARCHAR(255),price int);"

    sql = 'INSERT INTO car_insurance (name , registration_date, driving_license,license_plate,types,price,expiry_date) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}","{6}");'.format(name,registration_date,driving_license,license_plate,types,price,expiry_date)
    
    mycursor.execute(sql)

    mydb.commit()
    print(mycursor.rowcount, "record inserted")


if __name__=="__main__":
    DataUpdate("Ahmad","23 January 2019","43534656456","UP53CE6114","Comprehensive",500)

def GetData(license_plate):


    try:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="insurance_info"
    )
        cursor=mydb.cursor()
        sql_select_Query = """select * from car_insurance where license_plate = %s"""
    
        cursor.execute(sql_select_Query,(license_plate,))
        # get all records
        records = cursor.fetchall()
        # print("Total number of rows in table: ", cursor.rowcount)
        ans=[]
        for row in records:
            ans=[row[4],row[5],row[6]]
            
        return ans
    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    # finally:
    #     if connection.is_connected():
    #         connection.close()
    #         cursor.close()
