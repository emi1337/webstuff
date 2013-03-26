import sqlite3
import datetime, time

def connect_db():
	return sqlite3.connect("task.db")

def new_user(db, email, password, name):
	c = db.cursor()
	query = """INSERT INTO Users VALUES (NULL, ?, ?, ?)"""
	result = c.execute(query, (email, password, name))
	db.commit()
	print "You added a new user, %s" % name
	return result.lastrowid

def authenticate(db, email, password):
	c = db.cursor()
	query = """SELECT * FROM Users WHERE email=? AND password=?"""
	c.execute(query, (email, password))
	result = c.fetchone()
	if result:
		fields = ["id", "email", "password", "username"]
		print "You've been authorized!"
		return dict(zip(fields, result))
	else:
		return None

def new_task(db, title, user_id):
	c = db.cursor()
	now = datetime.datetime.now()
	query = """INSERT INTO Tasks VALUES (NULL, ?, ?, NULL, ?)"""
	result = c.execute(query, (title, now, user_id))
	# "details about the task", 
	db.commit()
	return result.lastrowid

def get_user(db, user_id):
	c = db.cursor()
	query = """SELECT * FROM Users WHERE id = ?"""
	c.execute(query, (user_id,))
	result = c.fetchone()
	if result:
		fields = ["id", "email", "password", "username"]
		return dict(zip(fields, result))
	else:
		return None

def complete_task(db, task_id):
	now = datetime.datetime.now()
	c = db.cursor()
	query = """UPDATE tasks SET completed_at=? WHERE id=?"""
	c.execute(query, (now, task_id,))
	db.commit()

def change_task_title(db, new_title, task_id):
	now = datetime.datetime.now()
	c = db.cursor()
	query = """UPDATE tasks SET title=? WHERE id=?"""
	c.execute(query, (now, new_title, task_id))
	db.commit()

def make_dictionary_from_task(task,fields):
	i = 0
	new_dict = {}
	for item in task:
		new_dict[fields[i]]=task[i]
		i += 1
	return new_dict

def get_tasks(db, user_id):
    c = db.cursor()
    if user_id:
        query = """SELECT * from Tasks WHERE user_id = ?"""
        c.execute(query, (user_id,))
    else:
        query = """SELECT * from Tasks"""
        c.execute(query)
    tasks = []
    rows = c.fetchall()
    for row in rows:
        task = dict(zip(["id", "title", "created_at", "completed_at", "user_id"], row))
        tasks.append(task)

    return tasks

def get_task(db, task_id):
	c = db.cursor()
	query = """SELECT * FROM Tasks WHERE id=?"""
	c.execute(query, (task_id,))
	result = c.fetchone()
	if result:
		fields = ["id", "title", "created_at", "completed_at", "user_id"]
		return dict(zip(fields, result))
	else:
		return None

def main():
	connect_db()


if __name__ == '__main__':
	main()