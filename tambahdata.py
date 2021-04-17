from PyQt5 import QtWidgets, uic, QtSql, QtCore,QtGui,QtPrintSupport
import sys
from PyQt5.QtSql import QSqlTableModel
import admin 

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('./desain/form.ui', self)
        self.show()
        self.openDB()
        self.tambah.clicked.connect(self.tambahadmin)
    def openDB(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('parkir.db')
        if not db.open():
            self.cek.setText("connect db error")
            return False
        else:
            self.cek.setText("connect db OK")
    def tambahadmin(self):
         use = self.username.text()
         pas = self.password.text()
         query = QtSql.QSqlQuery()
         simpan =  query.exec_("INSERT INTO admin VALUES ( '%s', '%s')" %(''.join(str(use)),''.join(str(pas))))
         if simpan:
             self.a= admin.Ui()
             self.a.show()
             self.close()
    


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
