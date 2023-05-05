import logging
import hashlib
from tqdm import tqdm
from typing import Optional
import multiprocessing as mp

logger = logging.getLogger()
logger.setLevel('INFO')


def check_card_number(hash: str, card_number: str) -> int:
    """
    Функция проверяет, соответствует ли номер карты хешу
    :param hash: Хеш
    :param card_number: Номер карты
    :return: Номер карты, если сооветствует, -1 - если не соответствует
    """
    true_hash = hashlib.blake2b(card_number.encode()).hexdigest()
    if hash == true_hash:
        return int(card_number)
    return 0


def enumerate_card_number(hash: str, bins: list, last_four_numbers: str, core_number: int = mp.cpu_count()) \
        -> Optional[int]:
    """
    Функция подбираем номер карты
    :param hash: Хеш карты
    :param bins: набор БИНов карты
    :param last_four_numbers: Последние 4 цифры карты
    :param core_number: Количество ядер
    :return: Номер карты, если найден, если нет - ничего
    """
    args = []
    for i in range(1000000):
        for j in bins:
            args.append((hash, f"{j}{i:06d}{last_four_numbers}"))
    with mp.Pool(processes=core_number) as p:
        for res in p.starmap(check_card_number, tqdm(args, ncols=120)):
            if res:
                p.terminate()
                return res
    return None
