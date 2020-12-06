import mysql.connector
from datetime import datetime, timedelta
from Create_Database import create_database
from Insert_Data import insert_data
import tkinter as tk
from tkinter import ttk, filedialog, Text
from tkinter import messagebox
from random import choice
from PIL import Image, ImageTk

resource_file = open("resources.txt", "r")
resource = {}
data = resource_file.readlines()
for lines in data:
	lines = list(lines.split())
	resource[lines[0]] = bool(int(lines[1]))

if resource["first_time"]:
	create_database()
	insert_data()
	resource_file.close()
	resource_file = open('resources.txt', 'w')
	resource_file.write('first_time 0')

mydb = mysql.connector.connect(host="localhost", user="root", password="Mymysql1", database="dbms_project")
cur = mydb.cursor()

grd_flr_room = [i for i in range(1000, 1100)]
for i in range(2000, 2100):
	grd_flr_room.append(i)

fir_flr_room = [i for i in range(1100, 1200)]
for i in range(2100, 2200):
	fir_flr_room.append(i)

sec_flr_room = [i for i in range(1200, 1250)]
for i in range(2200, 2250):
	sec_flr_room.append(i)

cur.execute("select discharge_date, room_no, floor_no from personal_details p join hostel_details h on p.p_id = h.p_id")
for p in cur:
	date, room, f_no = p[0], int(p[1]), int(p[2])
	today = datetime.now().date()
	if date > today:
		if f_no == 0:   grd_flr_room.remove(room)
		elif f_no == 1: fir_flr_room.remove(room)
		else: sec_flr_room.remove(room)

cur.close()
mydb.close()

class DatabaseView:
	def __init__(self, data):
		self.databaseViewWindow = tk.Tk()
		self.databaseViewWindow.wm_title("Database View")

		# Label widgets
		tk.Label(self.databaseViewWindow, text = "Database View Window",  width = 25).grid(pady = 5, column = 1, row = 1)

		self.databaseView = ttk.Treeview(self.databaseViewWindow)
		self.databaseView.grid(pady = 5, column = 1, row = 2)
		self.databaseView["show"] = "headings"
		self.databaseView["columns"] = ("p_id", "name", "aadhar_no", "age", "arrival_date", "discharge_date", "coming_from", "going_to", "phone", "street_name", "area", "city", "pincode", "state", "country", "hostel_no", "floor_no", "room_no")

		# Treeview column headings
		self.databaseView.heading("p_id", text = "Patient ID")
		self.databaseView.heading("name", text = "Name")
		self.databaseView.heading("aadhar_no", text = "Aadhar Number")
		self.databaseView.heading("age", text = "Age")
		self.databaseView.heading("arrival_date", text = "Arrival Date")
		self.databaseView.heading("discharge_date", text = "Discharge Date")
		self.databaseView.heading("coming_from", text = "Coming From")
		self.databaseView.heading("going_to", text = "Going To")
		self.databaseView.heading("phone", text = "Phone Number")
		self.databaseView.heading("street_name", text = "Street Name")
		self.databaseView.heading("area", text = "Area")
		self.databaseView.heading("city", text = "City")
		self.databaseView.heading("pincode", text = "Pincode")
		self.databaseView.heading("state", text = "State")
		self.databaseView.heading("country", text = "Country")
		self.databaseView.heading("hostel_no", text = "Hostel No")
		self.databaseView.heading("floor_no", text = "Floor")
		self.databaseView.heading("room_no", text = "Room No")

		# Treeview columns
		self.databaseView.column("p_id", width = 40)
		self.databaseView.column("name", width = 100)
		self.databaseView.column("aadhar_no", width = 90)
		self.databaseView.column("age", width = 40)
		self.databaseView.column("arrival_date", width = 70)
		self.databaseView.column("discharge_date", width = 70)
		self.databaseView.column("coming_from", width = 90)
		self.databaseView.column("going_to", width = 90)
		self.databaseView.column("phone", width = 70)
		self.databaseView.column("street_name", width = 100)
		self.databaseView.column("area", width = 100)
		self.databaseView.column("city", width = 100)
		self.databaseView.column("pincode", width = 50)
		self.databaseView.column("state", width = 80)
		self.databaseView.column("country", width = 60)
		self.databaseView.column("hostel_no", width = 40)
		self.databaseView.column("floor_no", width = 40)
		self.databaseView.column("room_no", width = 40)

		for x in data:
			self.databaseView.insert('', 'end', values=x)

		self.databaseViewWindow.mainloop()

