"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta
import locale
locale.setlocale(locale.LC_TIME, 'ru_RU')

def print_days():

    date_nw = datetime.now()
    dt_nw = date_nw.strftime('%A %d %B %Y')

    delta = timedelta(days = 1)
    dt_yesterday = date_nw - delta
    dt_ystd = dt_yesterday.strftime('%A %d %B %Y')

    delta_2 = timedelta(days = 30)
    dt_30 = date_nw - delta_2
    dt_back = dt_30.strftime('%A %d %B %Y')

    print(dt_ystd,dt_nw, dt_back, sep = '\n')


def str_2_datetime(date_string):

    date_string = '01/01/20 12:10:03.234567'
    date_dat = datetime.strptime(date_string, '%d/%m/%Y %H:%M:%S.%f')
    print(date_dat)



if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
