# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Python\SettleDocuments_MH\SplitFileAndModifyFileCreateTime_GUI\MainGUI.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(510, 348)
        Dialog.setSizeGripEnabled(True)
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(70, 130, 331, 31))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.pushButton_SeletFile = QtWidgets.QPushButton(self.splitter)
        self.pushButton_SeletFile.setObjectName("pushButton_SeletFile")
        self.textEdit_DisplaySelectedFilePath = QtWidgets.QTextEdit(self.splitter)
        self.textEdit_DisplaySelectedFilePath.setObjectName("textEdit_DisplaySelectedFilePath")
        self.dateTimeEdit_SelectDate = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit_SelectDate.setGeometry(QtCore.QRect(70, 190, 331, 31))
        self.dateTimeEdit_SelectDate.setObjectName("dateTimeEdit_SelectDate")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_SeletFile.setText(_translate("Dialog", "选择文件"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