class InsertWindow:
	def __init__(self):
		self.window = tk.Tk()
		self.window.wm_title("Insert data")

		self.mydb = mysql.connector.connect(host='localhost', user="root", password="Mymysql1", database='dbms_project')
		self.cur = self.mydb.cursor()

		# Initializing all the variables
		self.name = tk.StringVar()
		self.aadhar_no = tk.StringVar()
		self.age = tk.IntVar()
		self.arrival_date = datetime.now().date()
		self.discharge_date = self.arrival_date + timedelta(days=14)
		self.coming_from = tk.StringVar()
		self.going_to = tk.StringVar()
		self.street_name = tk.StringVar()
		self.area = tk.StringVar()
		self.city = tk.StringVar()
		self.pincode = tk.IntVar()
		self.state = tk.StringVar()
		self.country = tk.StringVar()
		self.phone_no = tk.StringVar()

		# Labels
		tk.Label(self.window, text = "Name",  width = 25).grid(pady = 5, column = 1, row = 1)
		tk.Label(self.window, text = "Aadhar Number",  width = 25).grid(pady = 5, column = 1, row = 2)
		tk.Label(self.window, text = "Age",  width = 25).grid(pady = 5, column = 1, row = 3)
		tk.Label(self.window, text = "Coming From",  width = 25).grid(pady = 5, column = 1, row = 4)
		tk.Label(self.window, text = "Going to",  width = 25).grid(pady = 5, column = 1, row = 5)
		tk.Label(self.window, text = "Street Name",  width = 25).grid(pady = 5, column = 1, row = 6)
		tk.Label(self.window, text = "Area",  width = 25).grid(pady = 5, column = 1, row = 7)
		tk.Label(self.window, text = "City",  width = 25).grid(pady = 5, column = 1, row = 8)
		tk.Label(self.window, text = "Pincode",  width = 25).grid(pady = 5, column = 1, row = 9)
		tk.Label(self.window, text = "State",  width = 25).grid(pady = 5, column = 1, row = 10)
		tk.Label(self.window, text = "Country",  width = 25).grid(pady = 5, column = 1, row = 11)
		tk.Label(self.window, text = "Phone number(s)",  width = 25).grid(pady = 5, column = 1, row = 12)

		# Fields
		# Entry widgets
		self.nameEntry = tk.Entry(self.window,  width = 25, textvariable = self.name)
		self.aadhar_noEntry = tk.Entry(self.window,  width = 25, textvariable = self.aadhar_no)
		self.ageEntry = tk.Entry(self.window,  width = 25, textvariable = self.age)
		self.coming_fromEntry = tk.Entry(self.window,  width = 25, textvariable = self.coming_from)
		self.going_toEntry = tk.Entry(self.window,  width = 25, textvariable = self.going_to)
		self.street_nameEntry = tk.Entry(self.window,  width = 25, textvariable = self.street_name)
		self.areaEntry = tk.Entry(self.window,  width = 25, textvariable = self.area)
		self.cityEntry = tk.Entry(self.window,  width = 25, textvariable = self.city)
		self.pincodeEntry = tk.Entry(self.window,  width = 25, textvariable = self.pincode)
		self.stateEntry = tk.Entry(self.window,  width = 25, textvariable = self.state)
		self.countryEntry = tk.Entry(self.window,  width = 25, textvariable = self.country)
		self.phone_noEntry = tk.Entry(self.window,  width = 25, textvariable = self.phone_no)

		self.nameEntry.grid(pady = 5, column = 3, row = 1)
		self.aadhar_noEntry.grid(pady = 5, column = 3, row = 2)
		self.ageEntry.grid(pady = 5, column = 3, row = 3)
		self.coming_fromEntry.grid(pady = 5, column = 3, row = 4)
		self.going_toEntry.grid(pady = 5, column = 3, row = 5)
		self.street_nameEntry.grid(pady = 5, column = 3, row = 6)
		self.areaEntry.grid(pady = 5, column = 3, row = 7)
		self.cityEntry.grid(pady = 5, column = 3, row = 8)
		self.pincodeEntry.grid(pady = 5, column = 3, row = 9)
		self.stateEntry.grid(pady = 5, column = 3, row = 10)
		self.countryEntry.grid(pady = 5, column = 3, row = 11)
		self.phone_noEntry.grid(pady = 5, column = 3, row = 12)

		# Button widgets
		tk.Button(self.window, width = 20, text = "Insert", command = self.Insert).grid(pady = 15, padx = 5, column = 1, row = 14)
		tk.Button(self.window, width = 20, text = "Reset", command = self.Reset).grid(pady = 15, padx = 5, column = 2, row = 14)
		tk.Button(self.window, width = 20, text = "Close", command = self.window.destroy).grid(pady = 15, padx = 5, column = 3, row = 14)

		self.window.mainloop()

	def __del__(self):
		self.cur.close()
		self.mydb.close()

	def Insert(self):
		cmd = "INSERT INTO personal_details(name, aadhar_no, age, arrival_date, discharge_date, coming_from, going_to) " \
			  "VALUES (%s, %s, %s, %s, %s, %s, %s)"
		ins = (self.nameEntry.get(), self.aadhar_noEntry.get(), self.ageEntry.get(), self.arrival_date, self.discharge_date, self.coming_fromEntry.get(), self.going_toEntry.get())
		self.cur.execute(cmd, ins)

		cmd = "SELECT p_id FROM personal_details WHERE aadhar_no = %s"
		self.cur.execute(cmd, (self.aadhar_noEntry.get(), ))
		data = self.cur.fetchall()
		print(data)
		p_id = data[0][0]

		cmd = "INSERT INTO address(p_id, street_name, area, city, pincode, state, country) " \
			  "VALUES (%s, %s, %s, %s, %s, %s, %s)"
		ins = (p_id, self.street_nameEntry.get(), self.areaEntry.get(), self.cityEntry.get(), self.pincodeEntry.get(), self.stateEntry.get(), self.countryEntry.get())
		self.cur.execute(cmd, ins)

		phones = self.phone_noEntry.get().split(',')
		cmd = "INSERT INTO contact_details(p_id, phone) VALUES (%s, %s)"
		ins = [(p_id, p) for p in phones]
		self.cur.executemany(cmd, ins)

		self.mydb.commit()

		self.AssignRoom(p_id, self.ageEntry.get())

	def AssignRoom(self, p_id, age):
		global grd_flr_room, fir_flr_room, sec_flr_room
		root = tk.Tk()
		age = int(age)
		root.title('Assigned')

		cmd = "INSERT INTO hostel_details(p_id, hostel_no, floor_no, room_no)" \
			  "VALUES (%s, %s, %s, %s)"

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

		self.cur.execute(cmd, (p_id, hostel_no, floor_no, room_no))

		self.mydb.commit()

		if floor_no == 0:   floor = "Ground"
		elif floor_no == 1: floor = "First"
		else:               floor = "Second"
		tk.Label(root, width=50, text=f"Room Number : {room_no}").grid(pady=15, padx=2, column = 0, row = 0)
		tk.Label(root, width=50, text=f"Floor : {floor} Floor").grid(pady=10, padx=2, column = 0, row = 1)
		tk.Label(root, width=50, text=f"Hostel Number : {hostel_no}").grid(pady=10, padx=2, column = 0, row = 2)
		tk.Button(root, width = 20, text = "OK", command = root.destroy).grid(pady = 15, padx = 5, column = 0, row = 3)

		root.mainloop()

	def Reset(self):
		self.nameEntry.delete(0, tk.END)
		self.aadhar_noEntry.delete(0, tk.END)
		self.ageEntry.delete(0, tk.END)
		self.coming_fromEntry.delete(0, tk.END)
		self.going_toEntry.delete(0, tk.END)
		self.street_nameEntry.delete(0, tk.END)
		self.areaEntry.delete(0, tk.END)
		self.cityEntry.delete(0, tk.END)
		self.pincodeEntry.delete(0, tk.END)
		self.stateEntry.delete(0, tk.END)
		self.countryEntry.delete(0, tk.END)
		self.phone_noEntry.delete(0, tk.END)

