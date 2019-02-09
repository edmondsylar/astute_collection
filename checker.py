import xmltodict
import pymysql

connection = {
    'host':'192.168.8.5',
    'user':'client',
    'password':None,
    'database':'astute-client'
    }


conn = pymysql.connect(**connection)
cur = conn.cursor()



with open('file.xml') as fd:
    check = xmltodict.parse(fd.read())

pub_date = check['sdnList']['publshInformation']['Publish_Date']
rec_count = check['sdnList']['publshInformation']['Record_Count']

print ('Published date: ',pub_date,'\nRecord count:', rec_count)


dates = []
recs = []

sql = 'SELECT * FROM t_sdnupdatecheck'
cur.execute(sql)
data = cur.fetchall()
for each in data:
    for one in each:
