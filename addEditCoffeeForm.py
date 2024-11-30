import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow
from addEditCoffeeFormUI import Ui_MainWindow


class AddEditCoffeForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, id=None, name='', roast='', molot='', descr='', price='', v=''):
        super().__init__(parent)
        self.id = id
        self.setupUi(self)
        self.nameEdit.setText(name)
        self.roastEdit.setText(roast)
        self.molotEdit.setText(molot)
        self.descrEdit.setText(descr)
        self.priceEdit.setText(str(price))
        self.VEdit.setText(str(v))
        self.pushButton.clicked.connect(self.save)

    def save(self):
        try:
            con = sqlite3.connect('coffee.sqlite')
            cur = con.cursor()
            if self.id:
                query = """UPDATE coffee SET name=?, roast=?, molat_zern=?, descr=?, price=?, v=? WHERE id=?"""
                params = (self.nameEdit.text(), self.roastEdit.text(), self.molotEdit.text(), self.descrEdit.text(),
                          int(self.priceEdit.text()), self.VEdit.text(), self.id)
            else:
                query = """INSERT INTO coffee (name, roast, molat_zern, descr, price, v) VALUES(?, ?, ?, ?, ?, ?)"""
                params = (self.nameEdit.text(), self.roastEdit.text(), self.molotEdit.text(), self.descrEdit.text(),
                          int(self.priceEdit.text()), float(self.VEdit.text()))
            cur.execute(query, params)
            con.commit()
            cur.close()
            con.close()
            self.parent().run()
            self.close()
        except Exception as e:
            print(e)
            self.statusbar.showMessage('что-то не так')


def except_hook(cls, exeption, traceback):
    sys.__excepthook__(cls, exeption, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddEditCoffeForm()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
