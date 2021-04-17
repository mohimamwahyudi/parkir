from PyQt5 import QtWidgets, uic, QtSql, QtCore,QtGui,QtPrintSupport
import sys
from PyQt5.QtSql import QSqlTableModel
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import login


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('./desain/satpam2.ui', self)
        self.model = QSqlTableModel()
        self.show()
        self.openDB()
        self.model = QtSql.QSqlTableModel()
        self.displaytable("")
        self.scan.clicked.connect(self.scaner)
        self.hapus.clicked.connect(self.padam)
        self.logout.clicked.connect(self.keluar)

    def openDB(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('parkir.db')
        if not db.open():
            self.cek.setText("connect db error")
            return False
        else:
            self.cek.setText("connect db OK")
    def displaytable(self, p_filter):
        if p_filter == "":
            self.model.setTable("tamu")
            self.model.setFilter("0")
            self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
            self.model.select()
            self.model.setHeaderData(0, QtCore.Qt.Horizontal, "stnk")
            self.model.setHeaderData(1, QtCore.Qt.Horizontal, "jenis")
            self.model.setHeaderData(2, QtCore.Qt.Horizontal, "status")
            self.model.setHeaderData(3, QtCore.Qt.Horizontal, "masuk")
            self.tableView.setModel(self.model)
        else:
            query = QtSql.QSqlQuery("select * from tamu"
                                    " where stnk like '%"+p_filter +"'")
            self.model.setTable("")
            self.model.setQuery(query)
            self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
            self.model.select()
            self.model.setHeaderData(0, QtCore.Qt.Horizontal, "stnk")
            self.model.setHeaderData(1, QtCore.Qt.Horizontal, "jenis")
            self.model.setHeaderData(2, QtCore.Qt.Horizontal, "status")
            self.model.setHeaderData(3, QtCore.Qt.Horizontal, "masuk")
            self.tableView.setModel(self.model)
    def scaner(self):
        cap = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_PLAIN
        stop = False
        while not stop:
            _, frame = cap.read()

            decodedObjects = pyzbar.decode(frame)
            for obj in decodedObjects:
                a= obj.data.decode("utf-8")
                self.displaytable(a)
                cv2.putText(frame, str(obj.data), (50, 50), font, 2,
                            (255, 0, 0), 3)
                stop = True
                

            cv2.imshow("Frame", frame)
            
            
            key = cv2.waitKey(1)
            
            if key == 27:
                break
        cap.release()
        cv2.destroyAllWindows()
    def padam(self):
        self.model.removeRow(self.tableView.currentIndex().row())
        self.displaytable("")
    def keluar(self):
        self.b= login.Ui()
        self.b.show()
        self.close()
    
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
