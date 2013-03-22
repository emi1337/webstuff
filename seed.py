import model

db = model.connect_db()
user_id = model.new_user(db, "chriszf@gmail.com", "password", "Christian")
task = model.new_task(db, "Complete this task list", user_id)
user_id = model.new_user(db, "elmo@gmail.com", "password", "Elmo")
task = model.new_task(db, "Hugs", user_id)
user_id = model.new_user(db, "cmonster@gmail.com", "password", "CMonster")
task = model.new_task(db, "Eat Cookies.", user_id)
user_id = model.new_user(db, "kermit@gmail.com", "password", "Kermit")
task = model.new_task(db, "Ribbit", user_id)
user_id = model.new_user(db, "thecount@gmail.com", "password", "The Count")
task = model.new_task(db, "1, 2, 3", user_id)
task = model.new_task(db, "4, 5, 6", user_id)