import os
import subprocess
import sys
import platform

def create_virtual_env():
    """Создает виртуальное окружение, если его нет."""
    if not os.path.exists("venv"):
        print("Создаю виртуальное окружение...")
        subprocess.check_call([sys.executable, "-m", "venv", "venv"])
        print("Виртуальное окружение создано.")
    else:
        print("Виртуальное окружение уже существует.")

def install_dependencies():
    """Устанавливает зависимости из requirements.txt."""
    print("Устанавливаю зависимости...")
    pip_path = get_pip_path()
    subprocess.check_call([pip_path, "install", "-r", "requirements.txt"])
    print("Зависимости установлены.")

def add_dependency(library):
    """Добавляет библиотеку в requirements.txt и устанавливает её."""
    pip_path = get_pip_path()

    # Проверяем, установлена ли библиотека
    try:
        subprocess.check_call([pip_path, "install", library])
    except subprocess.CalledProcessError:
        print(f"Ошибка при установке библиотеки: {library}")
        return

    # Добавляем библиотеку в requirements.txt
    with open("requirements.txt", "a") as req_file:
        req_file.write(f"{library}\n")
    print(f"Библиотека {library} добавлена в requirements.txt и установлена.")

def get_pip_path():
    """Возвращает путь до pip внутри виртуального окружения."""
    if platform.system() == "Windows":
        return os.path.join("venv", "Scripts", "pip")
    else:
        return os.path.join("venv", "bin", "pip")

def run_project():
    """Запускает основной файл проекта."""
    print("Запускаю проект...")
    python_path = get_python_path()
    subprocess.run([python_path, "src/main.py"])

def get_python_path():
    """Возвращает путь до Python внутри виртуального окружения."""
    if platform.system() == "Windows":
        return os.path.join("venv", "Scripts", "python")
    else:
        return os.path.join("venv", "bin", "python")

def main():
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "setup":
            create_virtual_env()
            install_dependencies()
            print("Сборка завершена.")
        elif command == "run":
            run_project()
        elif command == "add":
            if len(sys.argv) > 2:
                library = sys.argv[2]
                add_dependency(library)
            else:
                print("Укажите название библиотеки для добавления.")
        elif command == "start":
            # Выполняем сборку и запускаем программу последовательно
            print("Начинаю процесс сборки и запуска программы...")
            create_virtual_env()
            install_dependencies()
            run_project()
        else:
            print(f"Неизвестная команда: {command}")
    else:
        print("Используйте команды: setup, run, add, start")

if __name__ == "__main__":
    main()