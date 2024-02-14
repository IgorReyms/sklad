import os
import sys
import datetime
from manager.config_manager import ConfigParser
from template.form import Ui_MainWindow
from PySide6 import QtCore, QtGui, QtWidgets
from installation.install import install_process
from models.exceptions import CustomException
from models.custom_widgets import ExtendedComboBox
from src.repair_process import manage_data
from manager.updater import update_repair_page, update_debt_page, update_settings_page, update_shd_page
from src.debt_process import manage_debt_data
from src.shd_process import shd_manage_data
class MainForm(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        config = ConfigParser()
        self.unblockedStyleOfRepairBtn = self.ui.repairMenuButton.styleSheet()
        self.unblockedStyleOfDebtBtn = self.ui.debtMenuButton.styleSheet()
        self.unblockedStyleOfShdBtn = self.ui.shdMenuButton.styleSheet()
        #логика кнопок страницы Установки
        self.ui.OpenFileBrowserBtn.clicked.connect(self.installation_open_fileBrowser_by_click)
        self.ui.InstallBtn.clicked.connect(self.installation_app)

        # логика кнопок главного Меню
        self.ui.installationMenuButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.repairMenuButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.settingsMenuButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.debtMenuButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.shdMenuButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))

        # логика кнопок страницы Настройки-->видимость кнопок меню
        self.ui.CheckBoxRepairBtn.setChecked(config.config["Settings"]["repairBtnVisible"])
        self.ui.CheckBoxInstallBtn.setChecked(config.config["Settings"]["installationBtnVisible"])
        self.ui.CheckBoxDebtButton.setChecked(config.config["Settings"]["debtBtnVisible"])
        self.ui.CheckBoxShdButton.setChecked(config.config["Settings"]["shdBtnVisible"])
        self.settingsVisibility()
        self.ui.CheckBoxRepairBtn.stateChanged.connect(self.settingsVisibility)
        self.ui.CheckBoxInstallBtn.stateChanged.connect(self.settingsVisibility)
        self.ui.CheckBoxDebtButton.stateChanged.connect(self.settingsVisibility)
        self.ui.CheckBoxShdButton.stateChanged.connect(self.settingsVisibility)

        #логика кнопок Настройки конфигурации
        self.ui.DeleteStringIntoStocksTable.insertRow(0)
        self.ui.DeleteStringIntoStocksTable.insertColumn(0)
        self.ui.DeleteStringIntoStocksTable.verticalHeader().setVisible(False)
        self.ui.DeleteStringIntoStocksTable.setCellWidget(0, 0, ExtendedComboBox(self))
        self.ui.CreateStringIntoStocksBtn.clicked.connect(self.settings_CreateItemStocks)
        self.ui.DeleteStringIntoStocksBtn.clicked.connect(self.settings_DeleteItemStocks)


        # логика кнопок страницы Настройки-->добавить или удалить поля в эксель файле
        # self.ui.InsertFieldBtn.clicked.connect(lambda: self.settingsChangeExcelFields(1))
        # self.ui.DropFieldBtn.clicked.connect(lambda: self.settingsChangeExcelFields(0))

        # логика кнопок страницы Настройки-->сохранение настроек
        self.ui.SaveSettingsBtn.clicked.connect(self.settingsSave)


        # логика кнопок страницы Ремонтов
        self.ui.RepairNoInTextEdit.setPlainText(config.config["RepairInfo"]["LastRepairNo"])
        self.ui.RepairDataTextEdit.setPlainText(self.get_date())
        # логика таблицы страницы Ремонтов
        self.ui.TableRepairDocField.verticalHeader().setVisible(False)
        self.ui.TableRepairDocField.setContextMenuPolicy(QtGui.Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.TableRepairDocField.customContextMenuRequested.connect(self.repairTableContextMenu)


        # логика поиска изделия
        self.ui.RepairFindItem.insertRow(0)
        self.ui.RepairFindItem.insertColumn(0)
        self.ui.RepairFindItem.verticalHeader().setVisible(False)
        self.ui.RepairFindItem.setCellWidget(0, 0, ExtendedComboBox(self))
        self.ui.FinderRepairItemTable.insertRow(0)
        self.ui.FinderRepairItemTable.insertColumn(0)
        self.ui.FinderRepairItemTable.verticalHeader().setVisible(False)
        self.ui.FinderRepairItemTable.setCellWidget(0, 0, ExtendedComboBox(self))
        #создать ремонт
        self.ui.CreateRepairBtn.clicked.connect(self.create_repair)

        #создать отправлениe
        self.ui.CreateShipmentBtn.clicked.connect(self.create_repair_shipment)
        # выдать отремонтированные изделия
        self.ui.RepairOutClientBtn.clicked.connect(self.repair_to_client)

        #Поиск информации по ремонту
        self.ui.FinderRepairInfoBtn.clicked.connect(self.repair_finder_information)

        # логика кнопок страницы ЗАдолженность

        self.ui.CreateDebtBtn.clicked.connect(self.create_debt)
        self.ui.DebtOutBtn.clicked.connect(self.change_debt)
        self.ui.DebtFindBtn.clicked.connect(self.find_debt)
        self.ui.DebtReportPrint.clicked.connect(self.printing_debt_report)

        #логика кнопок страницы Транспортных накладных
        self.ui.shdCreateBtn.clicked.connect(self.shd_CreateShd)
        self.ui.shdFindDateBtn.clicked.connect(self.shd_FindShd)



        if config.config["Status"] == "Installed":
            update_debt_page(self, 'debt_status_info')
            update_settings_page(self)
            update_repair_page(self, 'repair_status_info')
            update_shd_page(self)

    def shd_CreateShd(self):
        if self.ui.shdCreateDateTextEdit.date().day() < 10:
            day = f'0{str(self.ui.shdCreateDateTextEdit.date().day() )}'
        else:
            day = str(self.ui.shdCreateDateTextEdit.date().day() )
        if self.ui.shdCreateDateTextEdit.date().month() < 10:
            month = f'0{str(self.ui.shdCreateDateTextEdit.date().month() )}'
        else:
            month = str(self.ui.shdCreateDateTextEdit.date().month())

        year = str(self.ui.shdCreateDateTextEdit.date().year() )


        shd_data = {
            "ТранспортнаяКомпания": [self.ui.shdCreateShipmentCompanyTextEdit.toPlainText()],
            "Клиент": [self.ui.shdCreateClientTextEdit.toPlainText()],
            "ТрекНомер": [self.ui.shdCreateTrekNoTextEdit.toPlainText()],
            "Дата": [year + '-' + month + '-' +day ]
        }

        try:
            shd_manage_data(shd_data,1)
            QtWidgets.QMessageBox.information(self, 'Информация',
                                              f"Строка по транспортной накладной создана")
            self.ui.shdCreateShipmentCompanyTextEdit.clear()
            self.ui.shdCreateClientTextEdit.clear()
            self.ui.shdCreateTrekNoTextEdit.clear()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Ошибка!",f'Не удалось создать строку по накладной. Причина: {e.__str__()}')
    def shd_FindShd(self):
        if self.ui.shdFindDate1TextEdit.date() < self.ui.shdFindDate0TextEdit.date():
            QtWidgets.QMessageBox.critical(self, "Ошибка!",
                                           f'Поле "ДатаПо" не может быть меньше поля "ДатаС"')
            return None

        if self.ui.shdFindDate0TextEdit.date().day() < 10:
            day_from = f'0{str(self.ui.shdFindDate0TextEdit.date().day())}'
        else:
            day_from = str(self.ui.shdFindDate0TextEdit.date().day())
        if self.ui.shdFindDate0TextEdit.date().month() < 10:
            month_from = f'0{str(self.ui.shdFindDate0TextEdit.date().month())}'
        else:
            month_from = str(self.ui.shdFindDate0TextEdit.date().month())
        if self.ui.shdFindDate1TextEdit.date().day() < 10:
            day_to = f'0{str(self.ui.shdFindDate1TextEdit.date().day())}'
        else:
            day_to = str(self.ui.shdFindDate1TextEdit.date().day())
        if self.ui.shdFindDate1TextEdit.date().month() < 10:
            month_to = f'0{str(self.ui.shdFindDate1TextEdit.date().month())}'
        else:
            month_to = str(self.ui.shdFindDate1TextEdit.date().month())
        year_from = str(self.ui.shdFindDate0TextEdit.date().year())
        year_to = str(self.ui.shdFindDate1TextEdit.date().year())
        shd_data = {
            "ТранспортнаяКомпания": self.ui.shdFindShipmentCompanyTextEdit.toPlainText(),
            "Клиент": self.ui.shdFindClientTextEdit.toPlainText(),
            "ТрекНомер": self.ui.shdFindTrekNoTextEdit.toPlainText(),
            "ДатаC": year_from + '-' + month_from + '-' + day_from,
            "ДатаПо": year_to + '-' + month_to + '-' + day_to,
            "DateFilterFlag": True if self.ui.shdDateCheckBox.checkState().value == 2 else False
        }
        try:
            shd_manage_data(shd_data, 2, self)

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Ошибка!",f'Не удалось совершить поиск накладных. Причина: {e.__str__()}')
    def settings_CreateItemStocks(self):
        self.temp = ExtendedComboBox(self)
        try:
            self.temp.create_stock(stock=self.ui.CreateStringIntoStocksTextEdit.toPlainText())
            QtWidgets.QMessageBox.information(self, 'Информация', f'Изделие {self.ui.CreateStringIntoStocksTextEdit.toPlainText()} успешно добавлено в stocks!')
            self.ui.CreateStringIntoStocksTextEdit.clear()
            self.ui.RepairFindItem.setRowCount(0)
            self.ui.RepairFindItem.insertRow(0)
            self.ui.RepairFindItem.setCellWidget(0, 0, ExtendedComboBox(self))
            self.ui.DebtItemTable.setRowCount(0)
            self.ui.DebtItemTable.insertRow(0)
            self.ui.DebtItemTable.setCellWidget(0, 0, ExtendedComboBox(self))
            self.ui.DebtOutItemTable.setRowCount(0)
            self.ui.DebtOutItemTable.insertRow(0)
            self.ui.DebtOutItemTable.setCellWidget(0, 0, ExtendedComboBox(self))
            self.ui.DeleteStringIntoStocksTable.setRowCount(0)
            self.ui.DeleteStringIntoStocksTable.insertRow(0)
            self.ui.DeleteStringIntoStocksTable.setCellWidget(0, 0, ExtendedComboBox(self))

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Ошибка!",f'Не удалось добавить в stock.xlsx. Причина: {e.__str__()}')
    def settings_DeleteItemStocks(self):
        self.temp = ExtendedComboBox(self)
        try:
            self.temp.delete_stock(stock=self.ui.DeleteStringIntoStocksTable.cellWidget(0, 0).get_data())
            QtWidgets.QMessageBox.information(self, 'Информация',
                                              f'Изделие {self.ui.DeleteStringIntoStocksTable.cellWidget(0, 0).get_data()} удалено из stocks!')
            self.ui.DeleteStringIntoStocksTable.clear()
            self.ui.RepairFindItem.setRowCount(0)
            self.ui.RepairFindItem.insertRow(0)
            self.ui.RepairFindItem.setCellWidget(0, 0, ExtendedComboBox(self))
            self.ui.DebtItemTable.setRowCount(0)
            self.ui.DebtItemTable.insertRow(0)
            self.ui.DebtItemTable.setCellWidget(0, 0, ExtendedComboBox(self))
            self.ui.DebtOutItemTable.setRowCount(0)
            self.ui.DebtOutItemTable.insertRow(0)
            self.ui.DebtOutItemTable.setCellWidget(0, 0, ExtendedComboBox(self))
            self.ui.DeleteStringIntoStocksTable.setRowCount(0)
            self.ui.DeleteStringIntoStocksTable.insertRow(0)
            self.ui.DeleteStringIntoStocksTable.setCellWidget(0, 0, ExtendedComboBox(self))

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Ошибка!", f'Не удалось добавить в stock.xlsx. Причина: {e.__str__()}')

    def create_debt(self):
        try:

            debt_info = {
                '№ Задолженности': [self.ui.DebtNoTextEdit.toPlainText()],
                'Дата создания': [self.ui.DebtDateCreateTextEdit.toPlainText()],
                'Клиент': [self.ui.DebtClientNameTextEdit.toPlainText()],
                'Изделие': [self.ui.DebtItemTable.cellWidget(0, 0).get_data()],
                'Исходный размер задолженности':[int(self.ui.DebtItemQtyTextEdit.toPlainText())],
                'Дата последней выдачи': [''],
                'Количество выданных изделий':[0],
                'Остаток по долгу': [int(self.ui.DebtItemQtyTextEdit.toPlainText())]
            }

            manage_debt_data(debt_info, 1)
            QtWidgets.QMessageBox.information(self, 'Информация', f"Задолженность {self.ui.DebtNoTextEdit.toPlainText()} учтена!")
            update_debt_page(self, 'create_debt')
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, 'Ошибка',
                                           f'При учете новой задолженности произошла ошибка. Причина: {e.__str__()}')

    def change_debt(self):
        try:
            debt_info = {
                '№ Задолженности': [self.ui.DebtOutNoTextEdit.toPlainText()],
                'Дата создания': [''],
                'Клиент': [''],
                'Изделие': [self.ui.DebtOutItemTable.cellWidget(0, 0).get_data()],
                'Исходный размер задолженности': [self.ui.DebtItemQtyTextEdit.toPlainText()],
                'Дата последней выдачи':[self.ui.DebtOutDateTextEdit.toPlainText()],
                'Количество выданных изделий': [self.ui.DebtOutItemQtyTextEdit.toPlainText()],
                'Остаток по долгу': [self.ui.DebtItemQtyTextEdit.toPlainText()]
            }
            manage_debt_data(debt_info, 2)
            QtWidgets.QMessageBox.information(self, 'Информация', f"Задолженность {self.ui.DebtOutNoTextEdit.toPlainText()} изменена!")
            update_debt_page(self, 'change_debt')
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, 'Ошибка',
                                           f'При изменении задолженности произошла ошибка. Причина: {e.__str__()}')


    def find_debt(self):
        try:

            debt_info = {
                '№ Задолженности': [self.ui.DebtFindByDebtNoTextEdit.toPlainText()],
                'Дата создания': [''],
                'Клиент': [self.ui.DebtFindByClientNameTextEdit.toPlainText()],
                'Изделие': [self.ui.DebtInfoItemTable.cellWidget(0, 0).get_data()],
                'Исходный размер задолженности': [0],
                'Дата последней выдачи':[self.ui.DebtFindByLastDateTextEdit.toPlainText()],
                'Количество выданных изделий': [0],
                'Остаток по долгу': [0]
            }
            answer = manage_debt_data(debt_info, 3)

            self.ui.DebtInfoTextEdit.setPlainText(answer)
            update_debt_page(self, 'find_debt')
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, 'Ошибка',
                                           f'При поиске задолженностей произошла ошибка. Причина: {e.__str__()}')
    def printing_debt_report(self):
        try:
            debt_info = {
                '№ Задолженности': [self.ui.DebtReportNoTextEdit.toPlainText()],
                'Дата создания': [''],
                'Клиент': [''],
                'Изделие': [''],
                'Исходный размер задолженности': [0],
                'Дата последней выдачи': [''],
                'Количество выданных изделий': [''],
                'Остаток по долгу': ['']
            }
            fonts = {"MainFont": int(self.ui.FontSizeMainTextEdit.toPlainText()),
                     "NotMainFont": int(self.ui.FontSizeNotMainTextEdit.toPlainText())}
            manage_debt_data(debt_info, 4,fonts=fonts)
            QtWidgets.QMessageBox.information(self, 'Информация',
                                           f'Печатная форма по задолжностям сформирована.')
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, 'Ошибка',
                                           f'При создании печатной формы произошла ошибка. Причина: {e.__str__()}')
    def installation_app(self) -> bool:
        userResponse = QtWidgets.QMessageBox.question(self, 'Предупреждение', 'Вы уверены?')
        if userResponse == QtWidgets.QMessageBox.StandardButton.Yes:
                try:
                    install_process(self.ui.InstallPathTextEdit.toPlainText())
                    QtWidgets.QMessageBox.information(self, 'Информация', 'Установка прошла успешно!')
                    self.ui.debtMenuButton.setEnabled(True)
                    self.ui.repairMenuButton.setEnabled(True)
                    self.ui.shdMenuButton.setEnabled(True)
                    self.ui.settingsMenuButton.setEnabled(True)
                    self.ui.repairMenuButton.setStyleSheet(self.unblockedStyleOfRepairBtn)
                    self.ui.debtMenuButton.setStyleSheet(self.unblockedStyleOfDebtBtn)
                    self.ui.shdMenuButton.setStyleSheet(self.unblockedStyleOfShdBtn)
                    self.ui.stackedWidget.setCurrentIndex(2)
                    update_repair_page(self, 'repair_status_info')
                    update_debt_page(self, 'debt_status_info')
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

        if self.ui.CheckBoxShdButton.checkState().value == 0:
            self.ui.shdMenuButton.hide()
        elif self.ui.CheckBoxShdButton.checkState().value == 2:
            self.ui.shdMenuButton.setVisible(True)
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
        if self.ui.CheckBoxInstallBtn.checkState().value == 0:
                config.config["Settings"]["installationBtnVisible"] = False
        elif self.ui.CheckBoxInstallBtn.checkState().value == 2:
                config.config["Settings"]["installationBtnVisible"] = True
        if self.ui.CheckBoxShdButton.checkState().value == 0:
                config.config["Settings"]["shdBtnVisible"] = False
        elif self.ui.CheckBoxShdButton.checkState().value == 2:
                config.config["Settings"]["shdBtnVisible"] = True


        userResponse = QtWidgets.QMessageBox.question(self, 'Предупреждение', 'Вы уверены, что хотите изменить структуру номера документов?')
        if userResponse == QtWidgets.QMessageBox.StandardButton.Yes:
                    message_values = [config.config["RepairInfo"]["LastRepairNo"],
                                      config.config["DebtInfo"]["LastDebtNo"],
                                      self.ui.SettingsRepairPrefixTextEdit.toPlainText() + '-' + str(self.ui.SetingsRepairFirstNoTextEdit.toPlainText()),
                                      self.ui.SettingsRepairPrefixTextEdit_2.toPlainText() + '-' + str(self.ui.SetingsRepairFirstNoTextEdit_2.toPlainText()),
                                      config.config["ReportInfo"]["MainFontSize"],
                                      config.config["ReportInfo"]["NotMainFontSize"],
                                      self.ui.FontSizeMainTextEdit.toPlainText(),
                                      self.ui.FontSizeNotMainTextEdit.toPlainText()]

                    config.config["RepairInfo"]["LastRepairNo"] = self.ui.SettingsRepairPrefixTextEdit.toPlainText() + '-' + str(self.ui.SetingsRepairFirstNoTextEdit.toPlainText())
                    config.config["DebtInfo"]["LastDebtNo"] = self.ui.SettingsRepairPrefixTextEdit_2.toPlainText() + '-' + str(self.ui.SetingsRepairFirstNoTextEdit_2.toPlainText())
                    config.config["ReportInfo"]["MainFontSize"] = self.ui.FontSizeMainTextEdit.toPlainText()
                    config.config["ReportInfo"]["NotMainFontSize"] = self.ui.FontSizeNotMainTextEdit.toPlainText()

        try:
            config.save_config()
            QtWidgets.QMessageBox.information(self, 'Информация', f'Настройки файла конфигурации сохранены! \n{message_values[0]}-->{message_values[2]}\n{message_values[1]}-->{message_values[3]}\nГлавный '
                                                                  f'шрифт {message_values[4]}-->{message_values[6]} \nМладший шрифт {message_values[5]}-->{message_values[7]}')
            update_settings_page(self)

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, 'Ошибка',
                                           f'При сохранении настроек возникла ошибка! Причина {e.__str__()}')

    # def settingsChangeExcelFields(self, operation_flag) -> None:
    #     if check_integrity(self):
    #         config = ConfigParser()
    #         if operation_flag == 0:
    #             if os.path.exists(config.config["ExcelPath"] + "/" + self.ui.ExcelNameTextEdit.toPlainText() + ".xlsx"):
    #                 QtWidgets.QMessageBox.information(self, 'Информация',"Скоро данная функция будет работать!")
    #             else:
    #                 QtWidgets.QMessageBox.critical(self, 'Ошибка',
    #                                                f'Файл {self.ui.ExcelNameTextEdit.toPlainText()}.xlsx не найден! Проверьте верность названия!')
    #         elif operation_flag == 1:
    #             if os.path.exists(config.config["ExcelPath"] + "/" + self.ui.ExcelNameTextEdit.toPlainText() + ".xlsx"):
    #                 QtWidgets.QMessageBox.information(self, 'Информация',"Скоро данная функция будет работать!")
    #             else:
    #                 QtWidgets.QMessageBox.critical(self, 'Ошибка',
    #                                                f'Файл {self.ui.ExcelNameTextEdit.toPlainText()}.xlsx не найден! Проверьте верность названия!')
    #     else:
    #         QtWidgets.QMessageBox.critical(self, 'Ошибка',
    #                                        f'Из-за нарушения целостности невозможно изменить файл!')

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

        fonts = {"MainFont": int(self.ui.FontSizeMainTextEdit.toPlainText()), "NotMainFont": int(self.ui.FontSizeNotMainTextEdit.toPlainText())}
        try:
            manage_data(repairs, 1,fonts=fonts)
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
            # if self.ui.FinderRepairNoTextEdit.toPlainText() != '' and self.ui.FinderRepairByClientTextEdit.toPlainText() != '':
            #     QtWidgets.QMessageBox.warning(self, 'Предупреждение',
            #                                    f'Заполнены оба поля поиска! Поиск осуществлен по Номеру Ремонта!')
            # if self.ui.FinderRepairNoTextEdit.toPlainText() != '':
            #     repair_info = manage_data(self.ui.FinderRepairNoTextEdit.toPlainText(), 4)
            #     QtWidgets.QMessageBox.information(self, 'Информация',
            #                                       f"Ремонт {self.ui.FinderRepairNoTextEdit.toPlainText()} найден!")
            #
            #     self.ui.FinderRepairClientTextEdit.setPlainText(repair_info['Клиент'])
            #     self.ui.FinderRepairStatusTextEdit.setPlainText(repair_info['Статус'])
            #     self.ui.FinderRepairShipNoTextEdit.setPlainText(repair_info['№ Отправления'])
            #     self.ui.FinderRepairShipmentDateTextEdit.setPlainText(str(repair_info['Дата отправления']))
            #     self.ui.FinderRepairOutTextEdit.setPlainText(str(repair_info['Дата выдачи']))
            #
            #
            #     string = ''
            #     name_len = len(repair_info['Сданные изделия']['Название'][0])
            #     for i in range(len(repair_info['Сданные изделия']['Название'])):
            #         string += repair_info['Сданные изделия']['Название'][i] + '-->' + str(repair_info['Сданные изделия']['Количество'][i]).ljust(5) + '\n'
            #         if name_len < len(repair_info['Сданные изделия']['Название'][i]):
            #             name_len = len(repair_info['Сданные изделия']['Название'][i])
            #
            #     string_head = 'Изделие'  + ' ' * (name_len-7)+ 'Количество\n'.ljust(5) + string
            #     self.ui.FinderRepairItemInfoTextEdit.setPlainText(string_head)
            #     self.ui.FinderRepairNoTextEdit.clear()
            #
            # if self.ui.FinderRepairByClientTextEdit.toPlainText() != '':
            #     repair_info = manage_data(self.ui.FinderRepairByClientTextEdit.toPlainText(), 5)
            #     QtWidgets.QMessageBox.information(self, 'Информация',
            #                                       f"По названию организации {self.ui.FinderRepairByClientTextEdit.toPlainText()} ремонты найдены!")
            #     self.ui.FinderRepairByClientTextEdit.clear()
            #     self.ui.FinderRepairAllInfoTextEdit.setPlainText(repair_info)
            filters = {
                '№ Заказа': self.ui.FinderRepairNoTextEdit.toPlainText(),
                'Клиент': self.ui.FinderRepairByClientTextEdit.toPlainText(),
                'Изделие': self.ui.FinderRepairItemTable.cellWidget(0, 0).get_data()
            }
            manage_data(filters, 4,fonts=None, window=self)

            self.ui.FinderRepairItemTable.setRowCount(0)
            self.ui.FinderRepairItemTable.insertRow(0)
            self.ui.FinderRepairItemTable.verticalHeader().setVisible(False)
            self.ui.FinderRepairItemTable.setCellWidget(0, 0, ExtendedComboBox(self))
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
        ui.shdMenuButton.setEnabled(False)
        ui.settingsMenuButton.setEnabled(False)
        ui.repairMenuButton.setStyleSheet(
            u"background-color: rgb(90, 90, 90);\n"
            "color: rgb(135, 135, 135);\n"
        )
        ui.debtMenuButton.setStyleSheet(
            u"background-color: rgb(90, 90, 90);\n"
            "color: rgb(135, 135, 135);\n"
        )
        ui.shdMenuButton.setStyleSheet(
            u"background-color: rgb(90, 90, 90);\n"
            "color: rgb(135, 135, 135);\n"
        )
        ui.settingsMenuButton.setStyleSheet(
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
        if not os.path.exists(config.config["ExcelPath"] + "/" + name + '.xlsx'):

            QtWidgets.QMessageBox.critical(window, 'Ошибка', f'При проверке целостности данных не был найден файл {name}.xlsx')


    return True

def start_project() -> None:
    on_start()