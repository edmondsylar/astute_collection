import pymysql
from flask import make_response, jsonify
import jwt
import datetime

connection = {
    'host':'localhost',
    'user':'root',
    'passwd':None,
    'database':'development_sdn'
}

fileName = 'dumps.csv'
licenses = []
clients = []

class UserModel:
    def __init__(self):
        self.conn = pymysql.connect(**connection)
        self.cur = self.conn.cursor()

        sql_license = "SELECT licenceUuid FROM t_licence"
        self.cur.execute(sql_license)
        for everything in self.cur:
            for one in everything:
                licenses.append(one)

        sql_clients = "SELECT clientUuid FROM t_clients"
        self.cur.execute(sql_clients)
        for all_clients in self.cur:
            for client in all_clients:
                clients.append(client)



    def credentials_cheker(self, client, license):
        if ((client in clients) and (license in licenses)):
            # If the infomation provided in valid and acurate.
            return self.validating_infomation(client, license)

        elif ((client in clients) and (license not in licenses)):
            # This checks if the client exists but the license doesnt.
            return ('The license is not registered')

        elif ((client not in clients) and (license in licenses)):
            # This checks if the license if valid but the client doesnt exists
            return ('The client trying to access this infomation is restricted or not in our databases.')

        else:
            return ('Wrong credentials or trying to breach system')



    def validating_infomation(self, client, license):
        get_intelligence_name = "SELECT intelligence_name FROM t_licence WHERE clientUuid='{}' AND licenceUuid='{}'".format(client, license)
        self.cur.execute(get_intelligence_name)
        result = self.cur.fetchall()
        if len(result) <= 0:
            return ('This user has been unenroled from the service.')
        else:
            for each in result:
                for c in each:
                    intel = c
            get_client = "SELECT clientName FROM t_clients WHERE clientUuid='{}'".format(client)
            self.cur.execute(get_client)
            name_container = self.cur.fetchall()
            if len(name_container) <=0 :
                return jsonify({'error':'System ran into an error'})

            else:
                token = jwt.encode({client:license, 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=5)}, 'secret',algorithm='HS256')
                return (token)

    def monitor(self):
        update = "SELECT * FROM t_sdnupdatecheck"
        self.cur.execute(update)
        mon = self.cur.fetchall()
        return """
	<html>
	<head> <title>Admin Monitor Dashboard</title>
	</head>
	<body>
	<h1> Welcome Admin Edmond</h1>
	<p>You have {} records in the table</p><br>
	{}
	<br><br><br><br><br>
	&copy Copyright Astute Server 2019

	</body>
""".format(len(mon), mon)

