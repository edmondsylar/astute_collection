from Server.DataFetch.appfine import *
import schedule
import time
import os


def job():
	main()

schedule.every(1).day.at("00:00").do(job)

#Note trigger start here
print ('Trigger started.....')
while True:
	#Start running the scheduled task.
	#os.system('screen -X - S agentOne quit')
	#if os.system('screen -dmSL agentOne python  Server/agent003.py'):
	#	print ('Server restarted')
	#lse:
	#	print ('something went wrong')
	schedule.run_pending()
	#from trigger.extractore import *
	os.system('mysqldump -u root development_sdn > Server/dumps.sql')

