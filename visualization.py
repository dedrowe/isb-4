import logging
import matplotlib.pyplot as plt

logger = logging.getLogger()
logger.setLevel('INFO')


def create_png_with_statistics(statistics: dict, file_name: str) -> None:
    """
    Функция создает гистограмму со статистикой и сохраняет ее как png файл
    :param statistics: Статистика
    :param file_name: Путь к файлу
    :return: Функция ничего не возвращает
    """
    fig = plt.figure(figsize=(30, 5))
    plt.ylabel('time')
    plt.xlabel('processes')
    plt.title('statistics')
    x = statistics.keys()
    y = statistics.values()
    plt.bar(x, y, color='grey', width=0.5)
    plt.savefig(file_name)