class SearchWindow:
	def __init__(self):
		self.window = tk.Tk()
		self.window.title('Search')
		self.window.geometry('250x250')
		self.p_id = tk.IntVar()
		self.name = tk.StringVar()
		self.aadhar_no = tk.StringVar()

		tk.Label(self.window, text='Search data using these values').grid(pady=15, padx=30, columnspan=3, row=0)
		tk.Label(self.window, text="Patient ID ").grid(pady=10, padx=5, column=0, row = 1)
		tk.Label(self.window, text="Name ").grid(pady=10, padx=5, column=0, row = 2)
		tk.Label(self.window, text="Aadhar Number ").grid(pady=5, padx=5, column=0, row = 3)

		p_idEntry = tk.Entry(self.window, width = 20, textvariable=self.p_id)
		nameEntry = tk.Entry(self.window, width = 20, textvariable = self.name)
		aadhar_noEntry = tk.Entry(self.window, width = 20, textvariable = self.aadhar_no)

		p_idEntry.grid(column=1, row = 1)
		nameEntry.grid(column=1, row = 2)
		aadhar_noEntry.grid(column=1, row=3)

		def submitAction():
			p_id = p_idEntry.get()
			name = nameEntry.get()
			aadhar_no = aadhar_noEntry.get()

			cmd = "SELECT p.p_id, name, aadhar_no, age, arrival_date, discharge_date, coming_from, going_to, phone, street_name, area, city, pincode, state, country, hostel_no, floor_no, room_no " \
			    "FROM personal_details p, address a, hostel_details h, contact_details c " \
			    "WHERE a.p_id = p.p_id AND p.p_id = h.p_id AND p.p_id = c.p_id AND (p.p_id = %s OR name = %s OR aadhar_no = %s)"

			mydb = mysql.connector.connect(host='localhost', user='root', passwd='Mymysql1', database='dbms_project')
			cur = mydb.cursor()
			cur.execute(cmd, (p_id, name, aadhar_no, ))
			DatabaseView(cur)
			cur.close()
			mydb.close()

		submitButton = tk.Button(self.window, text='Search', width=28, command=submitAction)
		submitButton.grid(pady=20, padx=20, columnspan=3, row=4)

		self.window.mainloop()

