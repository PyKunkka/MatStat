# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1315, 635)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(390, 10, 411, 281))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(860, 20, 401, 271))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.pushBtn_make_hist = QtWidgets.QPushButton(self.centralwidget)
        self.pushBtn_make_hist.setGeometry(QtCore.QRect(530, 310, 121, 23))
        self.pushBtn_make_hist.setObjectName("pushBtn_make_hist")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1010, 310, 121, 23))
        self.pushButton.setObjectName("pushButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(320, 0, 20, 351))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(7, 340, 1301, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.tableWidget_Loaded_data_from_file = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_Loaded_data_from_file.setGeometry(QtCore.QRect(10, 10, 311, 331))
        self.tableWidget_Loaded_data_from_file.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_Loaded_data_from_file.setRowCount(2)
        self.tableWidget_Loaded_data_from_file.setColumnCount(3)
        self.tableWidget_Loaded_data_from_file.setObjectName("tableWidget_Loaded_data_from_file")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Loaded_data_from_file.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Loaded_data_from_file.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Loaded_data_from_file.setHorizontalHeaderItem(2, item)
        self.tableWidget_Loaded_data_from_file.horizontalHeader().setDefaultSectionSize(97)
        self.tableWidget_Chisl_haract = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_Chisl_haract.setGeometry(QtCore.QRect(10, 360, 761, 231))
        self.tableWidget_Chisl_haract.setRowCount(18)
        self.tableWidget_Chisl_haract.setColumnCount(4)
        self.tableWidget_Chisl_haract.setObjectName("tableWidget_Chisl_haract")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Chisl_haract.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Chisl_haract.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Chisl_haract.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Chisl_haract.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setItalic(False)
        item.setFont(font)
        self.tableWidget_Chisl_haract.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Chisl_haract.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Chisl_haract.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Chisl_haract.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Chisl_haract.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Chisl_haract.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Chisl_haract.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Chisl_haract.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Chisl_haract.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Chisl_haract.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Chisl_haract.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Chisl_haract.setItem(11, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Chisl_haract.setItem(12, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Chisl_haract.setItem(13, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Chisl_haract.setItem(14, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Chisl_haract.setItem(15, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Chisl_haract.setItem(16, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Chisl_haract.setItem(17, 0, item)
        self.tableWidget_Chisl_haract.horizontalHeader().setDefaultSectionSize(200)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(780, 350, 16, 261))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.checkBox_loharifm = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_loharifm.setGeometry(QtCore.QRect(830, 370, 111, 17))
        self.checkBox_loharifm.setObjectName("checkBox_loharifm")
        self.checkBox_standartizaciya = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_standartizaciya.setGeometry(QtCore.QRect(830, 400, 111, 17))
        self.checkBox_standartizaciya.setObjectName("checkBox_standartizaciya")
        self.checkBox_back_to_start = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_back_to_start.setGeometry(QtCore.QRect(830, 430, 171, 17))
        self.checkBox_back_to_start.setObjectName("checkBox_back_to_start")
        self.checkBox_clear_graphs = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_clear_graphs.setGeometry(QtCore.QRect(830, 460, 101, 17))
        self.checkBox_clear_graphs.setObjectName("checkBox_clear_graphs")
        self.pushButton_chec_box_run = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_chec_box_run.setGeometry(QtCore.QRect(860, 560, 75, 23))
        self.pushButton_chec_box_run.setObjectName("pushButton_chec_box_run")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(1000, 350, 20, 251))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.lineEdit_take_alpha = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_take_alpha.setGeometry(QtCore.QRect(1030, 410, 113, 21))
        self.lineEdit_take_alpha.setObjectName("lineEdit_take_alpha")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1160, 410, 91, 21))
        self.label.setObjectName("label")
        self.countClasses = QtWidgets.QLineEdit(self.centralwidget)
        self.countClasses.setGeometry(QtCore.QRect(1030, 370, 113, 20))
        self.countClasses.setObjectName("countClasses")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1160, 370, 81, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1315, 21))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Tools = QtWidgets.QMenu(self.menubar)
        self.menu_Tools.setObjectName("menu_Tools")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        self.menuAbout = QtWidgets.QMenu(self.menu_Help)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout_software = QtWidgets.QAction(MainWindow)
        self.actionAbout_software.setObjectName("actionAbout_software")
        self.actionAbout_developer = QtWidgets.QAction(MainWindow)
        self.actionAbout_developer.setObjectName("actionAbout_developer")
        self.menu_File.addAction(self.actionOpen)
        self.menu_File.addAction(self.actionSave)
        self.menu_File.addAction(self.actionExit)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionAbout_software)
        self.menuAbout.addAction(self.actionAbout_developer)
        self.menu_Help.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Tools.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Робота з даними"))
        self.pushBtn_make_hist.setText(_translate("MainWindow", "Гістограма"))
        self.pushButton.setText(_translate("MainWindow", "Функція розподілу"))
        item = self.tableWidget_Loaded_data_from_file.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "X, Дані"))
        item = self.tableWidget_Loaded_data_from_file.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "N, Кількість"))
        item = self.tableWidget_Loaded_data_from_file.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "P, Ймовірність"))
        item = self.tableWidget_Chisl_haract.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Величини"))
        item = self.tableWidget_Chisl_haract.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Нижня оцінка"))
        item = self.tableWidget_Chisl_haract.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Оцінка"))
        item = self.tableWidget_Chisl_haract.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Верхня оцінка"))
        __sortingEnabled = self.tableWidget_Chisl_haract.isSortingEnabled()
        self.tableWidget_Chisl_haract.setSortingEnabled(False)
        item = self.tableWidget_Chisl_haract.item(1, 0)
        item.setText(_translate("MainWindow", "Середнє арефметичне"))
        item = self.tableWidget_Chisl_haract.item(2, 0)
        item.setText(_translate("MainWindow", " Усічене середнє"))
        item = self.tableWidget_Chisl_haract.item(3, 0)
        item.setText(_translate("MainWindow", "Медіана"))
        item = self.tableWidget_Chisl_haract.item(4, 0)
        item.setText(_translate("MainWindow", "Медіана середніх Уолша"))
        item = self.tableWidget_Chisl_haract.item(5, 0)
        item.setText(_translate("MainWindow", "МАД"))
        item = self.tableWidget_Chisl_haract.item(6, 0)
        item.setText(_translate("MainWindow", "Незсунена дисперсія"))
        item = self.tableWidget_Chisl_haract.item(7, 0)
        item.setText(_translate("MainWindow", "Зсунена дисперсія"))
        item = self.tableWidget_Chisl_haract.item(8, 0)
        item.setText(_translate("MainWindow", "Незс. Сер. квад. відхилення"))
        item = self.tableWidget_Chisl_haract.item(9, 0)
        item.setText(_translate("MainWindow", "Зсунене сер. квад. відхилення"))
        item = self.tableWidget_Chisl_haract.item(10, 0)
        item.setText(_translate("MainWindow", "Коеф. асиметрії"))
        item = self.tableWidget_Chisl_haract.item(11, 0)
        item.setText(_translate("MainWindow", "Коеф. асиметрії зсунений"))
        item = self.tableWidget_Chisl_haract.item(12, 0)
        item.setText(_translate("MainWindow", "Коефіцієнт ексцесу, зсунений"))
        item = self.tableWidget_Chisl_haract.item(13, 0)
        item.setText(_translate("MainWindow", "Коефіцієнт ексцесу, незсунений"))
        item = self.tableWidget_Chisl_haract.item(14, 0)
        item.setText(_translate("MainWindow", "Коефіцієнт контрексцесу"))
        item = self.tableWidget_Chisl_haract.item(15, 0)
        item.setText(_translate("MainWindow", "Коефіцієнт варіації Пірсона"))
        item = self.tableWidget_Chisl_haract.item(16, 0)
        item.setText(_translate("MainWindow", "Мінімум"))
        item = self.tableWidget_Chisl_haract.item(17, 0)
        item.setText(_translate("MainWindow", "Максимум"))
        self.tableWidget_Chisl_haract.setSortingEnabled(__sortingEnabled)
        self.checkBox_loharifm.setText(_translate("MainWindow", "Логарифмування"))
        self.checkBox_standartizaciya.setText(_translate("MainWindow", "Стандартизація"))
        self.checkBox_back_to_start.setText(_translate("MainWindow", "Повернутись до початкового"))
        self.checkBox_clear_graphs.setText(_translate("MainWindow", "Очистити сітки"))
        self.pushButton_chec_box_run.setText(_translate("MainWindow", "Відтворити"))
        self.label.setText(_translate("MainWindow", "Альфа значення"))
        self.label_2.setText(_translate("MainWindow", "Кількість класів"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_Tools.setTitle(_translate("MainWindow", "&Tools"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout_software.setText(_translate("MainWindow", "About software"))
        self.actionAbout_developer.setText(_translate("MainWindow", "About developer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
