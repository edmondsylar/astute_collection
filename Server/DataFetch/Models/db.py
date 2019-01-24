import pymysql

connection = {
	'host':'localhost',
	'user':'root',
	'database':'development_sdn',
	'passwd':None
}


class dbModel:
	def __init__(self):
		# self.batch
		self.conn = pymysql.connect(**connection)
		self.cur = self.conn.cursor()

		# records = []
		# update_var = "SELECT sdnUid FROM t_sdn_entry"
		# self.cur.execute(update_var)
		# self.data = self.cur.fetchall()
		# for all in data:
		# 	for one in all:
		# 		records.append(one)


	def t_sdn_entry (self, uid, lastName, sdnType, fetchedInformationUid):
		records = []
		update_var = "SELECT sdnUid FROM t_sdn_entry"
		self.cur.execute(update_var)
		data = self.cur.fetchall()
		for all in data:
			for one in all:
				records.append(one)

		if uid in records:
			pass
		else:
			sql = "INSERT INTO t_sdn_entry(sdnUid, lastName, sdnType, fetchedInformationUid) VALUES ('{}', '{}', '{}', '{}')".format(uid, lastName, sdnType, fetchedInformationUid)
			self.cur.execute(sql)
			self.conn.commit()

		# exit()


	def t_sdn_firstname (self, uid, firstName, fetchedInformationUid):
		records = []
		update_var = "SELECT sdnUid FROM t_sdn_firstname"
		self.cur.execute(update_var)
		data = self.cur.fetchall()
		for all in data:
			for one in all:
				records.append(one)

		if uid in records:
			pass
		else:
			sql = "INSERT INTO t_sdn_firstname(sdnUid, firstName, fetchedInformationUid) VALUES('{}', '{}', '{}')".format(uid, firstName, fetchedInformationUid)
			self.cur.execute(sql)
			self.conn.commit()


	def t_sdn_title(self, sdnEntryUid, title, fetchedInformationUid):
		records = []
		update_var = "SELECT sdnEntryUid FROM t_sdn_title"
		self.cur.execute(update_var)
		data = self.cur.fetchall()
		for all in data:
			for one in all:
				records.append(one)

		if sdnEntryUid in records:
			pass
		else:
			sql = "INSERT INTO t_sdn_title(sdnEntryUid, title, fetchedInformationUid) VALUES('{}', '{}', '{}')".format(sdnEntryUid, title, fetchedInformationUid)
			self.cur.execute(sql)
			self.conn.commit()

	def t_sdn_remarks(self, sdnUid, remarks, fetchedInformationUid):
		records = []
		update_var = "SELECT sdnUid FROM t_sdn_remarks"
		self.cur.execute(update_var)
		data = self.cur.fetchall()
		for all in data:
			for one in all:
				records.append(one)

		if sdnUid in records:
			pass
		else:
			sql = "INSERT INTO t_sdn_remarks(sdnUid, remarks, fetchedInformationUid) VALUES ('{}', '{}', '{}')".format(sdnUid, remarks, fetchedInformationUid)
			self.cur.execute(sql)
			self.conn.commit()


	def t_sdn_programlist(self, sdnUid, program, fetchedInformationUid):
		records = []
		update_var = "SELECT sdnUid FROM t_sdn_programlist"
		self.cur.execute(update_var)
		data = self.cur.fetchall()
		for all in data:
			for one in all:
				records.append(one)

		if sdnUid in records:
			pass
		else:
			sql = "INSERT INTO t_sdn_programlist(sdnUid, program, fetchedInformationUid) VALUES ('{}', '{}', '{}')".format(sdnUid, program, fetchedInformationUid)
			self.cur.execute(sql)
			self.conn.commit()

	def t_sdn_idList(self, sdnUid, idUid, fetchedInformationUid):
		records = []
		update_var = "SELECT sdnUid FROM t_sdn_idlist"
		self.cur.execute(update_var)
		data = self.cur.fetchall()
		for all in data:
			for one in all:
				records.append(one)

		if sdnUid in records:
			pass
		else:
			sql = "INSERT INTO t_sdn_idlist(sdnUid, idUid, fetchedInformationUid) VALUES ('{}', '{}', '{}')".format(sdnUid, idUid, fetchedInformationUid)
			self.cur.execute(sql)
			self.conn.commit()


	def t_sdn_idList_idytype(self, sdnUid, idUid, idType, fetchedInformationUid):
		records = []
		update_var = "SELECT sdnUid FROM t_sdn_idlist_idtype"
		self.cur.execute(update_var)
		data = self.cur.fetchall()
		for all in data:
			for one in all:
				records.append(one)

		if sdnUid in records:
			pass
		else:
			sql = "INSERT INTO t_sdn_idlist_idtype(sdnUid, idUid, idType, fetchedInformationUid) VALUES ('{}', '{}', '{}', '{}')".format(sdnUid, idUid, idType,fetchedInformationUid)
			self.cur.execute(sql)
			self.conn.commit()

	def t_sdn_idList_idnumber(self, sdnUid, idUid, idNumber, fetchedInformationUid):
		records = []
		update_var = "SELECT sdnUid FROM t_sdn_idlist_idnumber"
		self.cur.execute(update_var)
		data = self.cur.fetchall()
		for all in data:
			for one in all:
				records.append(one)

		if sdnUid in records:
			pass
		else:
			sql = "INSERT INTO t_sdn_idlist_idnumber(sdnUid, idUid, idNumber, fetchedInformationUid) VALUES ('{}', '{}', '{}', '{}')".format(sdnUid, idUid, idNumber, fetchedInformationUid)
			self.cur.execute(sql)
			self.conn.commit()

	def t_sdn_idList_idCountry(self, sdnUid, idUid, idCountry, fetchedInformationUid):
		records = []
		update_var = "SELECT sdnUid FROM t_sdn_idlist_idcountry"
		self.cur.execute(update_var)
		data = self.cur.fetchall()
		for all in data:
			for one in all:
				records.append(one)

		if sdnUid in records:
			pass
		else:
			sql = "INSERT INTO t_sdn_idlist_idcountry(sdnUid, idUid, idCountry, fetchedInformationUid) VALUES ('{}', '{}', '{}', '{}')".format(sdnUid, idUid, idCountry, fetchedInformationUid)
			self.cur.execute(sql)
			self.conn.commit()


	def t_sdn_idList_issueDate(self, sdnUid, idUid, issueDate, fetchedInformationUid):
		records = []
		update_var = "SELECT sdnUid FROM t_sdn_idlist_issuedate"
		self.cur.execute(update_var)
		data = self.cur.fetchall()
		for all in data:
			for one in all:
				records.append(one)

		if sdnUid in records:
			pass
		else:
			sql = "INSERT INTO t_sdn_idlist_issuedate(sdnUid, idUid, issueDate, fetchedInformationUid) VALUES ('{}','{}','{}','{}')".format(sdnUid, idUid, issueDate, fetchedInformationUid)
			self.cur.execute(sql)
			self.conn.commit()

	def t_sdn_idList_expirationDate(self, sdnUid, idUid, expirationDate, fetchedInformationUid):
		records = []
		update_var = "SELECT sdnUid FROM t_sdn_idlist_expirationdate"
		self.cur.execute(update_var)
		data = self.cur.fetchall()
		for all in data:
			for one in all:
				records.append(one)

		if sdnUid in records:
			pass
		else:
			sql = "INSERT INTO `t_sdn_idlist_expirationdate`(`sdnUid`, `idUid`, `expirationDate`, `fetchedInformationUid`) VALUES ('{}', '{}', '{}', '{}')".format(sdnUid, idUid, expirationDate,fetchedInformationUid)
			self.cur.execute(sql)
			self.conn.commit()

	def t_sdn_akaList(self, sdnUid, akaUid, akaType, akaCategory, fetchedInformationUid):
		records = []
		update_var = "SELECT sdnUid FROM t_sdn_akalist"
		self.cur.execute(update_var)
		data = self.cur.fetchall()
		for all in data:
			for one in all:
				records.append(one)

		if sdnUid in records:
			pass
		else:
			sql = "INSERT INTO t_sdn_akalist(sdnUid, akaUid, akaType, akaCategory, fetchedInformationUid) VALUES ('{}', '{}', '{}', '{}', '{}')".format(sdnUid, akaUid, akaType, akaCategory, fetchedInformationUid)
			self.cur.execute(sql)
			self.conn.commit()

	def t_sdn_akaList_lastName(self, sdnUid, akaUid, akaLastName, fetchedInformationUid):
		records = []
		update_var = "SELECT sdnUid FROM t_sdn_akalist_lastname"
		self.cur.execute(update_var)
		data = self.cur.fetchall()
		for all in data:
			for one in all:
				records.append(one)

		if sdnUid in records:
			pass
		else:
			sql = "INSERT INTO t_sdn_akalist_lastname(sdnUid, akaUid, akaLastName, fetchedInformationUid) VALUES ('{}', '{}', '{}', '{}')".format(sdnUid, akaUid, akaLastName, fetchedInformationUid)
			self.cur.execute(sql)
			self.conn.commit()

	def t_sdn_akaList_firstName(self, sdnUid, akaUid, akafirstName, fetchedInformationUid):
		records = []
		update_var = "SELECT sdnUid FROM t_sdn_akalist_firstname"
		self.cur.execute(update_var)
		data = self.cur.fetchall()
		for all in data:
			for one in all:
				records.append(one)

		if sdnUid in records:
			pass
		else:
			sql = "INSERT INTO `t_sdn_akalist_firstname`(`sdnUid`, `akaUid`, `akaFfirstName`, `fetchedInformationUid`) VALUES ('{}', '{}', '{}', '{}')".format(sdnUid, akaUid, akafirstName, fetchedInformationUid)
			self.cur.execute(sql)
			self.conn.commit()

	def t_sdn_addressList(self, sdnUid, addressUid, fetchedInformationUid):
		records = []
		update_var = "SELECT sdnUid FROM t_sdn_addresslist"
		self.cur.execute(update_var)
		data = self.cur.fetchall()
		for all in data:
			for one in all:
				records.append(one)

		if sdnUid in records:
			pass
		else:
			sql ="INSERT INTO `t_sdn_addresslist`(`sdnUid`, `addressUid`, `fetchedInformationUid`) VALUES ('{}', '{}', '{}')".format(sdnUid, addressUid, fetchedInformationUid)
			self.cur.execute(sql)
			self.conn.commit()

	def t_sdn_addressList_address1(self, sdnUid, addressUid, address1, fetchedInformationUid):
		records = []
		update_var = "SELECT sdnUid FROM t_sdn_addresslist_address1"
		self.cur.execute(update_var)
		data = self.cur.fetchall()
		for all in data:
			for one in all:
				records.append(one)

		if sdnUid in records:
			pass
		else:
			sql = "INSERT INTO `t_sdn_addresslist_address1`(`sdnUid`, `addressUid`, `address1`, `fetchedInformationUid`) VALUES ('{}', '{}', '{}', '{}')".format(sdnUid, addressUid, address1, fetchedInformationUid)
			self.cur.execute(sql)
			self.conn.commit()

	def t_sdn_addressList_address2(self, sdnUid, addressUid, address2, fetchedInformationUid):
		records = []
		update_var = "SELECT sdnUid FROM t_sdn_addresslist_address2"
		self.cur.execute(update_var)
		data = self.cur.fetchall()
		for all in data:
			for one in all:
				records.append(one)

		if sdnUid in records:
			pass
		else:
			sql = "INSERT INTO  t_sdn_addresslist_address2(sdnUid, addressUid, address2, fetchedInformationUid) VALUES ('{}', '{}', '{}', '{}')".format(sdnUid, addressUid, address2, fetchedInformationUid)
			self.cur.execute(sql)
			self.conn.commit()

	def t_sdn_addressList_address3(self, sdnUid, addressUid, address3, fetchedInformationUid):
		records = []
		update_var = "SELECT sdnUid FROM t_sdn_addresslist_address3"
		self.cur.execute(update_var)
		data = self.cur.fetchall()
		for all in data:
			for one in all:
				records.append(one)

		if sdnUid in records:
			pass
		else:
			sql = "INSERT INTO  t_sdn_addresslist_address3(sdnUid, addressUid, address3, fetchedInformationUid) VALUES ('{}', '{}', '{}', '{}')".format(sdnUid, addressUid, address3, fetchedInformationUid)
			self.cur.execute(sql)
			self.conn.commit()

	def t_sdn_addressList_city(self, sdnUid, addressUid, city, fetchedInformationUid):
		records = []
		update_var = "SELECT sdnUid FROM t_sdn_addresslist_city"
		self.cur.execute(update_var)
		data = self.cur.fetchall()
		for all in data:
			for one in all:
				records.append(one)

		if sdnUid in records:
			pass
		else:
			sql = "INSERT INTO `t_sdn_addresslist_city`(`sdnUid`, `addressUid`, `city`, `fetchedInformationUid`) VALUES ('{}', '{}', '{}', '{}')".format(sdnUid, addressUid, city, fetchedInformationUid)
			self.cur.execute(sql)
			self.conn.commit()

	def t_sdn_addressList_stateorProvince(self, sdnUid, addressUid, stateOrProvince, fetchedInformationUid):
		records = []
		update_var = "SELECT sdnUid FROM t_sdn_addresslist_stateorprovince"
		self.cur.execute(update_var)
		data = self.cur.fetchall()
		for all in data:
			for one in all:
				records.append(one)

		if sdnUid in records:
			pass
		else:
			sql = "INSERT INTO `t_sdn_addresslist_stateorprovince`(`sdnUid`, `addressUid`, `stateOrProvince`, `fetchedInformationUid`) VALUES ('{}', '{}', '{}', '{}')".format(sdnUid, addressUid, stateOrProvince, fetchedInformationUid)
			self.cur.execute(sql)
			self.conn.commit()

	def t_sdn_addressList_postalCode(self, sdnUid, addressUid, postalCode, fetchedInformationUid):
		records = []
		update_var = "SELECT sdnUid FROM t_sdn_addresslist_postalcode"
		self.cur.execute(update_var)
		data = self.cur.fetchall()
		for all in data:
			for one in all:
				records.append(one)

		if sdnUid in records:
			pass
		else:
			sql = "INSERT INTO `t_sdn_addresslist_postalcode`(`sdnUid`, `addressUid`, `postalCode`, `fetchedInformationUid`) VALUES ('{}', '{}', '{}', '{}')".format(sdnUid, addressUid, postalCode, fetchedInformationUid)
			self.cur.execute(sql)
			self.conn.commit()

	def t_sdn_addressList_country(self, sdnUid, addressUid, country, fetchedInformationUid):
		records = []
		update_var = "SELECT sdnUid FROM t_sdn_addresslist_country"
		self.cur.execute(update_var)
		data = self.cur.fetchall()
		for all in data:
			for one in all:
				records.append(one)

		if sdnUid in records:
			pass
		else:
			sql = "INSERT INTO `t_sdn_addresslist_country`(`sdnUid`, `addressUid`, `country`, `fetchedInformationUid`) VALUES ('{}', '{}', '{}', '{}')".format(sdnUid, addressUid, country, fetchedInformationUid)
			self.cur.execute(sql)
			self.conn.commit()


	def t_sdn_nationalityList(self, sdnUid, nationalityUid, country, mainEntry, fetchedInformationUid):
		records = []
		update_var = "SELECT sdnUid FROM t_sdn_nationalitylist"
		self.cur.execute(update_var)
		data = self.cur.fetchall()
		for all in data:
			for one in all:
				records.append(one)

		if sdnUid in records:
			pass
		else:
			sql = "INSERT INTO `t_sdn_nationalitylist`(`sdnUid`, `nationalityUid`, `country`, `mainEntry`, `fetchedInformationUid`) VALUES ('{}', '{}', '{}', '{}', '{}')".format(sdnUid, nationalityUid, country, mainEntry, fetchedInformationUid)
			self.cur.execute(sql)
			self.conn.commit()

	def t_sdn_citizenshipList(self, sdnUid, citizenshipUid, country, mainEntry, fetchedInformationUid):
		records = []
		update_var = "SELECT sdnUid FROM t_sdn_citizenshiplist"
		self.cur.execute(update_var)
		data = self.cur.fetchall()
		for all in data:
			for one in all:
				records.append(one)

		if sdnUid in records:
			pass
		else:
			sql = "INSERT INTO `t_sdn_citizenshiplist`(`sdnUid`, `citizenshipUid`, `country`, `mainEntry`, `fetchedInformationUid`) VALUES ('{}', '{}', '{}', '{}', '{}')".format(sdnUid, citizenshipUid, country, mainEntry, fetchedInformationUid)
			self.cur.execute(sql)
			self.conn.commit()

	def t_sdn_dateOfBirthList(self, sdnUid, dateOfBirthUid, dateOfBirth, mainEntry, fetchedInformationUid):
		records = []
		update_var = "SELECT sdnUid FROM t_sdn_dateofbirthlist"
		self.cur.execute(update_var)
		data = self.cur.fetchall()
		for all in data:
			for one in all:
				records.append(one)

		if sdnUid in records:
			pass
		else:
			sql = "INSERT INTO `t_sdn_dateofbirthlist`(`sdnUid`, `dateOfBirthUid`, `dateOfBirth`, `mainEntry`, `fetchedInformationUid`) VALUES ('{}', '{}', '{}', '{}', '{}')".format(sdnUid, dateOfBirthUid, dateOfBirth, mainEntry, fetchedInformationUid)
			self.cur.execute(sql)
			self.conn.commit()

	def t_sdn_placeOfBirthList(self, sdnUid, placeOfBirthUid, placeOfBirth, mainEntry, fetchedInformationUid):
		records = []
		update_var = "SELECT sdnUid FROM t_sdn_placeofbirthlist"
		self.cur.execute(update_var)
		data = self.cur.fetchall()
		for all in data:
			for one in all:
				records.append(one)

		if sdnUid in records:
			pass
		else:
			sql = "INSERT INTO `t_sdn_placeofbirthlist`(`sdnUid`,`placeOfBirthUid`,`placeOfBirth`,`mainEntry`, `fetchedInformationUid`) VALUES ('{}', '{}', '{}', '{}', '{}')".format(sdnUid, placeOfBirthUid, placeOfBirth, mainEntry, fetchedInformationUid)
			self.cur.execute(sql)
			self.conn.commit()

	def t_sdn_vesselInfo(self, sdnUid, fetchedInformationUid):
		records = []
		update_var = "SELECT sdnUid FROM t_sdn_vesselinfo"
		self.cur.execute(update_var)
		data = self.cur.fetchall()
		for all in data:
			for one in all:
				records.append(one)

		if sdnUid in records:
			pass
		else:
			sql = "INSERT INTO `t_sdn_vesselinfo`(`sdnUid`, `fetchedInformationUid`) VALUES ('{}', '{}')".format(sdnUid, fetchedInformationUid)
			self.cur.execute(sql)
			self.conn.commit()

	def t_sdn_vesselInfo_callSign(self,sdnVesselInfoUuid, sdnUid, callSign, fetchedInformationUid):
		records = []
		update_var = "SELECT sdnUid FROM t_sdn_vesselinfo_callsign"
		self.cur.execute(update_var)
		data = self.cur.fetchall()
		for all in data:
			for one in all:
				records.append(one)

		if sdnUid in records:
			pass
		else:
			sql = "INSERT INTO `t_sdn_vesselinfo_callsign`(`sdnVesselInfoUuid`,`sdnUid`, `callSign`, `fetchedInformationUid`) VALUES ('{}', '{}', '{}', '{}')".format(sdnVesselInfoUuid, sdnUid, callSign, fetchedInformationUid)
			self.cur.execute(sql)
			self.conn.commit()

	def t_sdn_vesselInfo_vesselType(self, sdnVesselInfoUuid, sdnUid, vesselType, fetchedInformationUid):
		records = []
		update_var = "SELECT sdnUid FROM t_sdn_vesselinfo_vesseltype"
		self.cur.execute(update_var)
		data = self.cur.fetchall()
		for all in data:
			for one in all:
				records.append(one)

		if sdnUid in records:
			pass
		else:
			sql = "INSERT INTO `t_sdn_vesselinfo_vesseltype`(`sdnVesselInfoUuid`,`sdnUid`, `vesselType`, fetchedInformationUid) VALUES ('{}', '{}', '{}', '{}')".format(sdnVesselInfoUuid, sdnUid, vesselType, fetchedInformationUid)
			self.cur.execute(sql)
			self.conn.commit()

	def t_sdn_vesselInfo_vesselFlag(self, sdnVesselInfoUuid, sdnUid, vesselFlag, fetchedInformationUid):
		records = []
		update_var = "SELECT sdnUid FROM t_sdn_vesselinfo_vesselflag"
		self.cur.execute(update_var)
		data = self.cur.fetchall()
		for all in data:
			for one in all:
				records.append(one)

		if sdnUid in records:
			pass
		else:
			sql = "INSERT INTO `t_sdn_vesselinfo_vesselflag`(`sdnVesselInfoUuid`, `sdnUid`, `vesselFlag`, fetchedInformationUid) VALUES ('{}','{}', '{}', '{}')".format(sdnVesselInfoUuid, sdnUid, vesselFlag, fetchedInformationUid)
			self.cur.execute(sql)
			self.conn.commit()

	def t_sdn_vesselInfo_vesselOwner(self, sdnVesselInfoUuid, sdnUid, vesselOwner, fetchedInformationUid):
		records = []
		update_var = "SELECT sdnUid FROM t_sdn_vesselinfo_vesselowner"
		self.cur.execute(update_var)
		data = self.cur.fetchall()
		for all in data:
			for one in all:
				records.append(one)

		if sdnUid in records:
			pass
		else:
			sql = "INSERT INTO `t_sdn_vesselinfo_vesselowner`(`sdnVesselOwnerUuid`, `sdnUid`, `vesselOwner`, fetchedInformationUid) VALUES ('{}', '{}', '{}', '{}')".format(sdnVesselInfoUuid, sdnUid, vesselOwner, fetchedInformationUid)
			self.cur.execute(sql)
			self.conn.commit()

	def t_sdn_vesselInfo_tonnage(self, sdnVesselInfoUuid, sdnUid, tonnage, fetchedInformationUid):
		records = []
		update_var = "SELECT sdnUid FROM t_sdn_vesselinfo_tonnage"
		self.cur.execute(update_var)
		data = self.cur.fetchall()
		for all in data:
			for one in all:
				records.append(one)

		if sdnUid in records:
			pass
		else:
			sql = "INSERT INTO `t_sdn_vesselinfo_tonnage`(`sdnVesselInfoUuid`, `sdnUid`, `tonnage`, fetchedInformationUid) VALUES ('{}', '{}', '{}', '{}')".format(sdnVesselInfoUuid, sdnUid, tonnage,fetchedInformationUid)
			self.cur.execute(sql)
			self.conn.commit()


	def t_sdn_vesselInfo_grossRegisteredTonnage(self, sdnVesselInfoUuid, sdnUid, grossRegisteredTonnage, fetchedInformationUid):
		records = []
		update_var = "SELECT sdnUid FROM t_sdn_vesselinfo_grossregisteredtonnage"
		self.cur.execute(update_var)
		data = self.cur.fetchall()
		for all in data:
			for one in all:
				records.append(one)

		if sdnUid in records:
			pass
		else:
			sql = "INSERT INTO `t_sdn_vesselinfo_grossregisteredtonnage`(`sdnVesselInfoUuid`, `sdnUid`, `grossRegisteredTonnage`, `fetchedInformationUid`) VALUES ('{}', '{}', '{}', '{}')".format(sdnVesselInfoUuid, sdnUid, grossRegisteredTonnage, fetchedInformationUid)
			self.cur.execute(sql)
			self.conn.commit()
