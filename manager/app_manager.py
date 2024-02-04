import os
import sys
import datetime
from config_manager import ConfigParser
from template.form import Ui_MainWindow
from PySide6 import QtCore, QtGui, QtWidgets
from installation.install import install_process
from models.exceptions import CustomException

class MainForm(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        config = ConfigParser()
        self.unblockedStyleOfRepairBtn = self.ui.repairMenuButton.styleSheet()
        self.unblockedStyleOfDebtBtn = self.ui.debtMenuButton.styleSheet()
        #логика кнопок страницы Установки
        self.ui.OpenFileBrowserBtn.clicked.connect(self.installation_open_fileBrowser_by_click)
        self.ui.InstallBtn.clicked.connect(self.installation_app)

        # логика кнопок главного Меню
        self.ui.installationMenuButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.repairMenuButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.settingsMenuButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.debtMenuButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))

        # логика кнопок страницы Настройки-->видимость кнопок меню
        self.ui.CheckBoxRepairBtn.setChecked(config.config["Settings"]["repairBtnVisible"])
        self.ui.CheckBoxInstallBtn.setChecked(config.config["Settings"]["debtBtnVisible"])
        self.ui.CheckBoxDebtButton.setChecked(config.config["Settings"]["installationBtnVisible"])
        self.settingsVisibility()
        self.ui.CheckBoxRepairBtn.stateChanged.connect(self.settingsVisibility)
        self.ui.CheckBoxInstallBtn.stateChanged.connect(self.settingsVisibility)
        self.ui.CheckBoxDebtButton.stateChanged.connect(self.settingsVisibility)
        # логика кнопок страницы Настройки-->добавить или удалить поля в эксель файле
        self.ui.InsertFieldBtn.clicked.connect(lambda: self.settingsChangeExcelFields(1))
        self.ui.DropFieldBtn.clicked.connect(lambda: self.settingsChangeExcelFields(0))

        # логика кнопок страницы Настройки-->сохранение настроек
        self.ui.SaveSettingsBtn.clicked.connect(self.settingsSave)

        # логика кнопок страницы Ремонтов
        self.ui.RepairNoInTextEdit.setPlainText(config.config["RepairInfo"]["LastRepairNo"])
        self.ui.RepairDataTextEdit.setPlainText(self.get_data())
        self.ui.TableRepairDocField.


    def installation_app(self) -> bool:
        userResponse = QtWidgets.QMessageBox.question(self, 'Предупреждение', 'Вы уверены?')
        if userResponse == QtWidgets.QMessageBox.StandardButton.Yes:
                try:
                    install_process(self.ui.InstallPathTextEdit.toPlainText())
                    QtWidgets.QMessageBox.information(self, 'Информация', 'Установка прошла успешно!')
                    self.ui.debtMenuButton.setEnabled(True)
                    self.ui.repairMenuButton.setEnabled(True)
                    self.ui.repairMenuButton.setStyleSheet(self.unblockedStyleOfRepairBtn)
                    self.ui.debtMenuButton.setStyleSheet(self.unblockedStyleOfDebtBtn)
                    self.ui.stackedWidget.setCurrentIndex(2)
                except CustomException as excptn:
                    QtWidgets.QMessageBox.critical(self, 'Ошибка', f'Установка не удалась по причине: {excptn.__str__()}')
        return True
    def installation_open_fileBrowser_by_click(self)-> None:
        filePath = QtWidgets.QFileDialog.getExistingDirectory()
        self.ui.InstallPathTextEdit.setText(filePath)
    def settingsVisibility(self) -> None:
        if self.ui.CheckBoxRepairBtn.checkState().value == 0:
            self.ui.repairMenuButton.hide()
        elif self.ui.CheckBoxRepairBtn.checkState().value == 2:
            self.ui.repairMenuButton.setVisible(True)

        if self.ui.CheckBoxDebtButton.checkState().value == 0:
            self.ui.debtMenuButton.hide()
        elif self.ui.CheckBoxDebtButton.checkState().value == 2:
            self.ui.debtMenuButton.setVisible(True)

        if self.ui.CheckBoxInstallBtn.checkState().value == 0:
            self.ui.installationMenuButton.hide()
        elif self.ui.CheckBoxInstallBtn.checkState().value == 2:
            self.ui.installationMenuButton.setVisible(True)
    def settingsSave(self) -> None:
        config = ConfigParser()
        if self.ui.CheckBoxRepairBtn.checkState().value == 0:
            config.config["Settings"]["repairBtnVisible"] = False
        elif self.ui.CheckBoxRepairBtn.checkState().value == 2:
            config.config["Settings"]["repairBtnVisible"] = True
        if self.ui.CheckBoxDebtButton.checkState().value == 0:
            config.config["Settings"]["debtBtnVisible"] = False
        elif self.ui.CheckBoxDebtButton.checkState().value == 2:
            config.config["Settings"]["debtBtnVisible"] = True
        if self.ui.CheckBoxDebtButton.checkState().value == 0:
            config.config["Settings"]["installationBtnVisible"] = False
        elif self.ui.CheckBoxDebtButton.checkState().value == 2:
            config.config["Settings"]["installationBtnVisible"] = True
        try:
            config.save_config()
            QtWidgets.QMessageBox.information(self, 'Информация',
                                           f'Настройки сохранены!')
        except:
            QtWidgets.QMessageBox.critical(self, 'Ошибка',
                                           f'При сохранении настроек возникла ошибка!')

    def settingsChangeExcelFields(self, operation_flag) -> None:
        if check_integrity(self):
            config = ConfigParser()
            if operation_flag == 0:
                if os.path.exists(config.config["ExcelPath"] + "/" + self.ui.ExcelNameTextEdit.toPlainText() + ".xlsx"):
                    QtWidgets.QMessageBox.information(self, 'Информация',"Скоро данная функция будет работать!")
                else:
                    QtWidgets.QMessageBox.critical(self, 'Ошибка',
                                                   f'Файл {self.ui.ExcelNameTextEdit.toPlainText()}.xlsx не найден! Проверьте верность названия!')
            elif operation_flag == 1:
                if os.path.exists(config.config["ExcelPath"] + "/" + self.ui.ExcelNameTextEdit.toPlainText() + ".xlsx"):
                    QtWidgets.QMessageBox.information(self, 'Информация',"Скоро данная функция будет работать!")
                else:
                    QtWidgets.QMessageBox.critical(self, 'Ошибка',
                                                   f'Файл {self.ui.ExcelNameTextEdit.toPlainText()}.xlsx не найден! Проверьте верность названия!')
        else:
            QtWidgets.QMessageBox.critical(self, 'Ошибка',
                                           f'Из-за нарушения целостности невозможно изменить файл!')

    def get_data(self):
        return datetime.datetime.today().strftime('%d-%m-%Y')



