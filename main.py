import json
import logging
import platform
import sys

from PyQt5.QtWidgets import QApplication
from assistant.gui import GUI
from assistant.hannah3_0setup import hannah3_0setup


def read_json():
    logging.info('Reading configuration data.')
    # Reading data file
    with open('config/config.json') as file:
        return json.load(file)


if __name__ == '__main__':
    operating_system = platform.uname().system
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s:%(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    hannah3_0setup = hannah3_0setup(logger=logging, config=read_json(), os_name=operating_system)

    app = QApplication(sys.argv)
    gui = GUI()

    hannah3_0setup.start()
    gui.start()

    app.exit(app.exec_())
