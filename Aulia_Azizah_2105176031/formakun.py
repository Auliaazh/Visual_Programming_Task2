# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import image_rc, sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1245, 818)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(-31, -11, 1281, 831))
        self.frame.setStyleSheet("background : #ffffff")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(120, 170, 291, 141))
        self.label.setStyleSheet("font-size : 30px;\n"
"font-weight : bold;\n"
"background : none;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(120, 210, 391, 141))
        self.label_2.setStyleSheet("font-size : 20px;\n"
"background : none;\n"
"")
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(120, 320, 401, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setStyleSheet("border : none;\n"
"border-bottom : 1px solid;")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setStyleSheet("border : none;\n"
"border-bottom : 1px solid;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setStyleSheet("border : none;\n"
"border-bottom : 1px solid;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setStyleSheet("border : none;\n"
"border-bottom : 1px solid;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(150, 600, 341, 41))
        self.pushButton.setStyleSheet("border-radius : 10px;\n"
"background-color: rgba(92, 138, 138,0.5);\n"
"font-size : 18px;\n"
"font-weight :200px;")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(230, 660, 131, 31))
        self.label_3.setStyleSheet("font-size :13px;\n"
"background :none;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(350, 660, 131, 31))
        self.label_4.setStyleSheet("font-size :13px;\n"
"background :none;\n"
"color : blue;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(240, 730, 171, 61))
        self.label_5.setStyleSheet("font-size : 15px;\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(120, 10, 401, 181))
        self.label_7.setStyleSheet("image: url(:/img/2.jpg);\n"
"background :none;")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(250, 120, 291, 141))
        self.label_8.setStyleSheet("font-size : 20px;\n"
"font-weight : bold;\n"
"background : none;\n"
"font-style : italic")
        self.label_8.setObjectName("label_8")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(570, 10, 711, 821))
        self.frame_2.setStyleSheet("background : rgba(92, 138, 138,0.5);\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(40, 40, 651, 351))
        self.label_6.setStyleSheet("image: url(:/img/1.jpg);\n"
"background :none;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_17 = QtWidgets.QLabel(self.frame_2)
        self.label_17.setGeometry(QtCore.QRect(50, 240, 651, 531))
        self.label_17.setStyleSheet("image: url(:/img/png-clipart-make-up-cartoon-bijin-illustration-painted-eyeliner-makeup-watercolor-painting-comics-removebg-preview.png);\n"
"background :none;")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.frame_2.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.verticalLayoutWidget.raise_()
        self.pushButton.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_7.raise_()
        self.label_8.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Pendaftaran Akun"))
        self.label_2.setText(_translate("Form", "Silahkan Isi Form Ini untuk Mendaftar Akun"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Nama Lengkap"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Email"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "Password"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Konfirmasi Password"))
        self.pushButton.setText(_translate("Form", "Daftar"))
        self.label_3.setText(_translate("Form", "Sudah Punya Akun?"))
        self.label_4.setText(_translate("Form", "Log In"))
        self.label_5.setText(_translate("Form", "By : Aulia Azizah"))
        self.label_8.setText(_translate("Form", "MODENOWLY"))
import image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())