import mysql.connector
import MySQLdb.cursors
import config as cfg

class LoginDAO:
    db=""
    app.secret_key = 'initialSecretKey'
    def __init__(self): 
        self.db = mysql.connector.connect(
        host=cfg.mysql['host'],
        user=cfg.mysql['user'],
        password=cfg.mysql['password'],
        database=cfg.mysql['database']
        )

    def findLogin(self, Username, Password):
        cursor = self.db.cursor()
        sql="select * from users where Username = %s AND Password = %s"
        values = (Username, Password)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

loginDAO = LoginDAO()