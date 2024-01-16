#!/usr/bin/env python3

import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    random_numbers = [i async for i in async_generator()]
    return random_numbers
