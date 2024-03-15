'''Create a log file and command line logs at the same time'''
import logging
from logging import StreamHandler


def config_log():
    '''configure the log generator'''
    # Configure the logging module
    logging.basicConfig(filename='server.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Console (stream) handler
    console_handler = StreamHandler()
    console_handler.setFormatter(log_format)
    console_handler.setLevel(logging.INFO)

    # Add both handlers to the root logger
    logging.getLogger().addHandler(console_handler)
