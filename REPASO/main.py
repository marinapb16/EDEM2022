import os
import pandas as pd
import mysql.connector

while True:
    try:

        mydb = mysql.connector.connect(
        host='localhost',
        user="root",
        password="my_secret_password",
        database="app_db",
        port=3308
        )

        break

    except:
        print('Waiting for database to intialize')
        time.sleep(1)

print("DB connected")

mycursor = mydb.cursor()


file_name = "./dataset/people.json"

df = pd.read_json(file_name)

df.to_csv("./dataset/people.csv", index=False)


sql_csv = """LOAD DATA  INFILE '/var/lib/mysql-files/%s.csv'
INTO TABLE %s 
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;""" % ('people','employees')

mycursor.execute(sql_csv)

mydb.commit()


print(df)