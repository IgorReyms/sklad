import pandas as pd
import datetime
from manager.config_manager import ConfigParser
from manager.excel_style_manager import setExcelStyling
from PySide6 import QtWidgets
def shd_manage_data(new_data, flag, window=None):
    data = read_excel()
    data.astype(str)
    if flag == 1:
        string_df = pd.DataFrame.from_dict(new_data)
        string_df["ТрекНомер"].astype(str)

        data = pd.concat([data, string_df], ignore_index=True)

        if save_excel(data):
            return True
    elif flag == 2:
        if new_data["DateFilterFlag"]:
            new_data.pop("DateFilterFlag")
            df_copy = data.copy()

            pd.to_datetime(df_copy["Дата"])
            df_copy = df_copy[(df_copy["Дата"] >= new_data["ДатаC"]) & (df_copy["Дата"] <= new_data["ДатаПо"]) ]

            new_data.pop("ДатаC")
            new_data.pop("ДатаПо")
            for key in new_data:
                if new_data[key] != '':
                    if key == 'Клиент':
                        df_copy = df_copy[df_copy['Клиент'].str.contains(new_data['Клиент'])]
                    elif key == 'ТранспортнаяКомпания':
                        df_copy = df_copy[df_copy['ТранспортнаяКомпания'].str.contains(new_data['ТранспортнаяКомпания'])]
                    else:
                        try:
                            df_copy = df_copy.loc[(df_copy[key] == int(new_data[key]))]
                        except:
                            df_copy = df_copy.loc[(df_copy[key] == new_data[key])]

        elif not new_data["DateFilterFlag"]:
            new_data.pop("DateFilterFlag")
            new_data.pop("ДатаC")
            new_data.pop("ДатаПо")
            df_copy = data.copy()

            for key in new_data:
                if new_data[key] != '':
                    if key == 'Клиент':
                        df_copy = df_copy[df_copy['Клиент'].str.contains(new_data['Клиент'])]
                    elif key == 'ТранспортнаяКомпания':
                        df_copy = df_copy[df_copy['ТранспортнаяКомпания'].str.contains(new_data['ТранспортнаяКомпания'])]
                    else:
                        try:
                            df_copy = df_copy.loc[(df_copy[key] == int(new_data[key]))]
                        except:
                            df_copy = df_copy.loc[(df_copy[key] == new_data[key])]

        cols = [column for column in df_copy]
        window.ui.ShdInfoTable.setColumnCount(0)
        window.ui.ShdInfoTable.setRowCount(0)

        window.ui.ShdInfoTable.setColumnCount(len(cols))
        window.ui.ShdInfoTable.setRowCount(int(df_copy.shape[0]))
        window.ui.ShdInfoTable.verticalHeader().setVisible(False)
        header = window.ui.ShdInfoTable.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)
        window.ui.ShdInfoTable.setHorizontalHeaderLabels(cols)
        for index, col in enumerate(cols):
            if index > 0:
                header.setSectionResizeMode(index, QtWidgets.QHeaderView.ResizeMode.Stretch)

        index_str = 0
        for index, row in df_copy.iterrows():

            for index_col, col in enumerate(cols):
                window.ui.ShdInfoTable.setItem(index_str, index_col,
                                                          QtWidgets.QTableWidgetItem(str(row[col])))
            index_str += 1
def read_excel() -> pd.DataFrame:
    data = pd.read_excel(get_full_path())
    return data
def save_excel(obj: pd.DataFrame) -> bool:
    full_path = get_full_path()
    config = ConfigParser()
    try:
        obj.to_excel(full_path, index=False)
        setExcelStyling(full_path, config.config['ExcelFiles'][2]['ExcelSheetData']['data'])
    except Exception as e:
        print(e.__str__())
    return True
def get_full_path() -> str:
    config = ConfigParser()
    path = config.config["ExcelPath"]
    filename = config.config["ExcelFiles"][2]["ExcelFilename"] + '.xlsx'
    full_path = path + '/' + filename
    return full_path