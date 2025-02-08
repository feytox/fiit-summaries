import shutil
import subprocess
import argparse


QUARTZ_DIR = "quartz"


def main(fast_start: bool):
    if fast_start:
        start()
        return

    display_info()
    inp = input("> ")
    
    if inp == "1":
        start()


def display_info():
    print("--------------------------------------")
    print("Скрипт для локального запуска Quartz")
    print("--------------------------------------\n")

    print("Требования перед запуском (нужно сделать 1 раз):")
    print("1. Установить Node и npm")
    print("2. Находясь в папке quartz, выполнить следующее:")
    print("npm i\nnpm audit fix\n")

    print("После запуска скрипта будет удалено всё содержимое папки quartz/content")
    print("Эта папка используется лишь для билда, поэтому не стоит что-либо пытаться редактировать в ней.\n")

    print("Выберите действие:\n 1. Запуск\n 9. Стоп")


def start():
    shutil.rmtree("quartz/content")
    shutil.copytree("content", "quartz/content", dirs_exist_ok=True)
    run_simple("python transform_files.py")
    run_no_pipe("npx quartz build --serve")

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
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
        universal_newlines=True
    )

    for output in process.stdout:
        print(output.strip())

    process.wait()
    if process.returncode != 0:
        print(f"Команда завершилась с кодом ошибки: {process.returncode}")

def run_no_pipe(command: str):
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
    parser.add_argument("-f", "--fast", action=argparse.BooleanOptionalAction, help="Запуск без информации о скрипте")
    args = parser.parse_args()
    fast_start = args.fast

    main(fast_start if fast_start else False)