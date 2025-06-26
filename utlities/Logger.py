import logging
import inspect


class loggerClass:

    @staticmethod
    def getLogger():
        logger_name = inspect.stack()[1][3] # your task
        logger = logging.getLogger(logger_name)
        logfile = logging.FileHandler(".\\Logs\\automation.log")
        log_format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s -->  %(message)s")
        logfile.setFormatter(log_format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger


