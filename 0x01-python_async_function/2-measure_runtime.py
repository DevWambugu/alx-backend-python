#!/usr/bin/env python3

'''2-measure_runtime.py'''
import asyncio
import random
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int = 10) -> float:
    '''Creates a measure_time function with integers n
    and max_delay as arguments that measures the total
    execution time for wait_n(n, max_delay),
    and returns total_time / n. '''
    start_time = time.perf_counter()
    time_delays = asyncio.run(wait_n(n, max_delay))
    ending_time = time.perf_counter()
    total_time = ending_time - start_time
    return total_time / n
