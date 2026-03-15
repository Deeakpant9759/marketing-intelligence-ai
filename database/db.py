import mysql.connector
def get_connection():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password='Deepakpant@001',
        database="Commerce_inelligence"
    )