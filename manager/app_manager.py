import os
import sys
import datetime
from config_manager import ConfigParser
from template.form import Ui_MainWindow
from PySide6 import QtCore, QtGui, QtWidgets
from installation.install import install_process
from models.exceptions import CustomException
from models.custom_widgets import ExtendedComboBox
from src.create_repair import manage_data
from updater import update_repair_page
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
        self.ui.RepairDataTextEdit.setPlainText(self.get_date())
        # логика таблицы страницы Ремонтов
        self.ui.TableRepairDocField.verticalHeader().setVisible(False)
        self.ui.TableRepairDocField.setContextMenuPolicy(QtGui.Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.TableRepairDocField.customContextMenuRequested.connect(self.repairTableContextMenu)
        update_repair_page(self, 'repair_status_info')
        # логика поиска изделия
        self.ui.RepairFindItem.insertRow(0)
        self.ui.RepairFindItem.insertColumn(0)
        self.ui.RepairFindItem.verticalHeader().setVisible(False)
        self.ui.RepairFindItem.setCellWidget(0, 0, ExtendedComboBox(self))

        #создать ремонт
        self.ui.CreateRepairBtn.clicked.connect(self.create_repair)

        #создать отправлениe
        self.ui.CreateShipmentBtn.clicked.connect(self.create_repair_shipment)
        # выдать отремонтированные изделия
        self.ui.RepairOutClientBtn.clicked.connect(self.repair_to_client)

        #Поиск информации по ремонту
        self.ui.FinderRepairInfoBtn.clicked.connect(self.repair_finder_information)
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

    def get_date(self):
        return datetime.datetime.today().strftime('%d-%m-%Y')

    def repairTableContextMenu(self, pos):
        context_menu = QtWidgets.QMenu(self.ui.TableRepairDocField)
        add_action = QtGui.QAction("Вставить строку", self.ui.TableRepairDocField)
        del_action = QtGui.QAction("Удалить строку", self.ui.TableRepairDocField)

        add_action.triggered.connect(self.repairTableInsertRow)
        del_action.triggered.connect(self.repairTableDeleteRow)
        context_menu.addActions([add_action, del_action])
        context_menu.exec(self.ui.TableRepairDocField.viewport().mapToGlobal(pos))

    def repairTableInsertRow(self):
        try:
            combo_box = ExtendedComboBox()
        except CustomException as e:
            QtWidgets.QMessageBox.critical(self, 'Ошибка',
                                           f'При чтении файла товаров stocks произошла ошибка. Причина: {e.__str__()}')
        row_count = self.ui.TableRepairDocField.rowCount()
        self.ui.TableRepairDocField.insertRow(row_count)
        self.ui.TableRepairDocField.setCellWidget(row_count, 0, combo_box)



    def repairTableDeleteRow(self):
        selected_rows = self.ui.TableRepairDocField.selectedIndexes()
        for index in selected_rows:
            self.ui.TableRepairDocField.removeRow(index.row())

    def create_repair(self) -> None:
        rows_count = self.ui.TableRepairDocField.rowCount()
        cols_count = self.ui.TableRepairDocField.columnCount()
        static_repair_data = {
                '№ Заказа': [self.ui.RepairNoInTextEdit.toPlainText()],
                'Статус': ['Не отправлено'],
                '№ Отправления': [''],
                'Клиент': [self.ui.RepairClientTextEdit.toPlainText()],
                'От клиента': [self.ui.RepairDataTextEdit.toPlainText()],
                'Дата отправления': [''],
                'Клиенту':[''],
                'Изделие':[''],
                'Количество изделий': [0],
                'Комментарий':['']
            }
        repairs = list()
        data = static_repair_data
        for row in range(rows_count):

            for col in range(cols_count):
                if col == 0:
                    item = self.ui.TableRepairDocField.cellWidget(row, col).get_data()
                else:
                    item = self.ui.TableRepairDocField.item(row, col)
                if item is not None:
                    if col == 0:
                        data['Изделие'] = [str(item)]
                    elif col == 1:
                        data['Количество изделий'] = [int(item.text())]
                    elif col == 2:
                        data['Комментарий'] = [item.text()]
            repairs.append(data.copy())
            data = static_repair_data.copy()

        try:
            manage_data(repairs, 1)
            QtWidgets.QMessageBox.information(self, 'Информация', f"Ремонт {self.ui.RepairNoInTextEdit.toPlainText()} учтен! Создано строк:{len(repairs)}")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, 'Ошибка',
                                           f'При учете нового ремонта произошла ошибка. Причина: {e.__str__()}')

        if len(repairs) != 0:
            update_repair_page(self, 'create_repair')
        else:
            QtWidgets.QMessageBox.warning(self, 'Информация',
                                             f"Отсутствуют строки ремонта! Ремонт не создан!")

    def create_repair_shipment(self) -> None:

        try:
            manage_data(self.ui.ShipmentNoTextEdit.toPlainText(), 2)
            QtWidgets.QMessageBox.information(self, 'Информация',
                                              f"Ремонты отправлены! Изменено строк:{self.ui.RepairQtyUnShipInfoTextEdit.toPlainText()}")
            if self.ui.RepairQtyUnShipInfoTextEdit.toPlainText() != '0':
                update_repair_page(self, 'create_shipment')
            else:
                QtWidgets.QMessageBox.warning(self, 'Информация',
                                              f"Отсутствуют не отправленные Ремонты! Отправление не создано!")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, 'Ошибка',
                                           f'При создании отправления произошла ошибка!. Причина: {e.__str__()}')

    def repair_to_client(self) -> None:
        try:
            manage_data(self.ui.RepairNoOutTextEdit.toPlainText(), 3)
            QtWidgets.QMessageBox.information(self, 'Информация',
                                              f"Ремонт {self.ui.RepairNoOutTextEdit.toPlainText()} выдан клиенту!")

            update_repair_page(self, 'repair_status_info')
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, 'Ошибка',
                                           f'При выдаче ремонта произошла ошибка!. Причина: {e.__str__()}')

    def repair_finder_information(self):
        try:
            repair_info = manage_data(self.ui.FinderRepairNoTextEdit.toPlainText(), 4)
            QtWidgets.QMessageBox.information(self, 'Информация',
                                              f"Ремонт {self.ui.FinderRepairNoTextEdit.toPlainText()} найден!")

            self.ui.FinderRepairClientTextEdit.setPlainText(repair_info['Клиент'])
            self.ui.FinderRepairStatusTextEdit.setPlainText(repair_info['Статус'])
            self.ui.FinderRepairShipNoTextEdit.setPlainText(repair_info['№ Отправления'])
            self.ui.FinderRepairShipmentDateTextEdit.setPlainText(str(repair_info['Дата отправления']))
            self.ui.FinderRepairOutTextEdit.setPlainText(str(repair_info['Дата выдачи']))


            string = ''
            name_len = len(repair_info['Сданные изделия']['Название'][0])
            for i in range(len(repair_info['Сданные изделия']['Название'])):
                string += repair_info['Сданные изделия']['Название'][i] + '-->' + str(repair_info['Сданные изделия']['Количество'][i]).ljust(5) + '\n'
                if name_len < len(repair_info['Сданные изделия']['Название'][i]):
                    name_len = len(repair_info['Сданные изделия']['Название'][i])
            print(name_len)
            string_head = 'Изделие'  + ' ' * (name_len-7)+ 'Количество\n'.ljust(5) + string
            self.ui.FinderRepairItemInfoTextEdit.setPlainText(string_head)


        except Exception as e:
            QtWidgets.QMessageBox.critical(self, 'Ошибка',
                                           f'Информация по ремонту не собрана. Причина: {e.__str__()}')
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