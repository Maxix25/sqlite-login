import sqlite3
from getpass import getpass
from functions import option
db = sqlite3.connect("Login")
cursor = db.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS LOGIN (USERNAME VARCHAR(10) UNIQUE, PASSWORD VARCHAR(10), USERNUMBER INTEGER PRIMARY KEY AUTOINCREMENT)")
def register():
	try:
		username = input("Input username: ")
		password = getpass("Create a password: ")
		password_confirm = getpass("Confirm password: ")
		if password == password_confirm:
			cursor.execute("INSERT INTO LOGIN VALUES (?, ?, NULL)", (username, password))
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
	password = getpass("Password: ")
	username_list = cursor.execute("SELECT * FROM LOGIN WHERE USERNAME=(?) AND PASSWORD=(?)", (username, password))
	usernames = cursor.fetchall()
	if len(usernames) <= 0:
		print("Username or password incorrect!")
		choice = input("Try again? [Y/n]")
		if choice.lower() == "y" or choice == "":
			login()
		elif choice.lower() == "n":
			return
def query():
	username = "Maxi"
	cursor.execute("SELECT USERNAME FROM LOGIN")
	usernames = cursor.fetchall()
	for username in usernames:
		print(username)
"""
username = input("Enter username: ")
password = getpass("Enter password: ")
cursor.execute("INSERT INTO LOGIN VALUES(?, ?, NULL)", (username, password))
"""
print(
	"What do you want to do\n",
	"[1] Register\n",
	"[2] Login"
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