import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

print('running async test')

def say_boo():
    i = 0
    while True:
        print('...boo {0}'.format(i))
        i += 1
        time.sleep(4)


def say_baa():
    i = 0
    while True:
        print('...baa {0}'.format(i))
        i += 1
        time.sleep(4)

def make_noise():
    while True:
        print('making noooise')
        time.sleep(1)

def run():
    executor = ProcessPoolExecutor(3)
    loop = asyncio.get_event_loop()
    boo = asyncio.ensure_future(loop.run_in_executor(executor, say_boo))
    baa = asyncio.ensure_future(loop.run_in_executor(executor, say_baa))
    noise = asyncio.ensure_future(loop.run_in_executor(executor, make_noise))

    loop.run_forever()

run()