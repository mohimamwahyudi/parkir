from PyQt5 import QtWidgets, uic, QtSql, QtCore,QtGui,QtPrintSupport
import sys
import pyqrcode 
from pyqrcode import QRCode
from PyQt5.QtSql import QSqlTableModel
import data 

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('./desain/tambah.ui', self)
        self.show()
        self.openDB()
        self.tambah.clicked.connect(self.add)
    def openDB(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('parkir.db')
        if not db.open():
            self.cek.setText("connect db error")
            return False
        else:
            self.cek.setText("connect db OK")
    def add(self):
        nim = self.nim.text()
        nama = self.nama.text()
        jurusan = self.jurusan.text()
        nos = self.nos.text()
        nom = self.nom.text()
        query = QtSql.QSqlQuery()
        simpan =  query.exec_("INSERT INTO mahasiswa VALUES ( '%s', '%s', '%s', '%s','%s')" %
                              (''.join(str(nim)),''.join(str(nama)),''.join(str(jurusan)),''.join(str(nos)),''.join(nom)))
        if simpan:
            self.cek.setText("data berhasil di tambah")
            url = pyqrcode.create(nim)
            url.svg("./gambar/"+nim+".svg", scale = 8)
            self.a = data.Ui()
            self.a.show()
            self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
