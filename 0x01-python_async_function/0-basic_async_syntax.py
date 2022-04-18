#!/usr/bin/env python3

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Waits a random delay between 0 and max delay then returns the value.

    Args:
        max_delay: The maximum delay
    Returns:
        A random float value between 0 and max_delay
    """
    delay_value = random.uniform(0, max_delay)
    await asyncio.sleep(delay_value)
    return delay_value

