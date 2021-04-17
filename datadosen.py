from PyQt5 import QtWidgets, uic, QtSql, QtCore,QtGui,QtPrintSupport
import sys
import pyqrcode 
from pyqrcode import QRCode
from PyQt5.QtSql import QSqlTableModel
import tambahmhs
import datastpm
import admin
import login
import data 

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('./desain/datamhs.ui', self)
        self.model = QSqlTableModel()
        self.show()
        self.openDB()
        self.model = QtSql.QSqlTableModel()
        self.displaytable("")
        self.tambah.clicked.connect(self.add)
        self.satpam.clicked.connect(self.stm)
        self.hapus.clicked.connect(self.padam)
        self.mencari.textChanged.connect(self.caridata)
        self.admin.clicked.connect(self.masukadmin)
        self.logout.clicked.connect(self.keluar)
        self.mahasiswa.clicked.connect(self.mhs)
        self.dosen.setStyleSheet('background-color : rgb(171, 208, 255);')

        
        
    def openDB(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('parkir.db')
        if not db.open():
            self.cek.setText("connect db error")
            return False
        else:
            self.cek.setText("connect db OK")
            return True
    def displaytable(self, p_filter):
        if p_filter is "":
            self.model.setTable('dosen')
            query = QtSql.QSqlQuery("select * from dosen")
            self.model.setQuery(query)
            self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
            self.model.select()
            self.model.setHeaderData(0, QtCore.Qt.Horizontal, "nim")
            self.model.setHeaderData(1, QtCore.Qt.Horizontal, "nama")
            self.model.setHeaderData(2, QtCore.Qt.Horizontal, "no sepeda")
            self.model.setHeaderData(3, QtCore.Qt.Horizontal, "no mobil")
            self.tableView.setModel(self.model)
        else:
            query = QtSql.QSqlQuery("select * from dosen"
                                    " where nip like '%"+p_filter + "%' OR nama like '%"+p_filter + "%' ")
            self.model.setTable("")
            self.model.setQuery(query)
            self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
            self.model.select()
            self.model.setHeaderData(0, QtCore.Qt.Horizontal, "nim")
            self.model.setHeaderData(1, QtCore.Qt.Horizontal, "nama")
            self.model.setHeaderData(2, QtCore.Qt.Horizontal, "no sepeda")
            self.model.setHeaderData(3, QtCore.Qt.Horizontal, "no mobil")
            self.tableView.setModel(self.model)
    def add(self):
        self.a = tambahmhs.Ui()
        self.a.show
        self.close()
     
    def stm(self):
        self.a = datastpm.Ui()
        self.a.show()
        self.close()

    def padam(self):
        self.model.removeRow(self.tableView.currentIndex().row())
        self.displaytable("")     
    def caridata(self):
        kata = self.sender().text()
        self.displaytable(kata)
    def masukadmin(self):
        self.b= admin.Ui()
        self.b.show()
        self.close()
    def keluar(self):
        self.b= login.Ui()
        self.b.show()
        self.close()
    def mhs(self):
        self.a = data.Ui()
        self.a.show()
        self.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
 
