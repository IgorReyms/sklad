from models.repair import RepairData
import pandas as pd
from manager.config_manager import ConfigParser
from manager.excel_style_manager import setExcelStyling
import datetime
from models.exceptions import CustomException
from src.create_repair_document import on_create
from PySide6 import QtWidgets
def manage_data(new_data, flag, fonts=None, window=None):
    data = read_excel()
    if flag == 0:
        #процесс удаления
        ...

    if flag == 1:

        #процесс создания ремонта
        for string in new_data:
            string_df = pd.DataFrame.from_dict(string)
            data = pd.concat([data, string_df], ignore_index=True)

        if save_excel(data):
            config = ConfigParser()
            try:
                pdf_data = {
                    'ExcelPath': config.config["ExcelPath"],
                    'Дата': str(get_date()),
                    'Клиент': new_data[0]["Клиент"][0],
                    '№ Заказа': new_data[0]["№ Заказа"][0],
                    'Изделие': [datum['Изделие'][0] for datum in new_data],
                    'Количество': [str(datum['Количество изделий'][0]) for datum in new_data],
                    'Комментарий': [datum['Комментарий'][0] for datum in new_data],
                    'MainFont': fonts['MainFont'],
                    'NotMainFont': fonts['NotMainFont']

                }
                print(pdf_data)
                on_create(pdf_data)
            except Exception as e:
                raise e
            return True


    if flag == 2:
        #процесс отпраления ремонтов
        data.loc[data['Статус'] == 'Не отправлено', '№ Отправления'] =  new_data
        data.loc[data['Статус'] == 'Не отправлено', 'Дата отправления'] = get_date()
        data.loc[data['Статус'] == 'Не отправлено', 'Статус'] = 'Отправлено'

        if save_excel(data):
            return True

    if flag == 3:
        #процесс выдачи клиенту

        if len(data.loc[data['№ Заказа'] == new_data]) == 0:
            raise CustomException(f'Номер заказа {new_data} не найден в excel-файле! Проверьте правильность указанного номера заказа!')
        else:

            data.loc[data['№ Заказа'] == new_data, 'Статус'] = 'Выдано клиенту'
            data.loc[data['№ Заказа'] == new_data, 'Клиенту'] = get_date()
            if save_excel(data):
                return True

    # if flag == 4:
    #     #поиск по номеру ремонта
    #     if len(data.loc[data['№ Заказа'] == new_data]) == 0:
    #         raise CustomException(f'Номер заказа {new_data} не найден в excel-файле! Проверьте правильность указанного номера заказа!')
    #     else:
    #         repair_info = {'Клиент': data.loc[data['№ Заказа'] == new_data, 'Клиент'].iloc[0],
    #                        'Статус': data.loc[data['№ Заказа'] == new_data, 'Статус'].iloc[0],
    #                        '№ Отправления': str(data.loc[data['№ Заказа'] == new_data, '№ Отправления'].iloc[0]),
    #                        'Дата отправления': str(data.loc[data['№ Заказа'] == new_data, 'Дата отправления'].iloc[0]),
    #                        'Дата выдачи': str(data.loc[data['№ Заказа'] == new_data, 'Клиенту'].iloc[0]),
    #                        'Сданные изделия': {
    #                            'Название': [str(data.loc[data['№ Заказа'] == new_data, 'Изделие'].iloc[i]) for i in range(len(data.loc[data['№ Заказа'] == new_data]))],
    #                            'Количество': [str(data.loc[data['№ Заказа'] == new_data, 'Количество изделий'].iloc[i]) for i in range(len(data.loc[data['№ Заказа'] == new_data]))]
    #                        }}
    #
    #         return repair_info
    if flag == 4:
        #поиск информации по ремонтам
        df_copy = data.copy()
        for key in new_data:
            if new_data[key] != '':
                if key == 'Клиент':
                    df_copy = df_copy[df_copy['Клиент'].str.contains(new_data['Клиент'])]
                else:
                    df_copy = df_copy.loc[(df_copy[key] == new_data[key])]

        if df_copy.equals(data):
            raise CustomException("Заполните поля фильтров поиска!")

        df_copy = df_copy[['№ Заказа', 'Статус', 'Клиент','От клиента', 'Дата отправления', 'Клиенту', 'Количество изделий','Изделие']]
        cols = [column for column in df_copy]
        answer = ''
        col_print_width = 10
        for col in cols:
            answer += str(col) + 'ㅤ' * (col_print_width - len(col))
        answer += '\n'

        window.ui.FinderRepairResultTable.setColumnCount(0)
        window.ui.FinderRepairResultTable.setRowCount(0)

        window.ui.FinderRepairResultTable.setColumnCount(len(cols))
        window.ui.FinderRepairResultTable.setRowCount(int(df_copy.shape[0]))
        print(df_copy.shape[0])
        header = window.ui.FinderRepairResultTable.horizontalHeader()
        # header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)
        window.ui.FinderRepairResultTable.setHorizontalHeaderLabels(cols)
        for index,col in enumerate(cols):
            if index > 0:
                header.setSectionResizeMode(index, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

        index_str = 0
        for index, row in df_copy.iterrows():

            for index_col, col in enumerate(cols):
                window.ui.FinderRepairResultTable.setItem(index_str, index_col, QtWidgets.QTableWidgetItem(str(row[col])))
            index_str += 1

def read_excel() -> pd.DataFrame:
    data = pd.read_excel(get_full_path())
    return data
def get_date():
        return datetime.datetime.today().strftime('%d-%m-%Y')
def get_full_path() -> str:
    config = ConfigParser()
    path = config.config["ExcelPath"]
    filename = config.config["ExcelFiles"][0]["ExcelFilename"] + '.xlsx'
    full_path = path + '/' + filename
    return full_path
def save_excel(obj: pd.DataFrame) -> bool:
    full_path = get_full_path()
    config = ConfigParser()
    try:
        obj.to_excel(full_path, index=False)
        setExcelStyling(full_path, config.config['ExcelFiles'][0]['ExcelSheetData']['data'])
    except Exception as e:
        print(e.__str__())
    return True
