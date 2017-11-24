import time
import os
import sched
import realtime_boxoffice as rb
import latest_news as ln
import stock_top_list as stl
import threading as th

  
schedule = sched.scheduler(time.time, time.sleep)


def execute_command(arg1, inc):
    os.system(arg1)
    schedule.enter(inc, 0, execute_command, (arg1, inc))


def main(arg1, func, inc=60):
     
    schedule.enter(0, 0, func, (arg1, inc))
    schedule.run()


def realtime_box(arg1, inc):
    rb.prepare_data()
    schedule.enter(inc, 0, realtime_box, (arg1, inc))


def latest_news(arg1, inc):
    ln.prepare_data()
    schedule.enter(inc, 0, latest_news, (arg1, inc))


def stock_top_list(arg1, inc):
    stl.prepare_data()
    schedule.enter(inc, 0, stock_top_list, (arg1, inc))


if __name__ == '__main__':
    threads = []
    t1 = th.Thread(target=main, args=(None, realtime_box, 3600))
    t2 = th.Thread(target=main, args=(None, latest_news, 1800))
    t3 = th.Thread(target=main, args=(None, stock_top_list, 7200))
    threads.append(t1)
    threads.append(t2)
    threads.append(t3)
    for t in threads:
        t.start()