class DeleteWindow:
	def __init__(self):
		self.window = tk.Tk()
		self.window.title('Delete')
		self.p_id = tk.IntVar()

		tk.Label(self.window, text="Patient ID ").grid(pady=10, padx=5, column=0, row = 0)
		p_idEntry = tk.Entry(self.window, width = 20, textvariable=self.p_id)

		p_idEntry.grid(column=1, row = 0)

		def submitAction():
			p_id = p_idEntry.get()
			cmd = "DELETE FROM personal_details WHERE p_id = %s"

			mydb = mysql.connector.connect(host='localhost', user='root', passwd='Mymysql1', database='dbms_project')
			cur = mydb.cursor()
			cur.execute(cmd, (p_id, ))

			mydb.commit()
			messagebox.showinfo('Result', "Delete Successful")

			cur.close()
			mydb.close()

		submitButton = tk.Button(self.window, text='Delete', width=28, command=submitAction)
		submitButton.grid(pady=20, padx=20, columnspan=2, row=1)

		self.window.mainloop()

class UpdateWindow:
	def __init__(self):
		window = tk.Tk()
		window.title('Update Data')
		self.mydb = mysql.connector.connect(host='localhost', user="root", password="Mymysql1", database='dbms_project')
		self.cur = self.mydb.cursor()
		self.p_id = tk.IntVar()

		tk.Label(window, text='Enter Patient ID to Update his/her information').grid(padx=5, pady=15, columnspan=2, row=0)
		tk.Label(window, text='Patient ID').grid(pady=5, padx=5, column=0, row=1)
		self.p_idEntry = tk.Entry(window, width=15, textvariable=self.p_id)
		self.p_idEntry.grid(column=1, row=1)

		submitButton = tk.Button(window, text='Enter Details', width=15, command=self.submitAction)
		submitButton.grid(columnspan=2, row=2, padx=5, pady=20)

		window.mainloop()

	def __del__(self):
		self.cur.close()
		self.mydb.close()

	def submitAction(self):

		self.cur.execute("SELECT COUNT(p_id) FROM personal_details WHERE p_id = %s", (self.p_idEntry.get(),))
		data = self.cur.fetchall()
		if data[0][0] == 0:
			messagebox.showerror('Not Found', 'There is no information in the database')
			return

		window = tk.Tk()
		window.wm_title("Update data")

		cmd = "SELECT name, aadhar_no, age, coming_from, going_to, street_name, area, city, pincode, state, country, phone " \
			  "FROM personal_details p, address a, hostel_details h, contact_details c " \
			  "WHERE a.p_id = p.p_id AND p.p_id = h.p_id AND p.p_id = c.p_id AND p.p_id = %s"

		self.cur.execute(cmd, (self.p_idEntry.get(),))
		data = self.cur.fetchone()
		self.cur.fetchall()

		# Initializing all the variables
		name = tk.StringVar(window, value=data[0])
		aadhar_no = tk.StringVar(window, value=data[1])
		age = tk.IntVar(window, value=data[2])
		coming_from = tk.StringVar(window, value=data[3])
		going_to = tk.StringVar(window, value=data[4])
		street_name = tk.StringVar(window, value=data[5])
		area = tk.StringVar(window, value=data[6])
		city = tk.StringVar(window, value=data[7])
		pincode = tk.IntVar(window, value=data[8])
		state = tk.StringVar(window, value=data[9])
		country = tk.StringVar(window, value=data[10])
		phone_no = tk.StringVar(window, value=data[11])

		# Labels
		tk.Label(window, text="Name", width=25).grid(pady=5, column=1, row=1)
		tk.Label(window, text="Aadhar Number", width=25).grid(pady=5, column=1, row=2)
		tk.Label(window, text="Age", width=25).grid(pady=5, column=1, row=3)
		tk.Label(window, text="Coming From", width=25).grid(pady=5, column=1, row=4)
		tk.Label(window, text="Going to", width=25).grid(pady=5, column=1, row=5)
		tk.Label(window, text="Street Name", width=25).grid(pady=5, column=1, row=6)
		tk.Label(window, text="Area", width=25).grid(pady=5, column=1, row=7)
		tk.Label(window, text="City", width=25).grid(pady=5, column=1, row=8)
		tk.Label(window, text="Pincode", width=25).grid(pady=5, column=1, row=9)
		tk.Label(window, text="State", width=25).grid(pady=5, column=1, row=10)
		tk.Label(window, text="Country", width=25).grid(pady=5, column=1, row=11)
		tk.Label(window, text="Phone number(s)", width=25).grid(pady=5, column=1, row=12)

		# Fields
		# Entry widgets
		nameEntry = tk.Entry(window, width=25, textvariable=name)
		aadhar_noEntry = tk.Entry(window, width=25, textvariable=aadhar_no)
		ageEntry = tk.Entry(window, width=25, textvariable=age)
		coming_fromEntry = tk.Entry(window, width=25, textvariable=coming_from)
		going_toEntry = tk.Entry(window, width=25, textvariable=going_to)
		street_nameEntry = tk.Entry(window, width=25, textvariable=street_name)
		areaEntry = tk.Entry(window, width=25, textvariable=area)
		cityEntry = tk.Entry(window, width=25, textvariable=city)
		pincodeEntry = tk.Entry(window, width=25, textvariable=pincode)
		stateEntry = tk.Entry(window, width=25, textvariable=state)
		countryEntry = tk.Entry(window, width=25, textvariable=country)
		phone_noEntry = tk.Entry(window, width=25, textvariable=phone_no)

		nameEntry.grid(pady=5, column=3, row=1)
		aadhar_noEntry.grid(pady=5, column=3, row=2)
		ageEntry.grid(pady=5, column=3, row=3)
		coming_fromEntry.grid(pady=5, column=3, row=4)
		going_toEntry.grid(pady=5, column=3, row=5)
		street_nameEntry.grid(pady=5, column=3, row=6)
		areaEntry.grid(pady=5, column=3, row=7)
		cityEntry.grid(pady=5, column=3, row=8)
		pincodeEntry.grid(pady=5, column=3, row=9)
		stateEntry.grid(pady=5, column=3, row=10)
		countryEntry.grid(pady=5, column=3, row=11)
		phone_noEntry.grid(pady=5, column=3, row=12)

		# Button widgets

		def Update():
			cmd = "UPDATE personal_details SET name = %s, aadhar_no = %s, age = %s, coming_from = %s, going_to = %s " \
				  "WHERE p_id = %s"
			ins = (nameEntry.get(), aadhar_noEntry.get(), ageEntry.get(), coming_fromEntry.get(), going_toEntry.get(), self.p_idEntry.get(), )
			self.cur.execute(cmd, ins)

			p_id = self.p_idEntry.get()

			cmd = "UPDATE address SET street_name = %s, area = %s, city = %s, pincode = %s, state = %s, country = %s " \
				  "WHERE p_id = %s"
			ins = (street_nameEntry.get(), areaEntry.get(), cityEntry.get(), pincodeEntry.get(), stateEntry.get(), countryEntry.get(), p_id, )
			self.cur.execute(cmd, ins)

			phones = phone_noEntry.get()
			cmd = "UPDATE contact_details SET phone = %s WHERE p_id = %s AND phone = %s"
			ins = (phone_noEntry.get(), p_id, data[11], )
			self.cur.execute(cmd, ins)
			messagebox.showinfo('Result', 'Update Successful')

			self.mydb.commit()

			window.destroy()

		def Reset():
			nameEntry.delete(0, tk.END)
			aadhar_noEntry.delete(0, tk.END)
			ageEntry.delete(0, tk.END)
			coming_fromEntry.delete(0, tk.END)
			going_toEntry.delete(0, tk.END)
			street_nameEntry.delete(0, tk.END)
			areaEntry.delete(0, tk.END)
			cityEntry.delete(0, tk.END)
			pincodeEntry.delete(0, tk.END)
			stateEntry.delete(0, tk.END)
			countryEntry.delete(0, tk.END)
			phone_noEntry.delete(0, tk.END)

		tk.Button(window, width=20, text="Update", command=Update).grid(pady=15, padx=5, column=1, row=14)
		tk.Button(window, width=20, text="Reset", command=Reset).grid(pady=15, padx=5, column=2, row=14)
		tk.Button(window, width=20, text="Close", command=window.destroy).grid(pady=15, padx=5, column=3, row=14)

		window.mainloop()

