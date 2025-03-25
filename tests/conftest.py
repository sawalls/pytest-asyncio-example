from asyncio import TaskGroup, sleep
from pytest_asyncio import fixture


@fixture(scope="function")
async def async_buddy():
    mytasks = set()
    async def forever_loop():
        while True:
            await sleep(1)

    async def exception_task():
        await sleep(5)
        raise Exception("This is an exception")

    async with TaskGroup() as tg:
        mytasks.add(tg.create_task(forever_loop()))
        mytasks.add(tg.create_task(exception_task()))
        yield
