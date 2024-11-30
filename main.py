import sys
import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from addEditCoffeeForm import AddEditCoffeForm
from mainUI import Ui_MainWindow


class СoffeeApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.run()
        self.add_btn.clicked.connect(self.add)
        self.edit_btn.clicked.connect(self.edit)

    def run(self):
        self.tableWidget.clear()
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
        cur.close()
        con.close()

    def add(self):
        self.add_form = AddEditCoffeForm(self)
        self.add_form.show()

    def edit(self):
        id = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        query = """SELECT
                    *
                FROM
                    coffee
                WHERE id=?"""
        result = cur.execute(query, (id,)).fetchone()
        print(result)
        self.add_form = AddEditCoffeForm(self, id=id, name=result[1], roast=result[2], molot=result[3], descr=result[4],
                                         price=result[5], v=result[6])
        self.add_form.show()
        # self.red_form = AddEditCoffeForm(self)
        # self.red_form.show()


def except_hook(cls, exeption, traceback):
    sys.__excepthook__(cls, exeption, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = СoffeeApp()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
