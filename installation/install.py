from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Border, Side
import os
import json
# config = {"ExcelFilename": "ИсторияОтправлений",
#           "ExcelPath": '',
#           "ExcelSheetData": {
#     'sheetname':"ИсторияОпераций",
#     'data':{
#             'A1': '№ Заказа',
#             'B1': '№ Отправления',
#             'C1': 'Клиент',
#             'D1': 'От клиента',
#             'E1': 'Дата отправления',
#             'F1': 'Клиенту',
#             'G1': 'Количество изделий',
#             'H1': 'Изделия',
#           }
#           }
#           }
# with open('lconfig.json', 'w') as f:
#     json.dump(config, f)

class ConfigParser:
    def __init__(self):
        self.config = self.get_config()
    def get_config(self, __path='lconfig.json'):
        with open(__path, 'r') as f:
            config = json.load(f)
        return config
    def save_config(self, __path = 'lconfig.json') -> bool:
        with open(__path, 'w') as f:
            json.dump(self.config, f)
        return True

def change_config(path) -> bool:
    config = ConfigParser()
    config.config['ExcelPath'] = path
    return config.save_config()

def create_excel(path) -> bool:
    if change_config(path):

        config = ConfigParser()

        xlsx_data = Workbook()
        ws = xlsx_data.active
        ws.title = config.config['ExcelSheetData']['sheetname']



        if configure_excelfile(ws, config.config['ExcelSheetData']['data']):
            if path.replace(' ','') == '':
                xlsx_data.save(path + config.config["ExcelFilename"] + '.xlsx')
            else:
                xlsx_data.save(path + '/' +config.config["ExcelFilename"] + '.xlsx')

def configure_excelfile(sheet, sheet_config) -> bool:
    for key in sheet_config:
        sheet[key] = sheet_config[key]
        sheet[key].font = Font(size=12, bold=True)
        sheet[key].alignment = Alignment(horizontal = 'center')
        sheet[key].border = Border(bottom=Side(border_style="medium", color="000000"), right=Side(border_style="medium", color="000000"))
        sheet.column_dimensions[key[0]].width = 30
    return True
create_excel('')

