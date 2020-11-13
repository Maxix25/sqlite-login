import sqlite3
from flask import Flask, request, render_template
app = Flask(__name__)
db = sqlite3.connect("Login", check_same_thread = False)
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS LOGIN (USERNAME VARCHAR(10), PASSWORD VARCHAR(10), ROOT BOOLEAN)")

@app.route("/register", methods = ["POST", "GET"])

def register():

	if request.method == "POST":

		username = request.form["username"]
		password = request.form["password"]
		password_confirm = request.form["password_confirm"]
		if password == password_confirm:
			cursor.execute("INSERT INTO LOGIN VALUES (?, ?, False)", (username, password))
			db.commit()
			return render_template("register_success.html")
		else:

			return render_template("error.html")
	else:
		return render_template("register.html")









if __name__ == '__main__':
	app.run(debug = True)
db.exit()