import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

#NOTES#
## Üye kaydetme programı 
# Author : Protesq 
# Instagram : blog_vari ##

selected_table_var = None 
table_listbox = None
selected_table = None
selected_delete_table = None
status = False
#############################-Arka Planda Çalışanlar########################################
def refresh_tree():
    if selected_table:
        tree.delete(*tree.get_children())  
        conn = sqlite3.connect("database.sqlite")
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {selected_table}")
        rows = cur.fetchall()
        for row in rows:
            tree.insert("", "end", values=row)
        conn.close()

def refresh_tree2():
    if selected_table:
        tree2.delete(*tree2.get_children())  
        conn = sqlite3.connect("database.sqlite")
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {selected_table}")
        rows = cur.fetchall()
        for row in rows:
            tree2.insert("", "end", values=row)
        conn.close()

def show_text():
    user_text = user_entry.get()
    pass_text = pass_entry.get()
    login(user_text, pass_text)
    home_page.destroy()

#def table_show_text():
#    table_text = table_entry.get()
#    login_2(table_text)
#    before_register_form_page.destroy()

def add_data():
    user_name_text = user_add.get()
    pass_name_text = pass_add.get()
    if selected_table:
        add_database(selected_table, user_name_text, pass_name_text)

def delete_data():
    selected_item = tree.selection()
    if selected_item:
        id_value = tree.item(selected_item)["values"][0]  
        delete(id_value, selected_table)
        refresh_tree()

def delete_data_table():
    selected_item = tree2.selection()
    if selected_item:
        item_id = selected_item[0]
        table_name = tree2.item(item_id, 'values')[0]
        delete_table(table_name)
    else:
        print("No table selected for deletion.")

def delete_table(table_name):
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()

    try:
        cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
        connection.commit()
        print(f"Table '{table_name}' deleted successfully.")
    except Exception as e:
        print(f"Error deleting table: {str(e)}")
    finally:
        connection.close()
        refresh_tree2()



def update_data():
    user_name_text = user_add.get()
    pass_name_text = pass_add.get()
    if selected_table:
        update_database(selected_table, user_name_text, pass_name_text)

def add_database(table_name, user_name, password):
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()

    try:
        ex_query= f'SELECT COUNT(*) FROM {table_name} WHERE username=?'
        cursor.execute(ex_query,(user_name,))
        ex_count = cursor.fetchone()[0]
        if ex_count == 0:
            query = f'INSERT INTO {table_name} (username, password) VALUES (?, ?)'
            cursor.execute(query, (user_name, password))
            connection.commit()
            user_id = cursor.lastrowid
            print(f'Kullanıcı başarıyla kaydedildi. ID: {user_id}')
            messagebox.showinfo('Başarılı', 'Kullanıcı başarıyla kaydedildi.')
        else :
             messagebox.showinfo('Başarısız', 'Bu kullanıcı mevcut')

    except Exception as e:
        print(f'Hata: {str(e)}')
        messagebox.showerror('Hata', f'Veritabanına kaydedilirken bir hata oluştu: {str(e)}')
    finally:
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



def update_database(table_name, user_name, password):
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()

    try:
        query = f'INSERT INTO {table_name} (username, password) VALUES (?, ?)'
        cursor.execute(query, (user_name, password))
        connection.commit()
        user_id = cursor.lastrowid
        print(f'Kullanıcı başarıyla kaydedildi. ID: {user_id}')
        messagebox.showinfo('Başarılı', 'Kullanıcı başarıyla kaydedildi.')
    except Exception as e:
        print(f'Hata: {str(e)}')
        messagebox.showerror('Hata', f'Veritabanına kaydedilirken bir hata oluştu: {str(e)}')
    finally:
        connection.close()

def table_selected(event):
    global selected_table
    selected_indices = table_listbox.curselection()
    if selected_indices:
        selected_index = selected_indices[0]
        selected_table = table_listbox.get(selected_index)
        if selected_table:
            register_form(selected_table)
            before_register_form_page.destroy()

