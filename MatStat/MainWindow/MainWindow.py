from PyQt5 import QtGui, QtWidgets, QtCore
from MatStat.MainWindow.QtMainWindow import Ui_MainWindow
import sys
import numpy as np
from MatStat.Funct_calc_characteristics import CyslChar


class MainWindow(Ui_MainWindow, QtWidgets.QMainWindow, CyslChar):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.fileDialog = QtWidgets.QFileDialog(self)

    def setupUi(self, parent):
        super(MainWindow, self).setupUi(parent)
        self.actionOpen.triggered.connect(self.actionOpenSlot)
        self.actionExit.triggered.connect(self.actionExitSlot)
        self.pushBtn_make_hist.clicked.connect(self.btn_hist_clicked)
        self.pushButton.clicked.connect(self.btn_emp_clicked)

    def btn_hist_clicked(self):
        pass

    def btn_emp_clicked(self):
        pass

    @QtCore.pyqtSlot()
    def actionExitSlot(self):
        sys.exit(0)

    @QtCore.pyqtSlot()
    def actionOpenSlot(self, *args, **kwargs):
        name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "", ".", "All Files(*);;")
        f = open(name, 'r')
        list_data = [float(line.strip('\n').replace(' ', '').replace(',', '.')) for line in f]
        data = np.array(list_data)
        data = np.sort(data)

        self.tableWidget_Loaded_data_from_file.setRowCount(len(data))

        for i in range(0, len(data)):
            self.tableWidget_Loaded_data_from_file.setItem(
                i, 0, QtWidgets.QTableWidgetItem(str(data[i])))
            self.tableWidget_Loaded_data_from_file.setItem(
                i, 1, QtWidgets.QTableWidgetItem(str(list_data.count(data[i]))))
            self.tableWidget_Loaded_data_from_file.setItem(
                i, 2, QtWidgets.QTableWidgetItem(str(list_data.count(data[i])/len(data))))

        med = self.med(list_data)  # Медіана
        mean = self.mean_data(list_data)  # середнє значення вибірки
        mad = self.mad(med)  # MAД
        disp = self.disp(list_data, mean)  # дисперсія, незсунена
        disp_z = self.disp_z(list_data, mean)  # зсунена дисперсія
        sigma = np.sqrt(disp)  # Незсунене сер. квад.
        sigma_z = np.sqrt(disp_z)  # зсунене сер. квад.
        cof_asim = self.coef_asim(list_data, np.sqrt(disp_z), mean)  # коефіцієнт асиметрії
        cof_asim_z = self.coef_asim_zcun(np.shape(list_data)[0], cof_asim)  # коефіцієнт асиметрії, зсунений
        cof_ecsc_z = self.coef_ecsces_z(sigma_z, list_data, mean)  # Коеф. ексцесу
        cof_ecsc = self.coef_ecsces(cof_ecsc_z, np.shape(list_data)[0])

        self.tableWidget_Chisl_haract.setItem(1, 1, QtWidgets.QTableWidgetItem(
            str(self.mean_confidence_interval_lower(mean, np.sqrt(disp), np.shape(list_data)[0]))))  # Нижня оцінка сер.
        self.tableWidget_Chisl_haract.setItem(1, 2, QtWidgets.QTableWidgetItem(str(mean)))  # Середнє вибірки
        self.tableWidget_Chisl_haract.setItem(1, 3, QtWidgets.QTableWidgetItem(
            str(self.mean_confidence_interval_upper(mean, np.sqrt(disp), np.shape(list_data)[0]))))  # Верхня оцінка сер

        self.tableWidget_Chisl_haract.setItem(3, 2, QtWidgets.QTableWidgetItem(str(med)))  # Медіана
        self.tableWidget_Chisl_haract.setItem(4, 2, QtWidgets.QTableWidgetItem(str(self.med_Uol(list_data))))  # Мед.Уол
        self.tableWidget_Chisl_haract.setItem(5, 2, QtWidgets.QTableWidgetItem(str(mad)))  # МАД
        self.tableWidget_Chisl_haract.setItem(6, 2, QtWidgets.QTableWidgetItem(str(disp)))  # Незсунена Дисперсія
        self.tableWidget_Chisl_haract.setItem(7, 2, QtWidgets.QTableWidgetItem(str(disp_z)))  # Зсунена дисперсія

        self.tableWidget_Chisl_haract.setItem(8, 1, QtWidgets.QTableWidgetItem(
            str(self.return_sigma_mean_lower(mean, np.sqrt(disp), np.shape(list_data)[0]))))  # Нижня оцінка Сер.Квад.В.
        self.tableWidget_Chisl_haract.setItem(8, 2, QtWidgets.QTableWidgetItem(str(np.sqrt(disp))))  # Сер.Квад.Відхилен
        self.tableWidget_Chisl_haract.setItem(8, 3, QtWidgets.QTableWidgetItem(
            str(self.return_sigma_mean_upper(mean, np.sqrt(disp), np.shape(list_data)[0]))))  # Верхня оцінка Сер.Квад.В

        self.tableWidget_Chisl_haract.setItem(9, 2, QtWidgets.QTableWidgetItem(str(sigma_z)))  # Сер.Квад зсун.
        self.tableWidget_Chisl_haract.setItem(10, 2, QtWidgets.QTableWidgetItem(str(cof_asim)))  # Коеф.Асим не зсун
        self.tableWidget_Chisl_haract.setItem(11, 2, QtWidgets.QTableWidgetItem(str(cof_asim_z)))  # Коеф. Асим. зсун.
        self.tableWidget_Chisl_haract.setItem(12, 2,
                                              QtWidgets.QTableWidgetItem(
                                                  str(cof_ecsc_z)))  # Коефіцієнт ексцесу, зсунений
        self.tableWidget_Chisl_haract.setItem(13, 2,
                                              QtWidgets.QTableWidgetItem(str(cof_ecsc)))  # Коефіцієнт ексцесу, незсунен
        self.tableWidget_Chisl_haract.setItem(14, 2, QtWidgets.QTableWidgetItem(
            str(self.coef_cont_ecses(cof_ecsc))))  # Коефіцієнт контрексцесу
        self.tableWidget_Chisl_haract.setItem(15, 2, QtWidgets.QTableWidgetItem(
            str(self.coef_var_Pirsona(sigma, mean, mad, med))))  # Коефіцієнт варіації Пірсона
        self.tableWidget_Chisl_haract.setItem(16, 2, QtWidgets.QTableWidgetItem(str(np.min(list_data))))  # Мінімум
        self.tableWidget_Chisl_haract.setItem(17, 2, QtWidgets.QTableWidgetItem(str(np.max(list_data))))  # Максимум
