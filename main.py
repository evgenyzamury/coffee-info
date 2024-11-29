import sys
import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from mainUI import Ui_MainWindow


class СoffeeApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.run()

    def run(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        query = """SELECT
            *
        FROM
            coffee"""
        result = cur.execute(query).fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        for i, line in enumerate(result):
            for j, elem in enumerate(line):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))


def except_hook(cls, exeption, traceback):
    sys.__excepthook__(cls, exeption, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = СoffeeApp()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
