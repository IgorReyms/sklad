# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled2JKJDSg.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_InstallerService(object):
    def setupUi(self, InstallerService):
        if not InstallerService.objectName():
            InstallerService.setObjectName(u"InstallerService")
        InstallerService.resize(1016, 167)
        font = QFont()
        font.setFamilies([u"Gotham Pro"])
        font.setPointSize(14)
        InstallerService.setFont(font)
        InstallerService.setStyleSheet(u"QFrame {\n"
"font: 12pt \"Gotham Pro\";\n"
"background-color: rgb(59, 54, 53);\n"
"color: rgb(197, 197, 197);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: rgb(108, 100, 124);\n"
"font: 14pt \"Gotham Pro\";\n"
"color: rgb(229, 229, 229);\n"
"}")
        self.centralwidget = QWidget(InstallerService)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(271, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(271, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 25, 0, 25)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.textEdit = QTextEdit(self.frame_3)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_3.addWidget(self.textEdit)

        self.openpath = QPushButton(self.frame_3)
        self.openpath.setObjectName(u"openpath")

        self.horizontalLayout_3.addWidget(self.openpath)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 4)
        self.horizontalLayout_3.setStretch(2, 1)

        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(428, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.horizontalSpacer_3 = QSpacerItem(429, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.installBtn = QPushButton(self.frame_4)
        self.installBtn.setObjectName(u"installBtn")

        self.horizontalLayout_2.addWidget(self.installBtn)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.verticalLayout_2.setStretch(0, 3)
        self.verticalLayout_2.setStretch(1, 1)

        self.verticalLayout.addWidget(self.frame_2)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)
        # InstallerService.setCentralWidget(self.centralwidget)

        self.retranslateUi(InstallerService)

        QMetaObject.connectSlotsByName(InstallerService)
    # setupUi

    def retranslateUi(self, InstallerService):
        InstallerService.setWindowTitle(QCoreApplication.translate("InstallerService", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0449\u0438\u043a", None))
        self.label.setText(QCoreApplication.translate("InstallerService", u"\u0412\u0430\u0441 \u043f\u0440\u0438\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u0435\u0442 \u043c\u0430\u0441\u0442\u0435\u0440 \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u0420\u0435\u043c\u043e\u043d\u0442", None))
        self.label_2.setText(QCoreApplication.translate("InstallerService", u"\u041f\u0443\u0442\u044c \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438", None))
        self.openpath.setText(QCoreApplication.translate("InstallerService", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043f\u0430\u043f\u043a\u0443", None))
        self.installBtn.setText(QCoreApplication.translate("InstallerService", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
    # retranslateUi

