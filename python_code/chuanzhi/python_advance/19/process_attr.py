#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : process.py
# @Author: ly
# @Date  : 2018/12/8


import multiprocessing
import os
import time


def c_process_func(name, play):
    for i in range(5):
        print('我是子进程, 我叫 %s 我演过 %s 我的 pid 是 %s' % (name, play, multiprocessing.current_process().pid))
        print('我是子进程，我的父id 是 %s' % os.getppid())
        time.sleep(1)


def main():
    """单进程 单线程 之前写的代码在主线程上"""
    c_p = multiprocessing.Process(target=c_process_func, args=('zhaobenshan',), kwargs={'play':'xiaopin'})
    print('使用子进程实例获取 PID 为 %s 以及子进程名称为 %s' % (c_p.pid, c_p.name))
    c_p.start()
    # c_p.join()
    # c_p.join(3)
    c_p.terminate()
    while True:
        print('这是主进程, 使用 os 获取 pid 的值为 %s' % os.getpid())
        time.sleep(1)


if __name__ == '__main__':
    main()
