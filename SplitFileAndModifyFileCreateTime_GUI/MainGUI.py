# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
import sys
from PyQt5.QtCore import pyqtSlot, QPoint
from PyQt5.QtWidgets import QDialog
from Ui_MainGUI import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QAction, QFileDialog,  QTextEdit  
import os

class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot(QPoint)
    def on_splitter_customContextMenuRequested(self, pos):
        """
        Slot documentation goes here.
        
        @param pos DESCRIPTION
        @type QPoint
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot(bool)
    def on_textEdit_DisplaySelectedFilePath_copyAvailable(self, b):
        """
        Slot documentation goes here.
        
        @param b DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        # pass
        print("TNWZ->",b)
    
    @pyqtSlot()
    def on_pushButton_SeletFile_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        filename, tmp= QFileDialog.getOpenFileName(self, 'Open file', './', "txt files (*.txt)")  
        if filename:  
            # filePath = self.FilePath.text()
            print(filename)
            print(tmp)
            self.textEdit_DisplaySelectedFilePath.setText(filename)
    
    @pyqtSlot(QPoint)
    def on_dateTimeEdit_SelectDate_customContextMenuRequested(self, pos):
        """
        Slot documentation goes here.
        
        @param pos DESCRIPTION
        @type QPoint
        """
        # TODO: not implemented yet
        raise NotImplementedError
if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    Dialog = Dialog()
    # ui = Ui_Dialog()
    # ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