def table_selected2(event):
    global selected_table
    selected_indices = table_listbox.curselection()
    if selected_indices:
        selected_index = selected_indices[0]
        selected_table = table_listbox.get(selected_index)
        if selected_table:
            register_form(selected_table)
            table_page.destroy()

def table_delete_to_selected(event):
    global selected_delete_table
    selected_indices = table_listbox.curselection()
    if selected_indices:
        selected_index = selected_indices[0]
        selected_delete_table = table_listbox.get(selected_index)
        if selected_delete_table:
            delete_data()


#check
def return_page():
    global status
    selectscreen()
    if(status == False):
        table_create.destroy()
        
def return_page_table():
    before_register_form()
    if(status == False):
        register_page.destroy()


def return_page_for_table():
    selectscreen()
    if(status==False):
        table_page.destroy()


def return_before2():
    selectscreen()
    before_register_form_page.destroy()

def add_data_and_refresh():
    add_data()
    refresh_tree()

def update_data_and_refresh():
    update_data()
    refresh_tree()


#############################-Seçim Ekranı-########################################
def select_command():
    tables()

def select_command2():
    table_add()

def selectscreen():
    global select_page
    select_page = tk.Tk()
    select_page.title("Menu")

    screen_width = select_page.winfo_screenwidth()
    screen_height = select_page.winfo_screenheight()

    window_width = 700
    window_height = 600

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    select_page.geometry(f"{window_width}x{window_height}+{x}+{y}")
    select_page.configure(bg="white")

    menu_label = tk.Label(select_page, text="Menüye Hoş geldin !")
    menu_label.pack(pady=20)
        
    before_register_form_button = tk.Button(select_page, text="Veri Ekleme", command=select_command)
    before_register_form_button.pack(pady=10)

    table_create_button = tk.Button(select_page, text="Tablolar", command=select_command2)
    table_create_button.pack(pady=10)

#############################-Tablolar-########################################

def tables():
    status = True
    select_page.destroy()
    global table_page, table_listbox

    table_page = tk.Tk()
    table_page.title("Tables")

    screen_width = table_page.winfo_screenwidth()
    screen_height = table_page.winfo_screenheight()

    window_width = 700
    window_height = 600

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    table_page.geometry(f"{window_width}x{window_height}+{x}+{y}")
    table_page.configure(bg="white")

    table_listbox = tk.Listbox(table_page, width=100, selectmode=tk.YES)  # Tablo seçimi açık
    table_listbox.pack()

    conn = sqlite3.connect("database.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name!='sqlite_master';")
    table_names = cur.fetchall()
    conn.close()
    for name in table_names:
        table_listbox.insert("end", name[0])
        
    table_listbox.bind("<<ListboxSelect>>", table_selected2)


    return_button2 = tk.Button(table_page, text="Geri", command=return_page_for_table)
    return_button2.pack(pady=10)
    table_page.mainloop()
    
#############################-Tablo Ekleme-########################################

def table_refresh_tree():
    table_add()
    table_create.destroy()

def table_create_command():
    table_create_name = table_create_entry.get()
    if table_create_name:
        create_table(table_create_name)

def create_table(table_name):
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()
    
    try:
        cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)')
        print(f"Table '{table_name}' successfully created.")
        table_refresh_tree()

    except Exception as e:
        print(f"Error: {str(e)}")
    connection.commit()
    connection.close()

