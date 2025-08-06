import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)


def show_tasks(tasks):
    if not tasks:
        print("Список дел пуст!")
    else:
        print("Список дел:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")


def add_task(tasks):
    task = input("Введите новое дело: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Дело добавлено!")


def delete_task(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            num = int(input("Введите номер дела для удаления: "))
            if 1 <= num <= len(tasks):
                tasks.pop(num - 1)
                save_tasks(tasks)
                print("Дело удалено!")
            else:
                print("Некорректный номер!")
        except ValueError:
            print("Введите число!")


def main():
    tasks = load_tasks()
    while True:
        print("\nМеню:")
        print("1. Показать дела")
        print("2. Добавить дело")
        print("3. Удалить дело")
        print("4. Выход")

        choice = input("Выберите действие (1-4): ")
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Некорректный ввод!")


if __name__ == "__main__":
    main()