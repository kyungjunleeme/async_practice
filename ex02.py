# Python 3.7+
import asyncio
import random
async def lazy_greet(msg, delay=1):
    print(f'{msg!r} will be displayed in {delay} seconds.')
    await asyncio.sleep(delay)
    return msg.upper()

async def main():
    messages = 'hello world apple banana cherry'.split()
    cos = [lazy_greet(m, random.randrange(1, 5)) for m in messages]
    for f in asyncio.as_completed(cos):
        print(await f)

if __name__ == "__main__":
    asyncio.run(main())
