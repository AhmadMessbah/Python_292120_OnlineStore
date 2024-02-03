import mysql.connector

from model.entity import user


class UserController:
    def connect(self):
        self.connection = mysql.connector.connect(user='root', password='root123', database='mft')
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.connection.close()
        self.cursor.close()


    def save(self,  name, family, username, password, role, status=True):
        self.connect()
        self.cursor.execute(operation:"INSERT INTO User_tbl (name, family, username, password, role, status) values (%s, %s, %s, %s, %s)",
                            params[user.name , user.family , user.username , user.password , user.role , user.status])
        self.connection.commit()
        self.disconnect()


    def edit(self,  id, name, family, username, password, role, status):
        self.connect()
        self.cursor.execute(operation:"UPDATE User_tbl set name = %s, family = %s, username = %s, password = %s , role = %s, status = %s where id = %s",
        params:[user.name , user.family , user.username, user.password , user.role , user.id])
        self.disconnect()


    def remove(self, id):
        self.connect()
        self.cursor.execute(operation :"DELETE FROM User_tbl where id = %s" ,
        params :[user.id])


    def find_all(self):
        self.connect()
        self.cursor.execute("select * from Users")
        user = self.cursor.fetchall()
        self.disconnect()
        return user

    def find_by_username(self, username):
        self.connect()
        self.cursor.execute(operation:"SELECT * from user_tbl where username = %s", params:[username])
        user = self.cursor.fetchone()
        self.disconnect()
        return user


    def find_by_username_and_password(self, username, password):
        self.connect():
        self.cursor.execute(operation:"SELECT * from user_tbl where username = %s AND PASSWORD =%s",
        params:[user.username , user.password])
        user = self.cursor.fetchone()
        self.disconnect()
        return user
