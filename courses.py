from db import db
from sqlalchemy.sql import text
from sqlalchemy.sql import text

def get_courses():
    sql = text("SELECT id, name FROM courses WHERE visible=1 ORDER BY name")
    return db.session.execute(sql).fetchall()
    
def get_course(course_id):
    sql = text("""SELECT d.name, u.name FROM courses d, users u
             WHERE d.id=:course_id AND d.creator_id=u.id""")
    return db.session.execute(sql, {"course_id": course_id}).fetchone()
    
def add_course(name, visible, creator_id):
    sql = text("""INSERT INTO courses (creator_id, name, visible)
             VALUES (:creator_id, :name, 1) RETURNING id""")
    course_id = db.session.execute(sql, {"creator_id":creator_id, "name":name}).fetchone()[0]
    
    db.session.commit()
    return course_id
    
def remove_course(course_id, user_id):
    sql = text("UPDATE courses SET visible=0 WHERE id=:id AND creator_id=:user_id")
    db.session.execute(sql, {"id":course_id, "user_id":user_id})
    db.session.commit()
