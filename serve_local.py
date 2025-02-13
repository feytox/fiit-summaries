import shutil
import subprocess
import argparse
import os
import glob


QUARTZ_DIR = "quartz"


def main(fast_start: bool, fast_setup: bool):
    if fast_start and fast_setup:
        setup()
        start()
        return

    if fast_start:
        start()
        return
    
    if fast_setup:
        setup()
        return

    display_info()
    inp = input("> ")
    
    if inp == "1":
        start()
    elif inp == "2":
        setup()


def display_info():
    print("--------------------------------------")
    print("Скрипт для локального запуска Quartz")
    print("--------------------------------------\n")

    print("Требования перед запуском (нужно сделать 1 раз):")
    print("1. Установить Node и npm")
    print("2. Находясь в папке quartz, выполнить следующее: (или пункт Setup)")
    print("npm i\nnpm audit fix\n")

    print("После запуска скрипта будет удалено всё содержимое папки quartz/content")
    print("Эта папка используется лишь для билда, поэтому не стоит что-либо пытаться редактировать в ней.\n")

    print("Выберите действие:\n 1. Запуск\n 2. Setup\n 9. Стоп")

def setup():
    run("npm i")
    run("npm audit fix")


def start():
    shutil.rmtree("quartz/content", ignore_errors=True)
    shutil.copytree("content", "quartz/content", dirs_exist_ok=True)
    shutil.copytree("assets", "quartz/content/assets", dirs_exist_ok=True)
    for md in glob.glob("quartz/content/assets/*.md"):
        os.remove(md)
    
    run_simple("python transform_files.py")
    run("npx quartz build --serve")

def run_simple(command: str):
    process_result = subprocess.run(
        command,
        cwd=QUARTZ_DIR,
        shell=True,
        capture_output=True,
        text=True,
        check=True
    )
    print(process_result.stdout.strip())
    print(process_result.stderr.strip())

def run(command: str):
    process = subprocess.Popen(
        command,
        cwd=QUARTZ_DIR,
        shell=True
    )
    
    try:
        process.wait()
    except KeyboardInterrupt:
        return
    if process.returncode != 0:
        print(f"Команда завершилась с кодом ошибки: {process.returncode}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Скрипт для локального запуска Quartz")
    parser.add_argument("-f", "--fast", action="store_true", help="Быстрый запуск")
    parser.add_argument("-s", "--setup", action="store_true", help="Быстрый Setup")
    args = parser.parse_args()

    main(args.fast, args.setup)