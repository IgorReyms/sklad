import os

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, QSortFilterProxyModel
from PySide6.QtWidgets import QCompleter, QComboBox
import openpyxl, pandas, pathlib
from models.exceptions import CustomException
class ExtendedComboBox(QComboBox):
    def __init__(self, parent=None):
        super(ExtendedComboBox, self).__init__(parent)
        self.setPlaceholderText("Поиск...")
        self.setFocusPolicy(Qt.StrongFocus)
        self.setEditable(True)


        # add a filter model to filter matching items
        self.pFilterModel = QSortFilterProxyModel(self)
        self.pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.pFilterModel.setSourceModel(self.model())

        # add a completer, which uses the filter model
        self.completer = QCompleter(self.pFilterModel, self)
        # always show all (filtered) completions
        self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.setCompleter(self.completer)

        # connect signals
        self.lineEdit().textEdited.connect(self.pFilterModel.setFilterFixedString)
        self.completer.activated.connect(self.on_completer_activated)

        self.stocks = self.read_stocks()
        self.addItems(self.stocks)

    # on selection of an item from the completer, select the corresponding item from combobox
    def read_stocks(self) -> list:
        try:
            df_items = pandas.read_excel(str(os.getcwd().split('manager')[0] + "\\models\\stocks.xlsx"), header=1, usecols=[2])
            return df_items["Товар"].tolist()
        except Exception as e:
            raise CustomException(e.__str__())

    def get_data(self):
        return self.itemText(self.currentIndex())
    def on_completer_activated(self, text):
        if text:
            index = self.findText(text)
            self.setCurrentIndex(index)
            self.activated[str].emit(self.itemText(index))


    # on model change, update the models of the filter and completer as well
    def setModel(self, model):
        super(ExtendedComboBox, self).setModel(model)
        self.pFilterModel.setSourceModel(model)
        self.completer.setModel(self.pFilterModel)


    # on model column change, update the model column of the filter and completer as well
    def setModelColumn(self, column):
        self.completer.setCompletionColumn(column)
        self.pFilterModel.setFilterKeyColumn(column)
        super(ExtendedComboBox, self).setModelColumn(column)

