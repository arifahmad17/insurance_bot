import mysql.connector

def DataUpdate(name,registration_date,driving_license,license_plate,types):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="insurance_info"
    )

    mycursor = mydb.cursor()
    # sql="CREATE TABLE car_insurance (name VARCHAR(255) ,registration_date  VARCHAR(255) , driving_license VARCHAR(255),license_plate VARCHAR(255),type VARCHAR(255));"
    if types==("comprehensive"):
        sql= 'INSERT INTO car_insurance (name , registration_date, driving_license,license_plate,type ) VALUES ("{0}","{1}","{2}","{3}","{4}");'.format(name,registration_date,driving_license,license_plate,500)
        # sql="CREATE TABLE car_insurance (name VARCHAR(255) ,registration_date  VARCHAR(255) , driving_license VARCHAR(255),license_plate VARCHAR(255),type VARCHAR(255));"
    elif types==("standalone-own"):
        sql= 'INSERT INTO car_insurance (name , registration_date, driving_license,license_plate,type ) VALUES ("{0}","{1}","{2}","{3}","{4}");'.format(name,registration_date,driving_license,license_plate,300)
    elif types==("standalone-third-party"):
        sql= 'INSERT INTO car_insurance (name , registration_date, driving_license,license_plate ,type) VALUES ("{0}","{1}","{2}","{3}","{4}");'.format(name,registration_date,driving_license,license_plate,150)
    
    mycursor.execute(sql)

    mydb.commit()
    print(mycursor.rowcount, "record inserted")

if __name__=="__main__":
    DataUpdate("Ahmad","23 January 2019","43534656456","UP53CE6114","comprehensive")
