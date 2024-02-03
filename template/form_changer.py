# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiformBepyrH.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_ApplicationManager(object):
    def setupUi(self, ApplicationManager):
        if not ApplicationManager.objectName():
            ApplicationManager.setObjectName(u"ApplicationManager")

        ApplicationManager.resize(642, 442)
        font = QFont()
        font.setFamilies([u"Gotham Pro"])
        font.setPointSize(14)
        ApplicationManager.setFont(font)
        ApplicationManager.setStyleSheet(u"QFrame {\n"
"font: 14pt \"Gotham Pro\";\n"
"background-color: rgb(59, 54, 53);\n"
"color: rgb(197, 197, 197);\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: rgb(108, 100, 124);\n"
"	font: 14pt \"Gotham Pro\";\n"
"	color: rgb(229, 229, 229)\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(ApplicationManager)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(ApplicationManager)
        self.frame.setObjectName(u"frame")
        font1 = QFont()
        font1.setFamilies([u"Gotham Pro"])
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        self.frame.setFont(font1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(77, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.verticalLayout_4.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.verticalSpacer = QSpacerItem(20, 96, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.startBtn = QPushButton(self.frame_3)
        self.startBtn.setObjectName(u"startBtn")
        self.startBtn.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.startBtn)

        self.verticalSpacer_3 = QSpacerItem(20, 32, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.installBtn = QPushButton(self.frame_3)
        self.installBtn.setObjectName(u"installBtn")

        self.verticalLayout_3.addWidget(self.installBtn)

        self.verticalSpacer_4 = QSpacerItem(20, 32, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.settingsBtn = QPushButton(self.frame_3)
        self.settingsBtn.setObjectName(u"settingsBtn")

        self.verticalLayout_3.addWidget(self.settingsBtn)

        self.verticalLayout_3.setStretch(0, 3)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 3)
        self.verticalLayout_3.setStretch(3, 1)
        self.verticalLayout_3.setStretch(4, 3)

        self.verticalLayout_2.addWidget(self.frame_3)

        self.verticalSpacer_2 = QSpacerItem(20, 96, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 3)
        self.verticalLayout_2.setStretch(2, 6)
        self.verticalLayout_2.setStretch(3, 3)

        self.horizontalLayout.addWidget(self.frame_2)

        self.horizontalSpacer_2 = QSpacerItem(77, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 6)
        self.horizontalLayout.setStretch(2, 3)

        self.verticalLayout.addWidget(self.frame)

        self.verticalLayout.setStretch(0, 10)

        self.retranslateUi(ApplicationManager)



        QMetaObject.connectSlotsByName(ApplicationManager)
    # setupUi


    def retranslateUi(self, ApplicationManager):
        ApplicationManager.setWindowTitle(QCoreApplication.translate("ApplicationManager", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("ApplicationManager", u"\u0412\u0430\u0441 \u043f\u0440\u0438\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u0435\u0442  \u0441\u0435\u0440\u0432\u0438\u0441 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u0420\u0435\u043c\u043e\u043d\u0442", None))
        self.startBtn.setText(QCoreApplication.translate("ApplicationManager", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435", None))
        self.installBtn.setText(QCoreApplication.translate("ApplicationManager", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435", None))
        self.settingsBtn.setText(QCoreApplication.translate("ApplicationManager", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f", None))
    # retranslateUi



