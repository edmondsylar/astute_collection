import os
import pymysql
import sys
import pandas as pd

def mysql_to_csv(sql, file_path, host, user, password):
    try:
        con = pymysql.connect(host=host,
                                user=user,
                                password=password)
        print('Connected to DB: {}'.format(host))
        # Read table with pandas and write to csv
        df = pd.read_sql(sql, con)
        df.to_csv(file_path, encoding='utf-8', header = True,\
         doublequote = True, sep=',', index=False)
        print('File, {}, has been created successfully'.format(file_path))
        con.close()

    except Exception as e:
        print('Error: {}'.format(str(e)))
        sys.exit(1)

# Execution Example
sql = 'Select * From development_sdn.t_sdn_entry'
file_path = '../Server/dumps.csv'
host = 'localhost'
user = 'root'
password = None
mysql_to_csv(sql, file_path, host, user, password)

# This file File that gets the updates and creates an update of them