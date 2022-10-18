from asyncio.log import logger


for i in range(5):
    logger.info('info')
    print(f'hello {i}')
