import mysql.connector
from datetime import datetime, timedelta
from random import choice

mydb = mysql.connector.connect(host="localhost", user="root", passwd="Mymysql1")

def insert_data():
	person_details = open('person_details.txt', 'r')
	contact_details = open('contact_details.txt', 'r')
	address_details = open('address.txt', 'r')

	cmd = "INSERT INTO personal_details (name, aadhar_no, age, arrival_date, discharge_date, coming_from, going_to)" \
		"VALUES (%s, %s, %s, %s, %s, %s, %s)"
	ins = []

	for line in person_details.readlines():
		val = line.split(',')
		val[-1] = val[-1][0:-1]
		val[3] = datetime.strptime(val[3], "%Y-%m-%d").date()
		ins.append((val[0], val[1], int(val[2]), val[3], val[3]+timedelta(days=14), val[4], val[5]))
	
	cur = mydb.cursor()
	cur.execute("USE dbms_project")
	cur.executemany(cmd, ins)

	cmd = "INSERT INTO contact_details (P_id, phone)" \
		"VALUES (%s, %s)"
	ins = []

	for line in contact_details.readlines():
		val = line.split(',')
		val[-1] = val[-1][0:-1]
		p_id = 0
		find_p_id = "SELECT P_id FROM personal_details WHERE aadhar_no = %s"
		to_find = (int(val[0]), )
		cur.execute(find_p_id, to_find)
		for t in cur: 
			for x in t: p_id = x
		ins.append((p_id, int(val[1])))

	cur.executemany(cmd, ins)

	cmd = "INSERT INTO address (p_id, street_name, area, city, pincode, state, country)" \
		"VALUES (%s, %s, %s, %s, %s, %s, %s)"
	ins = []

	for line in address_details.readlines():
		val = line.split(',')
		val[-1] = val[-1][0:-1]
		p_id = 0
		find_p_id = "SELECT P_id FROM personal_details WHERE aadhar_no = %s"
		to_find = (int(val[0]), )
		cur.execute(find_p_id, to_find)
		for t in cur: 
			for x in t: p_id = x
		ins.append((p_id, val[1], val[2], val[3], int(val[4]), val[5], val[6]))

	cur.executemany(cmd, ins)

	cmd = "INSERT INTO hostel_details (P_id, hostel_no, floor_no, room_no)" \
		"VALUES (%s, %s, %s, %s)"
	ins = []

	cur.execute("SELECT p_id, age FROM personal_details")

	grd_flr_room = [i for i in range(1000, 1100)]
	for i in range(2000, 2100):
		grd_flr_room.append(i)

	fir_flr_room = [i for i in range(1100, 1200)]
	for i in range(2100, 2200):
		fir_flr_room.append(i)

	sec_flr_room = [i for i in range(1200, 1250)]
	for i in range(2200, 2250):
		sec_flr_room.append(i)

	for t in cur:
		p_id, age = t[0], t[1]
		room_no = 0
		if age >= 60:
			room_no = choice(grd_flr_room)
			grd_flr_room.remove(room_no)
		elif age >= 40:
			room_no = choice(fir_flr_room)
			fir_flr_room.remove(room_no)
		else:
			room_no = choice(sec_flr_room)
			sec_flr_room.remove(room_no)
		floor_no = (room_no//100)%10
		hostel_no = (room_no//1000)
		ins.append((p_id, hostel_no, floor_no, room_no))

	cur.executemany(cmd, ins)

	mydb.commit()