import time
import asyncio
from concurrent.futures import ProcessPoolExecutor

class As:
    def __init__(self):
        self.n = 0
        self.run()

    async def increase_n(self):
        while True:
            self.n += 1
            await asyncio.sleep(3)
            print(self.n)

    async def check_n(self):
        while True:
            if self.n == 5:
                print('Correct')
                raise TypeError
            else:
                print('Not yet', self.n)
            await asyncio.sleep(1)
    
    def run(self):
        # executor = ProcessPoolExecutor(2)
        asyncio.ensure_future(self.check_n())
        asyncio.ensure_future(self.increase_n())

        loop = asyncio.get_event_loop()
        loop.run_forever()

asn = As()