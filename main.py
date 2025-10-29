from crud import *

if __name__ == '__main__':
    # init_db()
    print('''
    Привіт
     Це інтерфейс для роботи з учнями та курсами
     ''')

    while True:
        print('''
        1 - отримати всіх студентів
        2 - створити студента
        3 - редагувати студента
        4 - видалити студента

         0 - вийти

         1 - отримати всі курсі
         2 - створит курс
         3 - редагувати курс
         4 - видалити курс

         9 -писати студента на курс
        ''')
        answer = input("Очікую відповідь\n")

        if answer == '1':
            for student in get_all_students():
                print(student)

        if answer == '2':
            name = input("Введіть ім'я:")
            age = int(input("Введіть вік студента:"))
            major = input("Введіть курс:")
            add_student(name, age, major)

        elif answer == '0':
            break