from models.repair import RepairData
import pandas as pd
from manager.config_manager import ConfigParser
from manager.excel_style_manager import setExcelStyling
def manage_data(new_data, flag) -> None:
    data = read_excel()
    if flag == 0:
        #процесс удаления
        ...

    if flag == 1:

        #процесс создания
        for string in new_data:
            string_df = pd.DataFrame.from_dict(string)
            data = pd.concat([data, string_df], ignore_index=True)

        if save_excel(data):
            return True


    if flag == 2:
        #процесс изменения
        if new_data == None:
            data.loc[data['Статус'] == 'Не отправлено', 'Статус'] = 'Отправлено'
        if save_excel(data):
            return True
def read_excel() -> pd.DataFrame:
    data = pd.read_excel(get_full_path())
    return data

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
