import json
import logging

logger = logging.getLogger()
logger.setLevel('INFO')

SETTINGS = {
    'hash': 'files/hash.txt',
    'bin': 'files/bin_numbers.txt',
    'last_four_numbers': 'files/last_four_numbers.txt',
    'card_number': 'files/card_number.txt',
    'csv_statistics': 'files/statistics.csv',
    'png_statistics': 'files/statistics.png'
}


def read_settings(file_with_settings: str = 'files/settings.json') -> dict:
    """
    Фукнция считывает настройки из файла
    :param file_with_settings: Путь к файлу с настройками
    :return: Настройки
    """
    settings = None
    try:
        with open(file_with_settings, 'r') as f:
            settings = json.load(f)
        logging.info("Настройки успешно считаны")
    except OSError as err:
        logging.warning(f"{err} Не удалось считать настройки")
    return settings


if __name__ == "__main__":
    with open('files/settings.json', 'w') as f:
        json.dump(SETTINGS, f)
