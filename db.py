import sqlite3

def create_table():
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()
    try:
        cursor.execute('CREATE TABLE IF NOT EXISTS user_s (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)')
        print("Tablo başarıyla oluşturuldu.")
    except Exception as e:
        print(f"Hataaa !!{str(e)}")
    connection.commit()
    connection.close()

def register_user(username, password):
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()
    try:
        cursor.execute('INSERT INTO user_s (username, password) VALUES (?, ?)', (username, password))
        connection.commit()
        user_id = cursor.lastrowid
        print(f"Kullanıcı başarıyla kaydedildi. ID: {user_id}")
    except Exception as e:
        print(f"Hata !!: {str(e)}")
    connection.close()

def show():
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM user_s')
    rows = cursor.fetchall()
    for row in rows:
        print("----------------")
        print(row)
        print("----------------")
    connection.close()

def update(id_value, username):
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()
    try:
        cursor.execute('UPDATE user_s SET username = ? WHERE id = ?', (username, id_value))
        print("Başarıyla güncellendi.")
        connection.commit()
    except Exception as e:
        print(f"Hata !!: {str(e)}")
    connection.close()

def delete(id_value):
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()
    try:
        cursor.execute('DELETE FROM user_s WHERE id = ?', (id_value,))
        connection.commit()
    except Exception as e:
        print(f"Hata !!: {str(e)}")
    connection.close()

def main():
    create_table()
    print("Ekleme: 1, Silme: 2, Güncelleme: 3, Verileri Görmek için: 4")
    value = int(input("Yapacağınız işlemi seçiniz: "))
    
    if value == 1:
        username = input('Kullanıcı adı: ')
        password = input('Şifre: ')
        register_user(username, password)
        show()
    
    elif value == 2:
        show()
        id_value = input('Silinecek ID: ')
        delete(id_value)
        show()
    
    elif value == 3:
        id_value = input('Güncellenecek ID: ')
        username = input("Yeni kullanıcı adı: ")
        update(id_value, username)
        show()
    
    elif value == 4:
        show()

run = True
while run:
    if __name__ == '__main__':
        main()
