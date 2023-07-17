import sqlite3
import cgi
import os
import cgitb
cgitb.enable()



def login (username,password):
    connection = sqlite3.connect('database.sqlite')
    cursor=connection.cursor()
    check = cursor.execute("SELECT username FROM kul WHERE username = ? AND Password = ?;", (username, password))
    connection.commit()
    if  cursor.fetchone():
        print("Giriş başarılı")
    else:
        print("Giriş başarısız.")    
    connection.close()
run = True
while run:
    username = input("Kullanıcı adınızı giriniz:")
    password = input("Şifrenizi giriniz:")
    login(username,password)
    