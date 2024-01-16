#!/usr/bin/env python3
'''This script generates a corooutine function'''

import asyncio
import random


async def async_generator():
    '''This function generates a coroutine that loops asynchronously
    wait for one second then yield a random number betwen 0 and 10'''
    for loop in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
