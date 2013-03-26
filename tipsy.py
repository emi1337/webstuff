from flask import Flask, render_template, request, redirect, url_for
import model

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html", user_name="chriszf")
"""
@app.route("/login")
def login():
	pass

@app.route("/user/<username>")
def profile(username):
	pass

with app.test_request_context():
	print url_for('index')
	print url_for('login')
	print url_for('long', next='/')
	print url_for('profile', username="John Doe")
"""
@app.route("/tasks")
def list_tasks():
	db = model.connect_db()
	tasks_from_db = model.get_tasks(db, None)
	return render_template("list_tasks.html", tasks = tasks_from_db)

@app.route("/save_task", methods = ["POST"])
def save_task():
	task_title = request.form["task_title"]
	db = model.connect_db()
	#Assumer that all tasks are attached to user 1.
	task_id = model.new_task(db, task_title, 1)
	return redirect("/tasks")

@app.route("/edit_task", methods = ["POST"])
def edit_task():
	new_title = request.form["new_title"]
	task_id = 1 # Pull from the URL?
	db = model.connect_db()
	task_id = model.edit_task_title(db, new_title, task_id)
	return redirect("/tasks")

@app.route("/save_task", methods = ["POST"])
def edit_task():
	task_title = request.form["task_title"]
	db = model.connect_db()
	#Assumer that all tasks are attached to user 1.
	task_id = model.new_task(db, task_title, 1)
	return redirect("/tasks")

"""@app.route("/save_task", methods = ["POST"])
def save_complete():
	task_title = request.form["task_title"]
	db = model.connect_db()
	#Assumer that all tasks are attached to user 1.
	task_id = model.new_task(db, task_title, 1)
	return redirect("/tasks")
"""

@app.route("/new_task")
def add_task():
	db = model.connect_db()
	#new_task = model.new_task(db, title, user_id)
	return render_template("new_task.html")#, tasks = new_task)

if __name__ == '__main__':
	app.run(debug=True)