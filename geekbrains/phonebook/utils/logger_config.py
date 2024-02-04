import logging


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    log_format = '%(asctime)s - %(levelname)s - %(name)s : %(message)s'
    log_file_name = 'phonebook.log'

    if not any(isinstance(handler, logging.FileHandler) and handler.baseFilename == log_file_name for handler in logger.handlers):
        file_handler = logging.FileHandler(log_file_name, encoding='utf-8')
        formatter = logging.Formatter(log_format)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
