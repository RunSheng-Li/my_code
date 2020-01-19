"""
日志级别
日志一共分为5个等级，从低到高分别是：
DEBUG：详细的信息，通常只出现在诊断问题上
INFO：确认一切按预期运行
WARNING：一个迹象表明，一些意想不到的事情发生了，或表明一些问题在不久的将来。（例如：磁盘空间低）。这个软件还能按预期工作
ERROR：更严重的问题，软件没能执行一些功能
CRITICAL：一个严重的错误，这表明程序本身可能无法继续运行

"""
import logging

# 第一步，创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# 第二步，创建一个handler,用于写入日志文件
logfile = 'log.log'
fh = logging.FileHandler(logfile, mode='a')
# 输出到file的log等级开关
fh.setLevel(logging.DEBUG)

# 第三步，再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
# 输出到console的log等级的开关
ch.setLevel(logging.WARNING)

# 第四步，定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 第五步，将logger添加到handler里面
logger.addHandler(fh)
logger.addHandler(ch)

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