def on_start() -> None:
    app = QtWidgets.QApplication(sys.argv)
    window = MainForm()
    if check_first_start(window.ui):
        window.ui.stackedWidget.setCurrentIndex(0)
    elif check_integrity(window):
        window.ui.stackedWidget.setCurrentIndex(2)
    window.show()
    sys.exit(app.exec())


def check_first_start(ui) -> bool:
    checker = ConfigParser()
    if checker.config["Status"] == "NotInstalled":
        ui.debtMenuButton.setEnabled(False)
        ui.repairMenuButton.setEnabled(False)
        ui.repairMenuButton.setStyleSheet(
            u"background-color: rgb(90, 90, 90);\n"
            "color: rgb(135, 135, 135);\n"
        )
        ui.debtMenuButton.setStyleSheet(
            u"background-color: rgb(90, 90, 90);\n"
            "color: rgb(135, 135, 135);\n"
        )

        return True
    else:
        return False

def check_integrity(window) -> bool:
    config = ConfigParser()
    excel_files = [config.config["ExcelFiles"][count]["ExcelFilename"] for count in range(int(config.config["ExcelFilesQty"]))]
    if not os.path.exists(config.config["ExcelPath"] + "/АрхивРемонтов/"):
        QtWidgets.QMessageBox.critical(window, 'Ошибка', f'При проверке целостности данных не был найдена папка АрхивРемонтов')
        return False
    if not os.path.exists(config.config["ExcelPath"] + "/АрхивЗадолженностей/"):
        QtWidgets.QMessageBox.critical(window, 'Ошибка', f'При проверке целостности данных не был найдена папка АрхивЗадолженностей')
        return False
    for name in excel_files:
        if not os.path.exists(config.config["ExcelPath"] +"/" + name + '.xlsx'):
            QtWidgets.QMessageBox.critical(window, 'Ошибка', f'При проверке целостности данных не был найден файл {name}.xlsx')
            return False
    return True

on_start()