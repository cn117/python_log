import logging
import logging.config
import time

logging.config.fileConfig('log.conf')
logger = logging.getLogger('key2')  
for i in range(0, 10):
    try:
        logger.debug('debug msg')
        logger.info('info msg')
        logger.warning('warning msg')
        num = int('abc')
    except:
        logger.error('error msg')
        logger.exception('exception strace')  

   # time.sleep(2)
# end for
