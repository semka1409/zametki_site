import sqlite3
import tkinter as tk
from tkinter import messagebox

# Создание базы данных и таблицы
def create_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Регистрация нового пользователя
def register_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        messagebox.showinfo("Регистрация", "Регистрация успешна!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Регистрация", "Пользователь с таким именем уже существует.")
    conn.close()

# Вход пользователя
def login_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    conn.close()
    if user:
        messagebox.showinfo("Вход", "Вход успешен!")
        return True
    else:
        messagebox.showerror("Вход", "Неверное имя пользователя или пароль.")
        return False

# Функция для регистрации пользователя
def register():
    username = entry_username.get()
    password = entry_password.get()
    register_user(username, password)

# Функция для входа пользователя
def login():
    username = entry_username.get()
    password = entry_password.get()
    login_user(username, password)

# Основное окно приложения
root = tk.Tk()
root.title("Вход/Выход из сервиса")

# Создание элементов интерфейса
label_username = tk.Label(root, text="Имя пользователя:")
label_password = tk.Label(root, text="Пароль:")
entry_username = tk.Entry(root)
entry_password = tk.Entry(root, show="*")
button_register = tk.Button(root, text="Зарегистрироваться", command=register)
button_login = tk.Button(root, text="Войти", command=login)

# Размещение элементов на окне
label_username.grid(row=0, column=0, padx=10, pady=10)
entry_username.grid(row=0, column=1, padx=10, pady=10)
label_password.grid(row=1, column=0, padx=10, pady=10)
entry_password.grid(row=1, column=1, padx=10, pady=10)
button_register.grid(row=2, column=0, padx=10, pady=10)
button_login.grid(row=2, column=1, padx=10, pady=10)

# Создание базы данных при запуске приложения
create_database()

# Запуск основного цикла приложения
root.mainloop()