def table_add():
    status_tables = False
    status = True
    select_page.destroy()
    global table_create, table_create_entry,tree2

    table_create = tk.Tk()
    table_create.title("Tables Add")

    screen_width = table_create.winfo_screenwidth()
    screen_height = table_create.winfo_screenheight()

    window_width = 700
    window_height = 600

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    table_create.geometry(f"{window_width}x{window_height}+{x}+{y}")
    table_create.configure(bg="white")

    tree2 = ttk.Treeview(table_create, columns=["Tablo Adı"], show="headings")
    tree2.heading("Tablo Adı", text="Tablo Adı")
    tree2.column("Tablo Adı", width=150, anchor=tk.CENTER)
    tree2.pack()
    
    conn = sqlite3.connect("database.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name!='sqlite_master';")
    table_names = cur.fetchall()
    conn.close()
    for name in table_names:
        tree2.insert("", "end", values=name)

    
    table_create_entry = tk.Entry(table_create, width=40)
    table_create_entry.pack(pady=10)

    table_create_button = tk.Button(table_create, text="Oluştur", command=table_create_command)
    table_create_button.pack(pady=10)
#############################-Tablo Silme-########################################


    label_delete = tk.Label(table_create, text="Tablo Silme Alanı")
    label_delete.pack(pady=20)

    delete_selected_button = tk.Button(table_create, text="Seçileni Sil", command=delete_data_table)
    delete_selected_button.pack(pady=10)


    return_button2 = tk.Button(table_create, text="Geri", command=return_page)
    return_button2.pack(pady=10)
    table_create.mainloop()

#############################-Tablo Seçim Ekranı-########################################


def before_register_form():
    global table_entry, before_register_form_page, table_listbox
    before_register_form_page = tk.Tk()
    before_register_form_page.title("Tables")
    screen_width = before_register_form_page.winfo_screenwidth()
    screen_height = before_register_form_page.winfo_screenheight()

    window_width = 700
    window_height = 600

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    before_register_form_page.geometry(f"{window_width}x{window_height}+{x}+{y}")
    before_register_form_page.configure(bg="white")


    label_user = tk.Label(before_register_form_page, text="BİR TABLO SEÇİNİZ.:")
    label_user.pack(pady=20)
    

    table_listbox = tk.Listbox(before_register_form_page,width=100)
    table_listbox.pack()

    conn = sqlite3.connect("database.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name!='sqlite_master';")
    table_names = cur.fetchall()
    conn.close()
    for name in table_names:
        table_listbox.insert("end", name[0])

    table_listbox.bind("<<ListboxSelect>>", table_selected)

    return_button2 = tk.Button(before_register_form_page, text="Geri", command=return_before2)
    return_button2.pack(pady=10)
#############################-Kullanıcı Kaydetme,Silme,Güncelleme-########################################

