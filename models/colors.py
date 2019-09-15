import MySQLdb
import db


def get_all():
    try:
        cursor = db.cursor()
        cursor.execute("SELECT color_id,name,hex FROM colors")
        result = cursor.fetchall()
        cursor.close()
        return result
    except MySQLdb.Error as err:
        print(err)
        return None


def add(name, hex):
    try:
        cursor = db.cursor()
        params = (name, hex)
        cursor.execute("INSERT INTO colors (created_at,name,hex) VALUES (NOW(), %s, %s)", params)
        last_row_id = cursor.lastrowid
        cursor.close()
        db.commit()
        return last_row_id
    except MySQLdb.Error as err:
        print(err)
        return None


def update(color_id, name, hex):
    try:
        cursor = db.cursor()
        params = (name, hex, color_id)
        cursor.execute("UPDATE colors SET name=%s, hex=%s WHERE color_id=%s", params)
        cursor.close()
        db.commit()
        return 1
    except MySQLdb.Error as err:
        print(err)
        return None


def delete(color_id):
    try:
        cursor = db.cursor()
        cursor.execute("DELETE FROM colors WHERE color_id=%s", [color_id])
        cursor.close()
        db.commit()
    except MySQLdb.Error as err:
        print(err)
        return None


def search(query):
    try:
        cursor = db.cursor()
        cursor.execute("SELECT color_id,name,hex FROM colors WHERE name LIKE %s", ['%' + query + '%'])
        result = cursor.fetchall()
        cursor.close()
        return result
    except MySQLdb.Error as err:
        print(err)
        return None
