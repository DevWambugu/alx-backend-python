#!/usr/bin/env python3
'''generates a list of random
numbers'''
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    '''This function will generate random numbers by calling
    the async generator function'''
    random_numbers = [i async for i in async_generator()]
    return random_numbers