def register_form(table_name):
    global pass_add, user_add, register_page, tree

    def refresh_tree():
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("database.sqlite")
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {table_name}")
        rows = cur.fetchall()
        for row in rows:
            tree.insert("", "end", values=row)
        conn.close()

    register_page = tk.Tk()
    register_page.title("Register Page")
    screen_width = register_page.winfo_screenwidth()
    screen_height = register_page.winfo_screenheight()

    window_width = 700
    window_height = 600

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    register_page.geometry(f"{window_width}x{window_height}+{x}+{y}")
    register_page.configure(bg="white")

    label_baslik = tk.Label(register_page, text="Kayıt Formu")
    label_baslik.pack(pady=20)
    


    tree = ttk.Treeview(register_page, columns=("ID", "Kullanıcı Adı", "Şifre"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Kullanıcı Adı", text="Kullanıcı Adı")
    tree.heading("Şifre", text="Şifre")
    tree.column("ID", width=50, anchor=tk.CENTER)
    tree.column("Kullanıcı Adı", width=200, anchor=tk.W)
    tree.column("Şifre", width=200, anchor=tk.W)
    tree.pack()
    

#############################-Kullanıcı Kaydetme-########################################


    label_add = tk.Label(register_page, text="Kullanıcı Kaydetme Alanı")
    label_add.pack(pady=20)

    label_user = tk.Label(register_page, text="Kullanıcı Adı:")
    label_user.pack(pady=20)

    user_add = tk.Entry(register_page, width=40)
    user_add.pack(pady=10)

    label_pass = tk.Label(register_page, text="Şifre:")
    label_pass.pack(pady=20)

    pass_add = tk.Entry(register_page, width=40)
    pass_add.pack(pady=10)

    show2_button = tk.Button(register_page, text="Kaydet", command=add_data_and_refresh)
    show2_button.pack(pady=10)

#############################-Kullanıcı Silme-########################################

    label_delete = tk.Label(register_page, text="Kullanıcı Silme Alanı")
    label_delete.pack(pady=20)

    delete_selected_button = tk.Button(register_page, text="Seçileni Sil", command=delete_data)
    delete_selected_button.pack(pady=10)


#############################-Kullanıcı Güncelleme-########################################
    def update_data(selected_item):
        def update_selected_data():
            new_user = user_update.get()
            new_pass = pass_update.get()

            if new_user and new_pass:
                conn = sqlite3.connect("database.sqlite")
                cur = conn.cursor()
                cur.execute(f"UPDATE {table_name} SET username=?, password=? WHERE ID=?", (new_user, new_pass, selected_item[0]))
                conn.commit()
                conn.close()
                refresh_tree()
                update_page.destroy()

        update_page = tk.Toplevel(register_page)
        update_page.title("Veri Güncelleme")

        user_update = tk.Entry(update_page, width=40)
        user_update.insert(0, selected_item[1])  # Existing username
        user_update.pack(pady=10)

        pass_update = tk.Entry(update_page, width=40)
        pass_update.insert(0, selected_item[2])  # Existing password
        pass_update.pack(pady=10)

    def on_item_selected(event):
        selected_item = tree.item(tree.selection())["values"]
        update_data(selected_item)
    tree.bind("<ButtonRelease-1>", on_item_selected)

#####################################################################################
    return_button = tk.Button(register_page, text="Geri", command=return_page_table)
    return_button.pack(pady=10)
    refresh_tree()

#############################-Admin Panele Giriş-########################################

def home():
    global user_entry, pass_entry, home_page
    home_page = tk.Tk()
    home_page.title("Home Page")
    screen_width = home_page.winfo_screenwidth()
    screen_height = home_page.winfo_screenheight()

    window_width = 700
    window_height = 600

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    home_page.geometry(f"{window_width}x{window_height}+{x}+{y}")
    home_page.configure(bg="white")

    label = tk.Label(home_page, text="Kullanıcı Adı: ")
    label.pack(pady=20)

    user_entry = tk.Entry(home_page, width=40)
    user_entry.pack(pady=10)

    label2 = tk.Label(home_page, text="Şifre:")
    label2.pack(pady=20)

    pass_entry = tk.Entry(home_page, width=40, show="*")
    pass_entry.pack(pady=10)

    show_button = tk.Button(home_page, text="Giriş yap", command=show_text)
    show_button.pack()

    home_page.mainloop()

#def login_2(table_text):
#    connection = sqlite3.connect('database.sqlite')
#    cursor = connection.cursor()
#    check = cursor.execute(f'SELECT * FROM {table_text}')
#    connection.commit()
#    if cursor.fetchone():
#        messagebox.showinfo("Uyarı !", "Giriş Başarılı.")
#        register_form(table_text)
#    else:
#        messagebox.showerror("Giriş Hatası", "Tablo adı yanlış !.")
#    connection.close()

def login(user_text, pass_text):
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()
    check = cursor.execute("SELECT username FROM kullanici WHERE username = ? AND Password = ?;", (user_text, pass_text))
    connection.commit()
    if cursor.fetchone():
        messagebox.showinfo("Uyarı !", "Giriş Başarılı.")
        selectscreen()
    else:
        messagebox.showerror("Giriş Hatası", "Kullanıcı adı veya şifre yanlış.")
    connection.close()


if __name__ == '__main__':
    home()
