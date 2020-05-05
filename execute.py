# -*- coding: UTF-8 -*-
"""
@time:2020/04/06
"""
import time

import schedule

from TimeTask.jobs.weather import get_data

def demo3():
    # schedule.every(10).seconds.do(get_data)
    # schedule.every().day.at("9:30").do(get_data)
    schedule.every().day.at("10:30").do(get_data)


    while 1:
        schedule.run_pending()
        time.sleep(10)
        print('end')


if __name__ == '__main__':
    demo3()
