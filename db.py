import sqlite3

def create_table(): #eğer yeni table açmak istiyorsanız _name_ kısmına create_table() yazmalısınız.

  connection = sqlite3.connect('database.sqlite')
  cursor = connection.cursor()
  cursor.execute('CREATE TABLE users9 (id INT ,username TEXT, password TEXT)')
  connection.commit()
  connection.close()

def register_user(id_value,username, password): #veri ekler

  connection = sqlite3.connect('database.sqlite')
  cursor = connection.cursor()
  try:
    cursor.execute('INSERT INTO users9 (id, username, password) VALUES (?, ?, ?)', (id_value, username, password))
    connection.commit()
  except Exception as e:
    print(f"Hata !!: {str(e)}")

  connection.close()

def show(): #verileri gösterir
  connection = sqlite3.connect('database.sqlite')
  cursor=connection.cursor()
  cursor.execute('SELECT * FROM users9')
  rows = cursor.fetchall()
  for row in rows:
    print("----------------")
    print(row)
    print("----------------")

  connection.commit()
  connection.close()

def update(id_value,username): #verileri günceller
  connection = sqlite3.connect('database.sqlite')
  cursor = connection.cursor()
  try:
    cursor.execute('UPDATE users9 SET id = ? WHERE username = ?', (id_value, username))
    print("Başarıyla güncellendi.")
    connection.commit()  # Commit the changes to the database
  except Exception as e:
    print(f"Hata !!: {str(e)}")

def delete(id_value): #veriyi siler.
  connection = sqlite3.connect('database.sqlite')
  cursor = connection.cursor()
  try:
    cursor.execute('DELETE FROM users9 WHERE id = ?', (id_value,))
    connection.commit()
  except Exception as e:
    print(f"Hata !!: {str(e)}")

  connection.close()

run = True

def main():
  print("Ekleme:1, Silme:2, Güncelleme:3, Verileri Görmek için 4 yazınız.")
  value = int(input("Yapacağınız işlemi seçiniz:"))
  if value == 1:
    id_value = int(input("Enter id : "))
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    register_user(id_value,username, password)
    print("Başarıyla eklendi.")
    show()
  if value ==2:
    id_value = input('Silinecek id: ')
    delete(id_value)
    show()
  if value == 3:
    id_value = input('Id : ')
    username = input("Güncellenecek veriyi yaz< : ")
    update(id_value,username)
    show()
  if value == 4:
    show()
while run:
  if __name__ == '__main__': 
    main()
  