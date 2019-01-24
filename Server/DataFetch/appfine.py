# from trigger import *
import urllib.request as ur
import requests
import xmltodict
import platform
from os import system as sys
import pymysql
import xmltodict
import time
import datetime
import os
from .sdnTrigger import sdn_trigger

temp_now = (time.asctime(time.localtime(time.time())))
# print ('date is : ',temp_now)
now = temp_now.replace(':', '-')

name = 'sdn_xml_{}.xml'.format(now)
file_name = str(name)
print ('File name is: ', file_name)

foreing_uids = []
uids = []

def main(*args):
	conn = pymysql.connect(host='127.0.0.1', user='root', passwd=None, db='development_sdn')
	cur = conn.cursor()
	cur.execute("SELECT `sdnUrl` FROM `t_sdnsourceurl` WHERE `sdnSourceUrlStatus`='Active' ")
	for r in cur:
		for val in r:
			print (val) #This prints the selected url from the database.
			url = val
			break



	print ('Downloadig file please wait....')
	r = requests.get(url, allow_redirects=True)
	cont_type = (r.headers.get('content-type'))

	if cont_type == 'application/xml':
		print ('Progressing........')
		open('{}'.format(file_name), 'wb').write(r.content)
		print ('Done creating temporary file.')

		try:
			fh = open('{}'.format(file_name))
			getter()
		except FileNotFoundError:
			print ('File probably could not be fetched')
			main()


	else:
		print('The file you are trying to access is not an xml file')



def sort_and_store(*args):
	conn = pymysql.connect(host='127.0.0.1', user='root', passwd=None, db='development_sdn')
	cur = conn.cursor()

	with open('{}'.format(file_name)) as fd:
		doc = xmltodict.parse(fd.read())

	Entries = doc['sdnList']['sdnEntry']
	store = []


	recs = []
	conn = pymysql.connect(host='127.0.0.1', user='root', passwd=None, db='development_sdn')
	cur = conn.cursor()
	sql="SELECT `sdnUid` FROM `t_sdn_entry`"
	cur.execute(sql)
	data = cur.fetchall()
	for each in data:
		for val in each:
			recs.append(val)

	with open('{}'.format(file_name)) as file:
		doc = xmltodict.parse(file.read())

	entries = doc['sdnList']['sdnEntry']
	ids = []
	count = 0
	for each in entries:
		entry = dict(each)
		if isinstance(entry, dict):
			uid = entry['uid']
			if uid in recs:
				# print ('exist...')
				# sys('cls')
				count +=1
				pass
			else:
				lastname = entry['lastName'].replace("'", ' ')
				print (lastname)
				print (entry['uid'], lastname, entry['sdnType'], '\n')

				uid = uids[0]
				sql = "INSERT INTO `t_sdnentry` (`sdnUid`, `lastName`, `sdnType`, `sdnFetchedInformationUid`) VALUES ('{}', '{}', '{}', '{}')".format(entry['uid'], str(lastname), entry['sdnType'], uid)
				cur.execute(sql)
				conn.commit()

				store.append(entry)

	recs = len(store)
	print (len(store), ' Records added' )
	print ('{} is the new record count.'.format(recs + count))

	sql = "INSERT INTO `t_sdnfetchedinformation` (`noOfSdnRecordsFetched`) VALUES ('{}')".format(recs)
	cur.execute(sql)
	conn.commit()
	cur.close()



def getter(*args):
	# time.sleep(4)
	with open('{}'.format(file_name)) as fd:
		check = xmltodict.parse(fd.read())

	pub_date = check['sdnList']['publshInformation']['Publish_Date']

	conn = pymysql.connect(host='127.0.0.1', user='root', passwd=None, db='development_sdn')
	cur = conn.cursor()
	cur.execute('SELECT `sdnPublishDate` FROM `t_sdnupdatecheck`')

	dumps = []
	for dates in cur:
		for each in dates:
			str(each)
		dumps.append(each)

	print (dumps)
	# time.sleep(4)
	if pub_date in dumps:
		print ('No new Updates Registered.')
		cur.execute("INSERT INTO `t_sdnupdatecheck` (`sdnPublishDate`) VALUES ('{}')".format(pub_date))
		conn.commit()
		fd.close()
		print ('record kept')
		# print (datetime.datetime.now())
		# os.remove('{}'.format(file_name))

		conn.close() #Close Connection.

	else:
		print ('Possible Updates Found.')
		count = 0
		indb = []
		# new =
		# exit()
		cur.execute("INSERT INTO `t_sdnupdatecheck` (`sdnPublishDate`) VALUES ('{}')".format(pub_date))
		conn.commit()
		conn.close()

		# pre = "SELECT sdnUid FROM t_sdn_entry"
		conn = pymysql.connect(host='127.0.0.1', user='root', passwd=None, db='development_sdn')
		cur = conn.cursor()
		cur.execute("SELECT sdnUid FROM t_sdn_entry")
		dbInfo = cur.fetchall()
		for all in dbInfo:
			for one in all:
				indb.append(one)

		with open('{}'.format(file_name)) as fd:
			doc = xmltodict.parse(fd.read())

		Entries = doc['sdnList']['sdnEntry']
		# print (indb)
		for i in range(0, len(Entries)):
			e = Entries[i]
			if e['uid'] in indb:
				pass
			else:
				count += 1

		if count != 0:
			conn = pymysql.connect(host='127.0.0.1', user='root', passwd=None, db='development_sdn')
			cur = conn.cursor()
			cur.execute("INSERT INTO t_sdnfetchedinformation(noOfSdnRecordsFetched) VALUES ('{}')".format(count))
			conn.commit()
			# conn.close()
			print ('done')

			sql = "SELECT sdnFetchedInformationUid FROM t_sdnfetchedinformation WHERE noOfSdnRecordsFetched='{}'".format(count)
			cur.execute(sql)
			allInfo = cur.fetchall()
			for all in allInfo:
				for one in all:
					batch = one

			print (batch)
			# time.sleep(5)
			sdn_trigger(file_name, batch)

main()
sys('rm {}'.format(file_name))
