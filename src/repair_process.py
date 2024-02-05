from models.repair import RepairData
import pandas as pd
from manager.config_manager import ConfigParser
from manager.excel_style_manager import setExcelStyling
import datetime
from models.exceptions import CustomException
from src.create_repair_document import on_create
def manage_data(new_data, flag):
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
                    'Комментарий': [datum['Комментарий'][0] for datum in new_data]

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

    if flag == 4:
        if len(data.loc[data['№ Заказа'] == new_data]) == 0:
            raise CustomException(f'Номер заказа {new_data} не найден в excel-файле! Проверьте правильность указанного номера заказа!')
        else:
            repair_info = {'Клиент': data.loc[data['№ Заказа'] == new_data, 'Клиент'].iloc[0],
                           'Статус': data.loc[data['№ Заказа'] == new_data, 'Статус'].iloc[0],
                           '№ Отправления': str(data.loc[data['№ Заказа'] == new_data, '№ Отправления'].iloc[0]),
                           'Дата отправления': str(data.loc[data['№ Заказа'] == new_data, 'Дата отправления'].iloc[0]),
                           'Дата выдачи': str(data.loc[data['№ Заказа'] == new_data, 'Клиенту'].iloc[0]),
                           'Сданные изделия': {
                               'Название': [str(data.loc[data['№ Заказа'] == new_data, 'Изделие'].iloc[i]) for i in range(len(data.loc[data['№ Заказа'] == new_data]))],
                               'Количество': [str(data.loc[data['№ Заказа'] == new_data, 'Количество изделий'].iloc[i]) for i in range(len(data.loc[data['№ Заказа'] == new_data]))]
                           }}

            return repair_info
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
