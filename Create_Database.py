import mysql.connector

def create_database():


	mydb = mysql.connector.connect(host="localhost", user="root", passwd="Mymysql1")
	cur = mydb.cursor()

	# --- create database

	cur.execute("CREATE DATABASE dbms_project")
	cur.execute("USE dbms_project")

	# --- create tables
	# --- 1. Personal Details
	# --- 2. Contact Details
	# --- 3. Address
	# --- 4. Hostel Details

	cmd1 = "CREATE TABLE personal_details (" \
	"P_id INT PRIMARY KEY NOT NULL auto_increment," \
	"Name VARCHAR(255)," \
	"Aadhar_no VARCHAR(12) UNIQUE," \
	"Age INT," \
	"Arrival_date DATE," \
	"Discharge_date DATE," \
	"Coming_from VARCHAR(255)," \
	"Going_to VARCHAR(255))"

	cur.execute(cmd1)

	cmd2 = "CREATE TABLE address (" \
	"P_id INT REFERENCES personal_details(P_id) ON DELETE CASCADE," \
	"street_name VARCHAR(50)," \
	"area VARCHAR(50)," \
	"City VARCHAR(50)," \
	"Pincode INT," \
	"State VARCHAR(50)," \
	"Country VARCHAR(50))"

	cur.execute(cmd2)

	cmd3 = "CREATE TABLE contact_details (" \
	"P_id INT REFERENCES personal_details(P_id) ON DELETE CASCADE," \
	"Phone VARCHAR(15));"

	cur.execute(cmd3)

	cmd4 = "CREATE TABLE hostel_details (" \
	"P_id INT REFERENCES personal_details(P_id) ON DELETE CASCADE," \
	"Hostel_no INT," \
	"Floor_no INT," \
	"Room_no INT);"

	cur.execute(cmd4)

	# --- Commit everything

	mydb.commit()
