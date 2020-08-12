import logging

class logGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename='.//Logs'+'//automation.log',format='%(asctime)s: %(levelname)s', datefmt='%m/%s/%y %I:%M:%S %P')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
