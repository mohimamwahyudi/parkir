from PyQt5 import QtWidgets, uic, QtSql, QtCore,QtGui,QtPrintSupport
import sys
import pyqrcode 
from pyqrcode import QRCode
from PyQt5.QtSql import QSqlTableModel
import datadosen

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('./desain/tambahdosen.ui', self)
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
        nip = self.nip.text()
        nama = self.nama.text()
        nos = self.nos.text()
        nom = self.nom.text()
        query = QtSql.QSqlQuery()
        simpan = query.exec_("INSERT INTO dosen (nip, nama, motor, mobil) VALUES ('"+nip+"' ,'"+nama+"', '"+nos+"', '"+nom+"')")
        
        if simpan:
            self.cek.setText("data berhasil di tambah")
            url = pyqrcode.create(nip)
            url.svg("./gambar/"+nip+".svg", scale = 8)
            self.a = datadosen.Ui()
            self.a.show()
            self.close()
        else:
            self.cek.setText("data tidak berhasil di tambah")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
