import sqlite3
from getpass import getpass
from functions import option
db = sqlite3.connect("Login")
cursor = db.cursor()
def register():
	try:
		username = input("Input username: ")
		password = getpass("Create a password: ")
		password_confirm = getpass("Confirm password: ")
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
	username = input("Introduce the root's username: ")
	password = getpass("Introduce the root's password: ")
	cursor.execute("SELECT * FROM LOGIN WHERE ROOT = 'YES'")
	list = cursor.fetchall()
	if username in list[0] and password in list[0]:
		print("Access Granted!")
		return True
	else:
		print("Acces Denied :(")
		return False

def root():
	username = input("Enter the root's username: ")
	password = getpass("Enter the root's password: ")
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
password = getpass("Enter password: ")
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