class HomePage:
	def __init__(self):
		# self.homePageWindow = tk.Tk()
		# self.homePageWindow.wm_title("NIT Silchar Quarantine System")
		#
		# tk.Label(self.homePageWindow, text="Home Page", width=100).grid(pady=20, column=1, row=1)
		#
		# tk.Button(self.homePageWindow, width=20, text="Insert", command=self.Insert).grid(pady=15, column=1, row=2)
		# tk.Button(self.homePageWindow, width=20, text="Update", command=self.Update).grid(pady=15, column=1, row=3)
		# tk.Button(self.homePageWindow, width=20, text="Search", command=self.Search).grid(pady=15, column=1, row=4)
		# tk.Button(self.homePageWindow, width=20, text="Delete", command=self.Delete).grid(pady=15, column=1, row=5)
		# tk.Button(self.homePageWindow, width=20, text="Display", command=self.Display).grid(pady=15, column=1, row=6)
		# tk.Button(self.homePageWindow, width=20, text="Exit", command=self.homePageWindow.destroy).grid(pady=15, column=1, row=7)
		#
		# self.homePageWindow.mainloop()
		root = tk.Tk()
		root.title('Database')

		# canvas and frame
		canvas = tk.Canvas(root, height=400, width=700, bg='#263D42')
		canvas.pack()
		frame = tk.Frame(canvas, bg="white")
		frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

		# Home image
		image = Image.open('DBMS_logo.png')
		resized = image.resize((300, 225), Image.ANTIALIAS)
		wall = ImageTk.PhotoImage(resized)

		# // styles for buttons
		style = ttk.Style()
		style.map("C.TButton",
				  foreground=[('pressed', 'red'), ('active', 'blue')],
				  background=[('pressed', '!disabled', 'black'), ('active', 'white')]
				  )

		# Labels-----------
		wall_box = tk.Label(frame, image=wall, bd='0')
		btn_box = tk.LabelFrame(frame, text='Choose the Operation',
								fg='#213B42', bd='0', font='Helvetica 13')


		# buttons
		insert_btn = ttk.Button(btn_box, text='Insert', style='C.TButton', command=self.Insert)
		update_btn = ttk.Button(btn_box, text='Update', style='C.TButton', command=self.Update)
		search_btn = ttk.Button(btn_box, text='Search', style='C.TButton', command=self.Search)
		delete_btn = ttk.Button(btn_box, text='Delete', style='C.TButton', command=self.Delete)
		display_btn = ttk.Button(btn_box, text='Display', style='C.TButton', command=self.Display)
		exit_btn = ttk.Button(btn_box, text='Exit', style='C.TButton', command=root.destroy)

		# //layouts-----------------
		wall_box.pack(side=(tk.LEFT), fill=tk.X, padx=10)
		btn_box.pack(side=(tk.RIGHT), fill=tk.X, padx=15, ipadx=10)

		insert_btn.pack(padx=10, pady=10, ipadx=10)
		update_btn.pack(padx=10, pady=10, ipadx=10)
		search_btn.pack(padx=10, pady=10, ipadx=10)
		delete_btn.pack(padx=10, pady=10, ipadx=10)
		display_btn.pack(padx=10, pady=10, ipadx=10)
		exit_btn.pack(padx=10, pady=10, ipadx=10)

		root.mainloop()

	def Insert(self):
		insert = InsertWindow()

	def Update(self):
		update = UpdateWindow()

	def Search(self):
		search = SearchWindow()

	def Delete(self):
		delete = DeleteWindow()

	def Display(self):
		mydb = mysql.connector.connect(host='localhost', user='root', passwd='Mymysql1', database='dbms_project')
		cur = mydb.cursor()
		cmd = "SELECT p.p_id, name, aadhar_no, age, arrival_date, discharge_date, coming_from, going_to, phone, street_name, area, city, pincode, state, country, hostel_no, floor_no, room_no " \
			  "FROM personal_details p, address a, hostel_details h, contact_details c " \
			  "WHERE a.p_id = p.p_id AND p.p_id = h.p_id AND p.p_id = c.p_id"
		cur.execute(cmd)
		data = cur.fetchall()
		# for x in data:
		# 	print(x)
		DatabaseView(data)
		cur.close()
		mydb.close()

homepage = HomePage()
