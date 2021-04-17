from PyQt5 import QtWidgets, uic, QtSql, QtCore,QtGui,QtPrintSupport
import sys
from PyQt5.QtSql import QSqlTableModel
import datastpm
import data
import tambahdata
import login
import datadosen

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('./desain/admin.ui', self)
        self.model = QSqlTableModel()
        self.show()
        self.openDB()
        self.model = QtSql.QSqlTableModel()
        self.displaytable("")
        self.hapus.clicked.connect(self.padam)
        self.admin.setStyleSheet('background-color : rgb(171, 208, 255);')
        self.satpam.clicked.connect(self.stm)
        self.mahasiswa.clicked.connect(self.mhs)
        self.tambah.clicked.connect(self.tambahs)
        self.logout.clicked.connect(self.keluar)
        self.dosen.clicked.connect(self.dtdosen)
        
    def openDB(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('parkir.db')
        if not db.open():
            self.cek.setText("connect db error")
            return False
        else:
            self.cek.setText("connect db OK")
    def displaytable(self, p_filter):
        if p_filter is "":
            self.model.setTable('admin')
            query = QtSql.QSqlQuery("select * from admin")
            self.model.setQuery(query)
            self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
            self.model.select()
            self.model.setHeaderData(0, QtCore.Qt.Horizontal, "username")
            self.model.setHeaderData(1, QtCore.Qt.Horizontal, "password")
            self.tableView.setModel(self.model)
        else:
            query = QtSql.QSqlQuery("select * from admin"
                                    " where nim username '%"+p_filter + "' OR nama like '%"+p_filter + "%' ")
            self.model.setTable("")
            self.model.setQuery(query)
            self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
            self.model.select()
            self.model.setHeaderData(0, QtCore.Qt.Horizontal, "username")
            self.model.setHeaderData(1, QtCore.Qt.Horizontal, "password")
            self.tableView.setModel(self.model)
        

    def padam(self):
        self.model.removeRow(self.tableView.currentIndex().row())
        self.displaytable("")
    def stm(self):
        self.a = datastpm.Ui()
        self.a.show()
        self.close()
    def mhs(self):
        self.b = data.Ui()
        self.b.show()
        self.close()

    def tambahs(self):
        self.c = tambahdata.Ui()
        self.c.show()
        self.close()
    def keluar(self):
        self.b= login.Ui()
        self.b.show()
        self.close()
    def dtdosen(self):
        self.c = datadosen.Ui()
        self.c.show()
        self.close()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
