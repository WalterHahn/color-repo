import config
import MySQLdb.cursors
from flask import g

def get():
    try:
        if not hasattr(g, 'mysql_connection'):
            g.mysql_connection = MySQLdb.Connection(
                host=config.db['host'],
                user=config.db['user'],
                passwd=config.db['password'],
                port=config.db['port'],
                db=config.db['database'],
                cursorclass=MySQLdb.cursors.DictCursor
            )
        return g.mysql_connection
    except MySQLdb.Error as err:
        print(err)
        return None


def cursor():
    conn = get()
    return conn.cursor()


def commit():
    conn = get()
    conn.commit()
