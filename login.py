from PyQt5 import QtWidgets, uic, QtSql, QtCore,QtGui
import sys
import data
import satpam
import satpam2

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('./desain/login.ui', self)
        self.show()
        self.openDB()
        self.masuk.clicked.connect(self.ceklogin)
        self.lihat.clicked.connect(self.lihatp)


        
    def openDB(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('parkir.db')
        if not db.open():
            self.cek.setText("connect db error")
            return False
        else:
            self.cek.setText("connect db OK")

    def ceklogin(self):
        username = self.username.text()
        password = self.password.text()
        query = QtSql.QSqlQuery()
        if username !='' and password !='':
            query.exec_("SELECT * FROM admin WHERE username='"+username+"' AND password='"+password+"'")
            if query.next():
                self.b = data.Ui()
                self.b.show()
                self.close()
            elif not query.next() :
                query.exec_("SELECT * FROM satpam WHERE username='"+username+"' AND password='"+password+"'")
                if query.next():
                    if query.record().value(0)=='satpam1' or query.record().value(0)=='satpam2':
                        self.c = satpam.Ui()
                        self.c.show()
                        self.close()
                    else:
                        print("a")
                        self.e = satpam2.Ui()
                        self.e.show()
                        self.close()
                else:
                    self.cek2.setText("username atau password salah ")
                
    def lihatp(self):
        if self.lihat.isChecked() == True:
            self.password.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.password.setEchoMode(QtWidgets.QLineEdit.Password)
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
