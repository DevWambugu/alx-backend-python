#!/usr/bin/env python3
'''0-basic_async_syntax.py'''

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''This asynchronous coroutine takes in an
    integer argument (max_delay, with a default value of 10)
    named wait_random that waits for a random delay
    between 0 and max_delay (included and float value)
    seconds and eventually returns it'''
    delay_time = random.uniform(0, max_delay)
    await asyncio.sleep(delay_time)
    return delay_time
