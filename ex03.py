#  DeprecationWarning: The explicit passing of coroutine objects to asyncio.wait() is deprecated since Python 3.8,
#  and scheduled for removal in Python 3.11.


import asyncio
import random
async def lazy_greet(msg, delay=1):
    print(f'{msg!r} will be displayed in {delay} seconds.')
    await asyncio.sleep(delay)
    return msg.upper()
async def main():
    messages = 'hello world apple banana cherry'.split()
    cos = [lazy_greet(m, random.randrange(1, 5)) for m in messages]
    (done, pending) = await asyncio.wait(cos, timeout=2)
    if pending:
        print("there is {} tasks not completed".format(len(pending)))
        for f in pending:
            f.cancel()
    for f in done:
        print(await f)


if __name__ == "__main__":
    asyncio.run(main())