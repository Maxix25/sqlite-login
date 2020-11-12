import sqlite3
from functions import option
db = sqlite3.connect("Login")
cursor = db.cursor()
def register():
	try:
		username = input("Input username: ")
		password = input("Create a password: ")
		password_confirm = input("Confirm password: ")
		if password == password_confirm:
			cursor.execute("INSERT INTO LOGIN VALUES (?, ?, NULL, 'NO')", (username, password))
			print("Username created correctly!")
		else:
			choice = input("Passwords didn't match, try again? [Y/n]")
			if choice.lower() == "y" or choice == "":
				register()
			else:
				return None
	except sqlite3.IntegrityError:
		while True:
			choice = input("Username already exists, want to try again? [Y/n]")
			if choice.lower() == "y" or choice == "":
				register()
				break
			elif choice.lower() == "n":
				break
			else:
				print("Non-valid character")

def login():
	username = input("Username: ")
	password = input("Password: ")
	db.set_trace_callback(print)
	cursor.execute('SELECT * FROM LOGIN WHERE USERNAME ="' + username + '" AND PASSWORD ="' + password + '"')
	list = cursor.fetchall()
	print(list)
	if len(list) <= 0:
		print("Username or password incorrect!")
		choice = input("Try again? [Y/n]")
		if choice.lower() == "y" or choice == "":
			login()
		elif choice.lower() == "n":
			return
	else:
		print("Access Granted! :)")
def query():
	username = input("Introduce the root's username: ")
	password = input("Introduce the root's password: ")
	cursor.execute("SELECT * FROM LOGIN WHERE ROOT = 'YES'")
	list = cursor.fetchall()
	if username in list[0] and password in list[0]:
		print("Access Granted!")
	else:
		print("Acces Denied :(")
		return False
	print(
		"Select what do you want to see\n",
		"[1] Usernames\n",
		"[2] Passwords\n",
		"[3] IsRoot\n",
		"[4] All"
		)
	choice = option(4)
	if choice == 1:
		cursor.execute("SELECT USERNAME FROM LOGIN")
	elif choice == 2:
		cursor.execute("SELECT USERNAME, PASSWORD FROM LOGIN")
		print("USERNAME PASSWORD")
	elif choice == 3:
		cursor.execute("SELECT USERNAME, ROOT FROM LOGIN")
		print("USERNAME ISROOT")
	elif choice == 4:
		cursor.execute("SELECT * FROM LOGIN")
	list = cursor.fetchall()
	for object in list:
		print(object)
	
	
def root():
	username = input("Enter the root's username: ")
	password = input("Enter the root's password: ")
	cursor.execute("INSERT INTO LOGIN VALUES(?, ?, NULL, 'YES')", (username, password))
	print("Root user created succesfully!")

cursor.execute("CREATE TABLE IF NOT EXISTS LOGIN (USERNAME VARCHAR(10) UNIQUE, PASSWORD VARCHAR(10), USERNUMBER INTEGER PRIMARY KEY AUTOINCREMENT, ROOT VARCHAR(4))")
cursor.execute("SELECT * FROM LOGIN")
list = cursor.fetchall()

if len(list) == 0:
	choice = input("Welcome to the sqlite login management!, i see that you haven't created any users, would you like to add a root user?, [Y/n]")
	if choice.lower() == "y" or choice == "":
		root()
	elif choice.lower() == "n":
		pass
	else:
		print("Non-valid character introduced")


"""
username = input("Enter username: ")
password = input("Enter password: ")
cursor.execute("INSERT INTO LOGIN VALUES(?, ?, NULL)", (username, password))
"""
print(
	"What do you want to do\n",
	"[1] Register\n",
	"[2] Login\n",
	"[3] Query (In Progress)"
	)
choice = option(3)
if choice == 1:
	register()
elif choice == 2:
	login()

elif choice == 3:
	query()

db.commit()
db.close()