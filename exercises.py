from db import db
from sqlalchemy.sql import text
from sqlalchemy.sql import text

def get_exercises():
    sql = text("SELECT id, name FROM exercises WHERE visible=1 ORDER BY name")
    return db.session.execute(sql).fetchall()
    
def get_exercise(exercise_id):
    sql = text("""SELECT e.name, e.instructions, e.model_answer FROM exercises e
             WHERE e.id=:exercise_id""")
    return db.session.execute(sql, {"exercise_id": exercise_id}).fetchone()
    
def add_exercise(name, instructions, model_answer):
    sql = text("""INSERT INTO exercises (name, instructions, model_answer, visible)
             VALUES (:name, :instructions, :model_answer, 1) RETURNING id""")
    exercise_id = db.session.execute(sql, {"name":name, "instructions":instructions, "model_answer": model_answer}).fetchone()[0]
    
    db.session.commit()
    return exercise_id
    
def remove_exercise(exercise_id, user_id):
    sql = text("UPDATE exercises SET visible=0 WHERE id=:id")
    db.session.execute(sql, {"id":exercise_id})
    db.session.commit()
    
def submit_answer(exercise_id, answer, user_id):
    sql = text("""INSERT INTO answers (exercise_id, user_id, answer)
             VALUES (:exercise_id, :user_id, :answer)""")
    db.session.execute(sql, {"exercise_id": exercise_id, "user_id": user_id, "answer": answer})
    db.session.commit()
    
def get_answer(exercise_id, user_id):
    sql = text("""SELECT answer FROM answers WHERE exercise_id = :exercise_id AND user_id = :user_id""")
    result = db.session.execute(sql, {"exercise_id": exercise_id, "user_id": user_id,})
    return result.fetchone()
