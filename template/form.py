# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiformNYKfwY.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1016, 805)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QLabel {\n"
"font: 10pt \"Microsoft JhengHei\";\n"
"}\n"
"QFrame#frame{\n"
"background-color:rgb(255, 255, 255);\n"
"}\n"
"QFrame#frame_2{\n"
"background-color:rgb(240, 240, 240);\n"
"}\n"
"QFrame#frame_3{\n"
"background-color:rgb(240, 240, 240);\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 2px;\n"
"}\n"
"QFrame#frame_4{\n"
"background-color:rgb(240, 240, 240);\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 2px;\n"
"}\n"
"QStackedWidget {\n"
"background-color:rgb(240, 240, 240);\n"
"}\n"
"QPushButton {\n"
"	background-color:rgb(255, 255, 255);\n"
"	font: 10pt \"Microsoft JhengHei\";\n"
"	border-style: outset;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(255, 255, 255);\n"
"	font: 10pt \"Microsoft JhengHei\";\n"
"	border-color:rgb(33, 214, 255);\n"
"	border-width: 1px;\n"
"	border-radius: 7px;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 "
                        "#f6f7fa);\n"
"	\n"
"	font: 10pt \"Microsoft JhengHei\";\n"
"	border-color:rgb(33, 214, 255);\n"
"	border-width: 2px\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 0, 0)
        self.installationMenuButton = QPushButton(self.frame)
        self.installationMenuButton.setObjectName(u"installationMenuButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.installationMenuButton.sizePolicy().hasHeightForWidth())
        self.installationMenuButton.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.installationMenuButton)

        self.settingsMenuButton = QPushButton(self.frame)
        self.settingsMenuButton.setObjectName(u"settingsMenuButton")
        sizePolicy.setHeightForWidth(self.settingsMenuButton.sizePolicy().hasHeightForWidth())
        self.settingsMenuButton.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.settingsMenuButton)

        self.repairMenuButton = QPushButton(self.frame)
        self.repairMenuButton.setObjectName(u"repairMenuButton")
        sizePolicy.setHeightForWidth(self.repairMenuButton.sizePolicy().hasHeightForWidth())
        self.repairMenuButton.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.repairMenuButton)

        self.debtMenuButton = QPushButton(self.frame)
        self.debtMenuButton.setObjectName(u"debtMenuButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.debtMenuButton.sizePolicy().hasHeightForWidth())
        self.debtMenuButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.debtMenuButton)

        self.horizontalSpacer = QSpacerItem(479, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 2)
        self.horizontalLayout.setStretch(4, 6)

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.installationPage = QWidget()
        self.installationPage.setObjectName(u"installationPage")
        self.label = QLabel(self.installationPage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(310, 10, 381, 41))
        self.label_2 = QLabel(self.installationPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 60, 231, 16))
        self.InstallPathTextEdit = QTextEdit(self.installationPage)
        self.InstallPathTextEdit.setObjectName(u"InstallPathTextEdit")
        self.InstallPathTextEdit.setGeometry(QRect(190, 60, 511, 26))
        self.OpenFileBrowserBtn = QPushButton(self.installationPage)
        self.OpenFileBrowserBtn.setObjectName(u"OpenFileBrowserBtn")
        self.OpenFileBrowserBtn.setGeometry(QRect(710, 60, 111, 24))
        self.InstallBtn = QPushButton(self.installationPage)
        self.InstallBtn.setObjectName(u"InstallBtn")
        self.InstallBtn.setGeometry(QRect(710, 100, 111, 24))
        self.stackedWidget.addWidget(self.installationPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.label_3 = QLabel(self.settingsPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 10, 251, 16))
        self.frame_3 = QFrame(self.settingsPage)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(20, 30, 251, 151))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 251, 16))
        self.CheckBoxInstallBtn = QCheckBox(self.frame_3)
        self.CheckBoxInstallBtn.setObjectName(u"CheckBoxInstallBtn")
        self.CheckBoxInstallBtn.setGeometry(QRect(10, 40, 76, 20))
        self.CheckBoxInstallBtn.setChecked(True)
        self.CheckBoxRepairBtn = QCheckBox(self.frame_3)
        self.CheckBoxRepairBtn.setObjectName(u"CheckBoxRepairBtn")
        self.CheckBoxRepairBtn.setGeometry(QRect(10, 70, 161, 20))
        self.CheckBoxRepairBtn.setChecked(True)
        self.CheckBoxDebtButton = QCheckBox(self.frame_3)
        self.CheckBoxDebtButton.setObjectName(u"CheckBoxDebtButton")
        self.CheckBoxDebtButton.setGeometry(QRect(10, 100, 141, 20))
        self.CheckBoxDebtButton.setChecked(True)
        self.SaveSettingsBtn = QPushButton(self.frame_3)
        self.SaveSettingsBtn.setObjectName(u"SaveSettingsBtn")
        self.SaveSettingsBtn.setGeometry(QRect(20, 120, 201, 24))
        self.label_5 = QLabel(self.settingsPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 190, 251, 16))
        self.frame_4 = QFrame(self.settingsPage)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(20, 210, 331, 131))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.ExcelNameTextEdit = QPlainTextEdit(self.frame_4)
        self.ExcelNameTextEdit.setObjectName(u"ExcelNameTextEdit")
        self.ExcelNameTextEdit.setGeometry(QRect(160, 10, 151, 31))
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 20, 131, 16))
        self.ExcelFieldTextEdit = QPlainTextEdit(self.frame_4)
        self.ExcelFieldTextEdit.setObjectName(u"ExcelFieldTextEdit")
        self.ExcelFieldTextEdit.setGeometry(QRect(160, 50, 151, 31))
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 50, 151, 31))
        self.DropFieldBtn = QPushButton(self.frame_4)
        self.DropFieldBtn.setObjectName(u"DropFieldBtn")
        self.DropFieldBtn.setGeometry(QRect(90, 90, 101, 24))
        self.InsertFieldBtn = QPushButton(self.frame_4)
        self.InsertFieldBtn.setObjectName(u"InsertFieldBtn")
        self.InsertFieldBtn.setGeometry(QRect(200, 90, 111, 24))
        self.stackedWidget.addWidget(self.settingsPage)
        self.repairPage = QWidget()
        self.repairPage.setObjectName(u"repairPage")
        self.RepairNoOutTextEdit = QPlainTextEdit(self.repairPage)
        self.RepairNoOutTextEdit.setObjectName(u"RepairNoOutTextEdit")
        self.RepairNoOutTextEdit.setGeometry(QRect(120, 600, 251, 31))
        self.label_8 = QLabel(self.repairPage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 60, 81, 16))
        self.TableRepairDocField = QTableWidget(self.repairPage)
        if (self.TableRepairDocField.columnCount() < 3):
            self.TableRepairDocField.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.TableRepairDocField.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.TableRepairDocField.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.TableRepairDocField.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.TableRepairDocField.setObjectName(u"TableRepairDocField")
        self.TableRepairDocField.setGeometry(QRect(10, 220, 931, 161))
        self.TableRepairDocField.setMidLineWidth(1)
        self.TableRepairDocField.setSortingEnabled(True)
        self.TableRepairDocField.setRowCount(0)
        self.TableRepairDocField.setColumnCount(3)
        self.TableRepairDocField.horizontalHeader().setDefaultSectionSize(150)
        self.TableRepairDocField.horizontalHeader().setStretchLastSection(True)
        self.label_9 = QLabel(self.repairPage)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 200, 81, 16))
        self.RepairClientTextEdit = QPlainTextEdit(self.repairPage)
        self.RepairClientTextEdit.setObjectName(u"RepairClientTextEdit")
        self.RepairClientTextEdit.setGeometry(QRect(90, 100, 251, 31))
        self.label_10 = QLabel(self.repairPage)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 110, 81, 20))
        self.label_11 = QLabel(self.repairPage)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 160, 81, 20))
        self.RepairDataTextEdit = QPlainTextEdit(self.repairPage)
        self.RepairDataTextEdit.setObjectName(u"RepairDataTextEdit")
        self.RepairDataTextEdit.setGeometry(QRect(90, 150, 251, 31))
        self.CreateRepairBtn = QPushButton(self.repairPage)
        self.CreateRepairBtn.setObjectName(u"CreateRepairBtn")
        self.CreateRepairBtn.setGeometry(QRect(10, 390, 161, 24))
        self.CreateShipmentBtn = QPushButton(self.repairPage)
        self.CreateShipmentBtn.setObjectName(u"CreateShipmentBtn")
        self.CreateShipmentBtn.setGeometry(QRect(220, 500, 161, 24))
        self.label_12 = QLabel(self.repairPage)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(30, 470, 121, 16))
        self.ShipmentNoTextEdit = QPlainTextEdit(self.repairPage)
        self.ShipmentNoTextEdit.setObjectName(u"ShipmentNoTextEdit")
        self.ShipmentNoTextEdit.setGeometry(QRect(130, 460, 251, 31))
        self.label_13 = QLabel(self.repairPage)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(30, 610, 81, 16))
        self.RepairOutClientBtn = QPushButton(self.repairPage)
        self.RepairOutClientBtn.setObjectName(u"RepairOutClientBtn")
        self.RepairOutClientBtn.setGeometry(QRect(220, 640, 161, 24))
        self.RepairNoInTextEdit = QPlainTextEdit(self.repairPage)
        self.RepairNoInTextEdit.setObjectName(u"RepairNoInTextEdit")
        self.RepairNoInTextEdit.setGeometry(QRect(90, 50, 251, 31))
        self.label_14 = QLabel(self.repairPage)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(410, 10, 171, 16))
        self.label_15 = QLabel(self.repairPage)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(390, 430, 141, 16))
        self.label_16 = QLabel(self.repairPage)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(330, 570, 331, 16))
        self.label_17 = QLabel(self.repairPage)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(710, 30, 111, 16))
        self.label_18 = QLabel(self.repairPage)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(620, 50, 241, 16))
        self.RepairQtyUnShipInfoTextEdit = QTextEdit(self.repairPage)
        self.RepairQtyUnShipInfoTextEdit.setObjectName(u"RepairQtyUnShipInfoTextEdit")
        self.RepairQtyUnShipInfoTextEdit.setGeometry(QRect(860, 40, 104, 31))
        self.label_19 = QLabel(self.repairPage)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(620, 90, 241, 16))
        self.RepairQtyShipInfoTextEdit = QTextEdit(self.repairPage)
        self.RepairQtyShipInfoTextEdit.setObjectName(u"RepairQtyShipInfoTextEdit")
        self.RepairQtyShipInfoTextEdit.setGeometry(QRect(860, 80, 104, 31))
        self.label_20 = QLabel(self.repairPage)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(620, 120, 241, 31))
        self.RepairQtyInfoTextEdit = QTextEdit(self.repairPage)
        self.RepairQtyInfoTextEdit.setObjectName(u"RepairQtyInfoTextEdit")
        self.RepairQtyInfoTextEdit.setGeometry(QRect(860, 120, 104, 31))
        self.label_21 = QLabel(self.repairPage)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(370, 190, 91, 20))
        self.RepairFindItem = QTableWidget(self.repairPage)
        self.RepairFindItem.setObjectName(u"RepairFindItem")
        self.RepairFindItem.setGeometry(QRect(470, 180, 471, 31))
        self.RepairFindItem.setShowGrid(False)
        self.RepairFindItem.setCornerButtonEnabled(False)
        self.RepairFindItem.setColumnCount(0)
        self.RepairFindItem.horizontalHeader().setVisible(False)
        self.RepairFindItem.horizontalHeader().setHighlightSections(True)
        self.RepairFindItem.horizontalHeader().setStretchLastSection(True)
        self.stackedWidget.addWidget(self.repairPage)
        self.debtPage = QWidget()
        self.debtPage.setObjectName(u"debtPage")
        self.label_22 = QLabel(self.debtPage)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(370, 10, 171, 16))
        self.DebtNoTextEdit = QPlainTextEdit(self.debtPage)
        self.DebtNoTextEdit.setObjectName(u"DebtNoTextEdit")
        self.DebtNoTextEdit.setGeometry(QRect(150, 50, 181, 31))
        self.label_23 = QLabel(self.debtPage)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(10, 60, 121, 16))
        self.label_24 = QLabel(self.debtPage)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(10, 100, 121, 16))
        self.label_25 = QLabel(self.debtPage)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(530, 60, 91, 20))
        self.ItemFindNameTextEdit = QPlainTextEdit(self.debtPage)
        self.ItemFindNameTextEdit.setObjectName(u"ItemFindNameTextEdit")
        self.ItemFindNameTextEdit.setGeometry(QRect(630, 50, 311, 31))
        self.DebtItemNameTextEdit = QPlainTextEdit(self.debtPage)
        self.DebtItemNameTextEdit.setObjectName(u"DebtItemNameTextEdit")
        self.DebtItemNameTextEdit.setGeometry(QRect(150, 90, 281, 31))
        self.label_26 = QLabel(self.debtPage)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(10, 180, 141, 16))
        self.DebtClientNameTextEdit = QPlainTextEdit(self.debtPage)
        self.DebtClientNameTextEdit.setObjectName(u"DebtClientNameTextEdit")
        self.DebtClientNameTextEdit.setGeometry(QRect(150, 170, 281, 31))
        self.label_27 = QLabel(self.debtPage)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(10, 220, 141, 16))
        self.DebtDateCreateTextEdit = QPlainTextEdit(self.debtPage)
        self.DebtDateCreateTextEdit.setObjectName(u"DebtDateCreateTextEdit")
        self.DebtDateCreateTextEdit.setGeometry(QRect(150, 210, 281, 31))
        self.label_28 = QLabel(self.debtPage)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(370, 310, 171, 16))
        self.label_29 = QLabel(self.debtPage)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(20, 340, 121, 16))
        self.DebtOutNoTextEdit = QPlainTextEdit(self.debtPage)
        self.DebtOutNoTextEdit.setObjectName(u"DebtOutNoTextEdit")
        self.DebtOutNoTextEdit.setGeometry(QRect(160, 330, 181, 31))
        self.DebtItemQtyTextEdit = QPlainTextEdit(self.debtPage)
        self.DebtItemQtyTextEdit.setObjectName(u"DebtItemQtyTextEdit")
        self.DebtItemQtyTextEdit.setGeometry(QRect(150, 130, 281, 31))
        self.label_30 = QLabel(self.debtPage)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(10, 140, 121, 16))
        self.DebtOutItemNameTextEdit = QPlainTextEdit(self.debtPage)
        self.DebtOutItemNameTextEdit.setObjectName(u"DebtOutItemNameTextEdit")
        self.DebtOutItemNameTextEdit.setGeometry(QRect(160, 370, 281, 31))
        self.label_31 = QLabel(self.debtPage)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(20, 380, 121, 16))
        self.DebtOutItemQtyTextEdit = QPlainTextEdit(self.debtPage)
        self.DebtOutItemQtyTextEdit.setObjectName(u"DebtOutItemQtyTextEdit")
        self.DebtOutItemQtyTextEdit.setGeometry(QRect(160, 410, 281, 31))
        self.label_32 = QLabel(self.debtPage)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(20, 420, 121, 16))
        self.DebtOutDateTextEdit = QPlainTextEdit(self.debtPage)
        self.DebtOutDateTextEdit.setObjectName(u"DebtOutDateTextEdit")
        self.DebtOutDateTextEdit.setGeometry(QRect(160, 450, 281, 31))
        self.label_33 = QLabel(self.debtPage)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(20, 460, 141, 16))
        self.label_34 = QLabel(self.debtPage)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(590, 210, 261, 20))
        self.DebtFindByClientNameTextEdit = QPlainTextEdit(self.debtPage)
        self.DebtFindByClientNameTextEdit.setObjectName(u"DebtFindByClientNameTextEdit")
        self.DebtFindByClientNameTextEdit.setGeometry(QRect(770, 240, 191, 31))
        self.label_35 = QLabel(self.debtPage)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(590, 250, 161, 16))
        self.label_36 = QLabel(self.debtPage)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(590, 280, 161, 16))
        self.DebtFindByItemNameTextEdit = QPlainTextEdit(self.debtPage)
        self.DebtFindByItemNameTextEdit.setObjectName(u"DebtFindByItemNameTextEdit")
        self.DebtFindByItemNameTextEdit.setGeometry(QRect(770, 280, 191, 31))
        self.label_37 = QLabel(self.debtPage)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(590, 320, 161, 16))
        self.DebtFindByLastDateTextEdit = QPlainTextEdit(self.debtPage)
        self.DebtFindByLastDateTextEdit.setObjectName(u"DebtFindByLastDateTextEdit")
        self.DebtFindByLastDateTextEdit.setGeometry(QRect(770, 320, 191, 31))
        self.CreateDebtBtn = QPushButton(self.debtPage)
        self.CreateDebtBtn.setObjectName(u"CreateDebtBtn")
        self.CreateDebtBtn.setGeometry(QRect(274, 260, 161, 24))
        self.DebtOutBtn = QPushButton(self.debtPage)
        self.DebtOutBtn.setObjectName(u"DebtOutBtn")
        self.DebtOutBtn.setGeometry(QRect(280, 490, 161, 24))
        self.DebtFindBtn = QPushButton(self.debtPage)
        self.DebtFindBtn.setObjectName(u"DebtFindBtn")
        self.DebtFindBtn.setGeometry(QRect(800, 360, 161, 24))
        self.DebtInfoTextEdit = QPlainTextEdit(self.debtPage)
        self.DebtInfoTextEdit.setObjectName(u"DebtInfoTextEdit")
        self.DebtInfoTextEdit.setGeometry(QRect(590, 410, 381, 291))
        self.stackedWidget.addWidget(self.debtPage)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.frame_2)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 15)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043b\u0430\u0434", None))
        self.installationMenuButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430", None))
        self.settingsMenuButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.repairMenuButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438 \u043f\u043e \u0440\u0435\u043c\u043e\u043d\u0442\u0430\u043c", None))
        self.debtMenuButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438 \u043f\u043e \u0434\u043e\u043b\u0433\u0430\u043c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u0432\u0438\u0441 \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 \u043c\u043e\u0434\u0443\u043b\u0435\u0439 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u0442\u043e \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 \u043d\u0430 \u0434\u0438\u0441\u043a\u0435", None))
        self.OpenFileBrowserBtn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043f\u0430\u043f\u043a\u0443", None))
        self.InstallBtn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0433\u043b\u0430\u0432\u043d\u043e\u0433\u043e \u043c\u0435\u043d\u044e", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434\u0438\u043c\u043e\u0441\u0442\u044c \u043a\u043d\u043e\u043f\u043e\u043a", None))
        self.CheckBoxInstallBtn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430", None))
        self.CheckBoxRepairBtn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438 \u043f\u043e \u0440\u0435\u043c\u043e\u043d\u0442\u0430\u043c", None))
        self.CheckBoxDebtButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438 \u043f\u043e \u0434\u043e\u043b\u0433\u0430\u043c", None))
        self.SaveSettingsBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u0438", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 excel-\u0444\u0430\u0439\u043b\u0430", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0434\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u043c\u043e\u0433\u043e\n"
