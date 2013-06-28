import logging
import math
import time
logger=logging.getLogger()
file=logging.FileHandler(time.strftime('%Y-%m-%d',time.localtime(time.time()))+"_log.log")
logger.addHandler(file)
formatter=logging.Formatter("%(asctime)s %(levelname)s %(message)s")
file.setFormatter(formatter)
logger.setLevel(logging.NOTSET)
for i in range(0,10):
	logger.info(str(i))
