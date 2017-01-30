# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 18:31:18 2017

@author: miniesta4
"""

import time

def timedcall(f, *args):
    '''
    Call function wiht args; return the time in seconds and result.
    '''
    t0 = time.clock()
    result = f(*args)
    t1 = time.clock()
    return t1-t0, result

def timedcalls(n, f, *args):
    """Call fn(*args) repeatedly: n times if n is an int, or up to
    n seconds if n is a float; return the min, avg, and max time"""
    if isinstance(n, int):
        times = [timedcall(f, *args)[0] for _ in range(n)]
    else:
        times = []
        while sum(times) < n:
            times.append(timedcall(f, *args)[0])
    return min(times), average(times), max(times)

def average(numbers):
    '''
    Return the average (arithmetic mean) of a sequence of numbers.
    '''
    return sum(numbers) / len(numbers)
