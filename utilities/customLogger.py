import logging
import inspect
from utilities.randomGenerator import Generic_Utilities

class LogGeneration:

    """ customLogger() is used to log the messages/status for required actions and validations """

    random_name_gen = Generic_Utilities.random_genrator()

    @staticmethod
    def customLogger(logLevel=logging.DEBUG):
        """ Set the class/method name from where it is called so we are using inspect module in python
        Get name of current function and caller with Python
        inspect.stack() returns a list with frame records.
        In function whoami(): inspect.stack()[1] is the frame record of the function that calls whoami, like foo() and bar().
        The fourth element of the frame record (inspect.stack()[1][3]) is the function name """

        logger_name = inspect.stack()[1][3]

        ## Create logger
        logger = logging.getLogger(logger_name)

        ## setting level to logger
        logger.setLevel(logLevel)
        ## create console handler or file handler and set the log level
        # fh = logging.FileHandler(".\\Logs\\automation.log", mode='w')
        log_path = ".\\Logs\\"+f"{logger_name}"+"_TestCase_"+f"{LogGeneration.random_name_gen}"+"_Log_File.log"
        # fh = logging.FileHandler(f".\\Logs\\{LogGeneration.random_name_gen}automation.log", mode='a')
        fh = logging.FileHandler(log_path)
        # stream handler used to log messages in console
        ch = logging.StreamHandler()
        ## create formatter - how you want your logs to be formatted
        formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
        ## add formatter to console
        ch.setFormatter(formatter)
        ## add formatter to file handler
        fh.setFormatter(formatter)
        ## add console handler to logger  -- logger is the main thing which logs our messages
        logger.addHandler(ch)
        ## add file handler to logger  -- logger is the main thing which logs our messages
        logger.addHandler(fh)
        ## now return logger
        return logger
        ##application codes -- log messages