from PyQt5 import QtWidgets, uic, QtSql, QtCore,QtGui,QtPrintSupport
import sys
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtPrintSupport import *
import datetime
import pyqrcode 
from pyqrcode import QRCode


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('./desain/tamu.ui', self)
        self.show()
        self.openDB()
        self.tambah.clicked.connect(self.add)
        self.simpan.clicked.connect(self.smp)


    def openDB(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('parkir.db')
        if not db.open():
            self.cek.setText("connect db error")
            return False
        else:
            self.cek.setText("connect db OK")
            return True
    def add(self):
        if self.motor.isChecked():
            time = datetime.datetime.now()
            detik = time.second
            menit = time.minute
            jam = time.hour
            Datenow = ("{}:{}:{}".format(jam, menit, detik))
            no = self.stnk.text()
            jenis = self.motor.text()
            query = QtSql.QSqlQuery()
            simpan =  query.exec_("INSERT INTO tamu VALUES ( '"+no+"', '"+jenis+"', '"+str(Datenow)+"')")
            
                              
            if simpan:
                self.cek.setText("data berhasil di tambah")
                url = pyqrcode.create(no)
                url.svg("./gambar/"+no+".svg", scale = 8)
                cek = QtGui.QPixmap("./gambar/"+no+".svg")
                self.gambar.setPixmap(cek)

        else:
            time = datetime.datetime.now()
            detik = time.second
            menit = time.minute
            jam = time.hour
            Datenow = ("{}:{}:{}".format(jam, menit, detik))
            no = self.stnk.text()
            jenis = self.mobil.text()
            query = QtSql.QSqlQuery()
            simpan =  query.exec_("INSERT INTO tamu VALUES ( '"+no+"', '"+jenis+"','"+str(Datenow)+"')")
            
                              
            if simpan:
                self.cek.setText("data berhasil di tambah")
                url = pyqrcode.create(no)
                url.svg("./gambar/"+no+".svg", scale = 8)
                cek = QtGui.QPixmap("./gambar/"+no+".svg")
                self.gambar.setPixmap(cek)
            
    def smp(self):
          # Create printer
        printer = QtPrintSupport.QPrinter()
        # Create painter
        painter = QtGui.QPainter()
        # Start painter
        painter.begin(printer)
        # Grab a widget you want to print
        screen = self.gambar.grab()
        # Draw grabbed pixmap
        painter.drawPixmap(10, 10, screen)
        # End painting
        painter.end()

                


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
