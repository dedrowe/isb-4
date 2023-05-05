import logging
import csv

logger = logging.getLogger()
logger.setLevel('INFO')


def read_data_from_txt_file(file_name: str) -> str:
    """
    Функция считывает данные из txt файла
    :param file_name: Путь к файлу
    :return: Строка с данными
    """
    try:
        with open(file_name, 'r') as f:
            data = f.read()
        logging.info("Данные успешно считаны")
    except OSError as err:
        logging.warning(f"{err} Не удалось считать данные")
    return data


def write_data_to_txt_file(data: str, file_name: str) -> None:
    """
    Функция записывает данные в txt файл
    :param data: Данные для записи
    :param file_name: Путь к файлу
    :return: Функция ничего не возвращает
    """
    try:
        with open(file_name, 'w') as f:
            f.write(data)
        logging.info("Данные успешно записаны")
    except OSError as err:
        logging.warning(f"{err} Не удалось записать данные")


def read_list(file_name: str) -> list:
    """
    Функция считывает кортеж из файла
    :param file_name: Путь к файлу
    :return: Кортеж
    """
    data = []
    try:
        with open(file_name, 'r') as f:
            data = f.readlines()
            data = list(map(int, data))
        logging.info("Данные успешно считаны")
    except OSError as err:
        logging.warning(f"{err} Не удалось считать данные")
    return data


def load_statistics(file_name: str) -> dict:
    """
    Функция считывает статистику из файла
    :param file_name: Имя файла
    :return: Словарь вида: (количество процессов: время)
    """
    try:
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            stats = list(reader)
        logging.info("Статистика успешно считана")
    except OSError as err:
        logging.warning(f"{err} Не удалось считать статистику")
    result = dict()
    for i in stats:
        processes, time = i
        result[int(processes)] = float(time)
    return result


def write_statistics(processes: int, time: float, file_name: str) -> None:
    """
    Функция записывает статистику в файл
    :param processes:
    :param time:
    :param file_name:
    :return: Функция ничего не возвращает
    """
    try:
        with open(file_name, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([processes, time])
        logging.info("Статистика успешно записана")
    except OSError as err:
        logging.warning(f"{err} Не удалось записать статистику")