"\u0438\u043b\u0438 \u0443\u0434\u0430\u043b\u044f\u0435\u043c\u043e\u0433\u043e \u043f\u043e\u043b\u044f", None))
        self.DropFieldBtn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043f\u043e\u043b\u0435", None))
        self.InsertFieldBtn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u043b\u0435", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u2116 \u0420\u0435\u043c\u043e\u043d\u0442\u0430", None))
        ___qtablewidgetitem = self.TableRepairDocField.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0438\u0437\u0434\u0435\u043b\u0438\u044f", None));
        ___qtablewidgetitem1 = self.TableRepairDocField.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None));
        ___qtablewidgetitem2 = self.TableRepairDocField.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439", None));
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044f \u0437\u0430\u043a\u0430\u0437\u0430", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0438\u0435\u043d\u0442", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442 \u043a\u043b\u0438\u0435\u043d\u0442\u0430", None))
        self.CreateRepairBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0440\u0435\u043c\u043e\u043d\u0442", None))
        self.CreateShipmentBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u2116 \u041e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u2116 \u0420\u0435\u043c\u043e\u043d\u0442\u0430", None))
        self.RepairOutClientBtn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0434\u0430\u0442\u044c \u043a\u043b\u0438\u0435\u043d\u0442\u0443", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0437\u0430\u043a\u0430\u0437\u0430 \u043f\u043e \u0440\u0435\u043c\u043e\u043d\u0442\u0443", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0434\u0430\u0447\u0430 \u043e\u0442\u0440\u0435\u043c\u043e\u043d\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u0438\u0437\u0434\u0435\u043b\u0438\u0439 \u043a\u043b\u0438\u0435\u043d\u0442\u0443 ", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0435 \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u043d\u044b\u0445 \u0440\u0435\u043c\u043e\u043d\u0442\u043e\u0432", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u043d\u044b\u0445 \u0440\u0435\u043c\u043e\u043d\u0442\u043e\u0432", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0442\u0440\u043e\u043a excel-\u0444\u0430\u0439\u043b\u0430 \n"
