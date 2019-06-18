
import cx_Oracle
def create_connection():
    return cx_Oracle.Connection('T751425/T751425@10.123.79.57/georli02')

def create_cursor(con):
    return cx_Oracle.Cursor(con)