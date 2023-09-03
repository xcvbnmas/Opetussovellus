from db import db
from sqlalchemy.sql import text

def get_list():
    sql = text("SELECT id, content FROM announcements WHERE visible=1 ORDER BY id")
    result = db.session.execute(sql)
    return result.fetchall()

def add_announcement(content):
    sql = text("""INSERT INTO announcements (content, visible)
             VALUES (:content, 1) RETURNING id""")
    announcement_id = db.session.execute(sql, {"content":content}).fetchone()[0]
    
    db.session.commit()
    return announcement_id
    
def remove_announcement(announcement_id):
    sql = text("UPDATE announcements SET visible=0 WHERE id=:id")
    db.session.execute(sql, {"id":announcement_id})
    db.session.commit()
