import pandas as pd
from manager.config_manager import ConfigParser
from manager.excel_style_manager import setExcelStyling
import datetime
from models.exceptions import CustomException

def manage_debt_data(new_data, flag):
    if flag == 1:
        ...
    elif flag == 2:
        ...
    elif flag == 3:
        ...

def read_excel() -> pd.DataFrame:
    data = pd.read_excel(get_full_path())
    return data
def get_date():
        return datetime.datetime.today().strftime('%d-%m-%Y')
def get_full_path() -> str:
    config = ConfigParser()
    path = config.config["ExcelPath"]
    filename = config.config["ExcelFiles"][1]["ExcelFilename"] + '.xlsx'
    full_path = path + '/' + filename
    return full_path
def save_excel(obj: pd.DataFrame) -> bool:
    full_path = get_full_path()
    config = ConfigParser()
    try:
        obj.to_excel(full_path, index=False)
        setExcelStyling(full_path, config.config['ExcelFiles'][1]['ExcelSheetData']['data'])
    except Exception as e:
        print(e.__str__())
    return True