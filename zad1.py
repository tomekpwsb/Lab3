import logging

def create_log(logLvl, message):
    logging.basicConfig(filename='example.log', encoding='utf-8', level=logLvl, format='%(asctime)s: %(levelname)s, %(message)s', datefmt='%m/%d/%Y %H:%M:%S')

    match logLvl:
        case logging.DEBUG:
            logging.debug(message)
        case logging.WARNING:
            logging.warning(message)
        case logging.ERROR:
            logging.error(message)
        case logging.CRITICAL:
            logging.critical(message)
        case _:
            logging.info(message)

create_log(logging.INFO, 'test')