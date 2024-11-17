# Домашнее задание по теме "Многопроцессорное программирование"
import time
from multiprocessing import Pool


# Функция для считывания информации из одного файла
def read_info(filename):
    # Создаём локальный список для хранения данных
    all_data = []

    # Открываем файл для чтения
    with open(filename, 'r') as file:
        # Считываем данные построчно
        line = file.readline()

        # Продолжаем чтение, пока строки не закончатся
        while line:
            # Добавляем прочитанную строку в список
            all_data.append(line.strip())

            # Читаем следующую строку
            line = file.readline()


# Генерация списка названий файлов
filenames = [f'./file_{i}.txt' for i in range(1, 5)]  # Файлы называются file_1.txt, file_2.txt и т.д.

if __name__ == "__main__":
    # Линейный вызов функции read_info для каждого файла
    start_time_linear = time.time()

    for filename in filenames:
        read_info(filename)

    end_time_linear = time.time()
    linear_execution_time = end_time_linear - start_time_linear
    print(f"Время выполнения линейной обработки: {linear_execution_time:.6f} сек.")

    # Многопроцессорный вызов функции read_info для каждого файла
    start_time_multiproc = time.time()

    # Создание пула процессов
    with Pool(processes=4) as pool:
        # Вызов функции read_info для каждого файла параллельно
        pool.map(read_info, filenames)

    end_time_multiproc = time.time()
    multiproc_execution_time = end_time_multiproc - start_time_multiproc
    print(f"Время выполнения многопроцессорной обработки: {multiproc_execution_time:.6f} сек.")