# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OpenAES.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import pyperclip
from lib import encryption


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(913, 532)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 30, 141, 21))
        self.label_2.setObjectName("label_2")
        self.key = QtWidgets.QLineEdit(self.centralwidget)
        self.key.setGeometry(QtCore.QRect(46, 250, 651, 31))
        self.key.setText("")
        self.key.setObjectName("key")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 250, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 150, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.copy_key = QtWidgets.QPushButton(self.centralwidget)
        self.copy_key.setGeometry(QtCore.QRect(826, 250, 75, 31))
        self.copy_key.setObjectName("copy_key")
        self.mode = QtWidgets.QComboBox(self.centralwidget)
        self.mode.setGeometry(QtCore.QRect(60, 150, 81, 31))
        self.mode.setObjectName("mode")
        self.mode.addItem("")
        self.mode.addItem("")
        self.choose_file = QtWidgets.QPushButton(self.centralwidget)
        self.choose_file.setGeometry(QtCore.QRect(10, 320, 131, 41))
        self.choose_file.setObjectName("choose_file")
        self.encrypt_btn = QtWidgets.QPushButton(self.centralwidget)
        self.encrypt_btn.setGeometry(QtCore.QRect(10, 470, 131, 41))
        self.encrypt_btn.setObjectName("encrypt_btn")
        self.output_name = QtWidgets.QLineEdit(self.centralwidget)
        self.output_name.setGeometry(QtCore.QRect(140, 370, 681, 41))
        self.output_name.setText("")
        self.output_name.setObjectName("output_name")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 370, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.copy_output_filename = QtWidgets.QPushButton(self.centralwidget)
        self.copy_output_filename.setGeometry(QtCore.QRect(830, 370, 75, 41))
        self.copy_output_filename.setObjectName("copy_output_filename")
        self.generate_key = QtWidgets.QPushButton(self.centralwidget)
        self.generate_key.setGeometry(QtCore.QRect(700, 250, 121, 31))
        self.generate_key.setObjectName("generate_key")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 110, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.algo = QtWidgets.QComboBox(self.centralwidget)
        self.algo.setGeometry(QtCore.QRect(80, 110, 81, 31))
        self.algo.setObjectName("algo")
        self.algo.addItem("")
        self.algo.addItem("")
        self.output_location = QtWidgets.QPushButton(self.centralwidget)
        self.output_location.setGeometry(QtCore.QRect(150, 320, 171, 41))
        self.output_location.setObjectName("output_location")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 913, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.input_file = None
        self.output_folder = None

        self.choose_file.clicked.connect(self.open_file)
        self.output_location.clicked.connect(self.choose_folder)
        
        self.encrypt_btn.clicked.connect(lambda: self.start(self.input_file, self.output_folder, self.output_name))

        self.copy_key.clicked.connect(lambda: self.copy(self.key))
        self.copy_output_filename.clicked.connect(lambda: self.copy(self.output_name))
        
        self.generate_key.clicked.connect(self.get_key)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "File Locker"))
        self.label.setText(_translate("MainWindow", "File Locker"))
        self.label_2.setText(_translate("MainWindow", "By Anti Government"))
        self.label_8.setText(_translate("MainWindow", "Key:"))
        self.label_9.setText(_translate("MainWindow", "Mode:"))
        self.copy_key.setText(_translate("MainWindow", "Copy"))
        self.mode.setItemText(0, _translate("MainWindow", "Encrypt"))
        self.mode.setItemText(1, _translate("MainWindow", "Decrypt"))
        self.choose_file.setText(_translate("MainWindow", "Choose file"))
        self.encrypt_btn.setText(_translate("MainWindow", "Start"))
        self.label_10.setText(_translate("MainWindow", "Output file name:"))
        self.copy_output_filename.setText(_translate("MainWindow", "Copy"))
        self.generate_key.setText(_translate("MainWindow", "Use random key"))
        self.label_11.setText(_translate("MainWindow", "Algorithm:"))
        self.algo.setItemText(0, _translate("MainWindow", "AES-256"))
        self.algo.setItemText(1, _translate("MainWindow", "DES"))
        self.output_location.setText(_translate("MainWindow", "Choose output file location"))
    
    def get_key(self):
        algo = encryption.algorithms[self.get_current_item(self.algo)]
        
        key = algo['get_key'](algo['length'])
        
        self.key.setText(str(key))
    

    def copy(self, obj):
        pyperclip.copy(obj.text())
    
    def open_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        
        filename, _ = QFileDialog.getOpenFileName(None, "Select which file to encrypt", "", "All Files (*);;Python Files (*.py)", options=options)
        
        self.input_file = filename

        return filename
    
    def choose_folder(self):
        foldername = QFileDialog.getExistingDirectory(None, "Select output directory")
        
        self.output_folder = foldername

        return foldername
    
    def show_popup(self, title, text, icon, detailed_text):
        msg = QMessageBox()

        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(icon)

        msg.setStandardButtons(QMessageBox.Ok)

        msg.setDetailedText(detailed_text)

        msg.exec_()
    
    def get_current_item(self, combobox):
        return combobox.currentText()
    
    def start(self, input_file, output_path, output_filename):
        algos = encryption.algorithms

        output_path = output_path + '/' + output_filename.text()

        try:
            algos[self.get_current_item(self.algo)][self.get_current_item(self.mode)](input_file, output_path, self.key.text())

        except Exception as exc:
            self.show_popup('An error occoured', 'An error occoured.', QMessageBox.Critical, str(exc))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
