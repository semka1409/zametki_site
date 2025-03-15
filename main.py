import sqlite3

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
        print("Регистрация успешна!")
    except sqlite3.IntegrityError:
        print("Пользователь с таким именем уже существует.")
    conn.close()

# Вход пользователя
def login_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    conn.close()
    if user:
        print("Вход успешен!")
        return True
    else:
        print("Неверное имя пользователя или пароль.")
        return False

# Выход пользователя
def logout_user():
    print("Вы вышли из системы.")

# Основной цикл программы
def main():
    create_database()
    while True:
        print("\n1. Регистрация\n2. Вход\n3. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            username = input("Введите имя пользователя: ")
            password = input("Введите пароль: ")
            register_user(username, password)
        elif choice == '2':
            username = input("Введите имя пользователя: ")
            password = input("Введите пароль: ")
            if login_user(username, password):
                while True:
                    print("\n1. Выйти из системы\n2. Вернуться в главное меню")
                    action = input("Выберите действие: ")
                    if action == '1':
                        logout_user()
                        break
                    elif action == '2':
                        break
        elif choice == '3':
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
