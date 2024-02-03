import sys
import time

from config_manager import ConfigParser
from template.form_changer import Ui_ApplicationManager
from template.form_installer import Ui_InstallerService
from PySide6 import QtCore, QtGui, QtWidgets
def on_start() -> None:
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_ApplicationManager()
    ui.setupUi(window)

    check_first_start(ui)
    install_flag = False
    settings_flag = False

    install_flag = ui.installBtn.clicked.connect(lambda: installation_form())
    settings_flag = ui.installBtn.clicked.connect(lambda: installation_form())
    window.show()

    if install_flag:
        window.close()
        inst = QtWidgets.QWidget()
        ui = Ui_InstallerService()
        ui.setupUi(inst)
        inst.show()


    sys.exit(app.exec())

def installation_form():
    return True
def settings_form():
    return True

def check_first_start(ui) -> None:
    checker = ConfigParser()
    if checker.config["Status"] == "NotInstalled":
        ui.startBtn.setEnabled(False)
        ui.startBtn.setStyleSheet(
            u"background-color: rgb(90, 90, 90);\n"
            "color: rgb(135, 135, 135);\n"
        )
    else:
        pass


on_start()