import sqlite3
def create_table(table_name): #tablo oluşturur
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()
    try:
        cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)')
        print("Tablo başarıyla oluşturuldu.")
    except Exception as e:
        print(f"Hataaa !!{str(e)}")
    connection.commit()
    connection.close()

def register_user(table_name,username, password): #kullanıcı kaydeder 
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()
    try:
        cursor.execute(f'INSERT INTO {table_name} (username, password) VALUES (?, ?)', (username, password))
        connection.commit()
        user_id = cursor.lastrowid
        print(f"Kullanıcı başarıyla kaydedildi. ID: {user_id}")
    except Exception as e:
        print(f"Hata !!: {str(e)}")
    connection.close()

def table_show(): #tüm tabloları gösterir
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    connection.close()

def show(table_name): #belli bir tabloyu gösterir
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM {table_name}')
    rows = cursor.fetchall()
    for row in rows:
        print("----------------")
        print(row)
        print("----------------")
    connection.close()

def update(table_name,id_value): #veriyi günceller.
    print("""
        Sadece Kullanıcı Adını Güncelleyeceksiniz : 1
        Sadece Şifre Güncelleyeceksiniz : 2
        Kullanıcı adı ve şifre güncelleyeceksiniz : 3
""")
    tercih = int(input("Girmek istediğiniz parametreyi giriniz:"))
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()
    if tercih == 1:
      username = input("Yeni kullanıcı adı: ")
      try:
        cursor.execute(f'UPDATE {table_name} SET username = ? WHERE id = ?', (username, id_value))
        print("Başarıyla güncellendi.")
        connection.commit()
      except Exception as e:
        print(f"Hata !!: {str(e)}")
    elif tercih ==2 :
      password = input("Yeni şifrenizi giriniz:")
      try:
        cursor.execute(f'UPDATE {table_name} SET password = ? WHERE id = ?', (password, id_value))
        print("Başarıyla güncellendi.")
        connection.commit()
      except Exception as e:
        print(f"Hata !!: {str(e)}")
    elif tercih ==3 :
      username = input("Yeni kullanıcı adı: ")
      password = input("Yeni şifrenizi giriniz:")
      try:
        cursor.execute(f'UPDATE {table_name} SET username = ? , password = ? WHERE id = ?', (username,password, id_value))
        print("Başarıyla güncellendi.")
        connection.commit()
      except Exception as e:
        print(f"Hata !!: {str(e)}")
    connection.close()

def delete(id_value,table_name): #veriyi siler
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()
    try:
        cursor.execute(f'DELETE FROM {table_name} WHERE id = ?', (id_value,))
        connection.commit()
    except Exception as e:
        print(f"Hata !!: {str(e)}")
    connection.close()

def main(): #her şey  bu kısımda başlar.
    print("Ekleme: 1, Silme: 2, Güncelleme: 3, Verileri Görmek için: 4,Tablo Oluşturmak İçin 5")
    value = int(input("Yapacağınız işlemi seçiniz: "))

    if value == 1:
        table_show()
        table_name= input("Tablo adını giriniz:")
        username = input('Kullanıcı adı: ')
        password = input('Şifre: ')
        register_user(table_name,username, password)
        show()
    
    elif value == 2:
        table_show()
        table_name = input("Tablo adını giriniz:")
        show(table_name)
        id_value = input('Silinecek ID: ')
        delete(id_value,table_name)
        print("Başarıyla silindi.")
    elif value == 3:
        table_show()
        table_name= input("Tablo adını giriniz:")
        show(table_name)
        id_value = input('Güncellenecek ID: ')
        update(table_name,id_value)
    elif value == 4:
        table_show()
        table_name= input("Tablo adını giriniz:")
        show(table_name)
    elif value == 5:
        table_name= input("Tablo adını giriniz:")
        create_table(table_name)

run = True
while run: #burada başlatacağımız defleri seçeriz. while döngüsü ise baştan başlatmayı sağlar.
    if __name__ == '__main__':
        main()