" \u043f\u043e \u0440\u0435\u043c\u043e\u043d\u0442\u0430\u043c", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u0438\u0437\u0434\u0435\u043b\u0438\u044f", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0437\u0430\u0434\u043e\u043b\u0436\u0435\u043d\u043d\u043e\u0441\u0442\u044c", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u2116 \u0437\u0430\u0434\u043e\u043b\u0436\u0435\u043d\u043d\u043e\u0441\u0442\u0438", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0438\u0437\u0434\u0435\u043b\u0438\u044f", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u0438\u0437\u0434\u0435\u043b\u0438\u044f", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0434\u0430\u0447\u0430 \u0434\u043e\u043b\u0433\u0430", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u2116 \u0437\u0430\u0434\u043e\u043b\u0436\u0435\u043d\u043d\u043e\u0441\u0442\u0438", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0438\u0437\u0434\u0435\u043b\u0438\u0439", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0438\u0437\u0434\u0435\u043b\u0438\u044f", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0438\u0437\u0434\u0435\u043b\u0438\u0439", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043f\u043e \u043e\u0442\u043a\u0440\u044b\u0442\u044b\u043c \u0437\u0430\u0434\u043e\u043b\u0436\u0435\u043d\u043d\u043e\u0441\u0442\u044f\u043c", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044e \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044e \u0438\u0437\u0434\u0435\u043b\u0438\u044f", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0434\u0430\u0442\u0435 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0439 \u0432\u044b\u0434\u0430\u0447\u0438", None))
        self.CreateDebtBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0437\u0430\u0434\u043e\u043b\u0436\u0435\u043d\u043d\u043e\u0441\u0442\u044c", None))
        self.DebtOutBtn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0434\u0430\u0442\u044c \u043f\u043e \u0437\u0430\u0434\u043e\u043b\u0436\u0435\u043d\u043d\u043e\u0441\u0442\u0438", None))
        self.DebtFindBtn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e", None))
    # retranslateUi

