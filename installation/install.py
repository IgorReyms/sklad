from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Border, Side
import os
from manager.config_manager import ConfigParser
from models.exceptions import CustomException

def install_process(path) -> None:
    create_excel(path)
    create_archive_path(path)



def change_config(path) -> bool:
    config = ConfigParser()
    config.config['ExcelPath'] = path
    return config.save_config()

def create_archive_path(path) -> None:

    if not os.path.exists(path + '/АрхивРемонтов/'):
        os.mkdir(path + '/АрхивРемонтов/')
    else:
        raise CustomException(f"Папка 'АрхивРемонтов' в {path} уже существует!")

    if not os.path.exists(path + '/АрхивЗадолженностей/'):
        os.mkdir(path + '/АрхивЗадолженностей/')
    else:
        raise CustomException(f"Папка 'АрхивЗадолженностей' в {path} уже существует!")
def create_excel(path) -> None:
        if change_config(path):

            config = ConfigParser()
            for count in range(int(config.config["ExcelFilesQty"])):

                xlsx_data = Workbook()
                ws = xlsx_data.active
                ws.title = config.config['ExcelFiles'][count]['ExcelSheetData']['sheetname']
                if configure_excelfile(ws, config.config['ExcelFiles'][count]['ExcelSheetData']['data']):
                    if path.replace(' ','') == '':
                        if os.path.exists(path + config.config['ExcelFiles'][count]["ExcelFilename"] + '.xlsx'):
                            raise CustomException(f"Excel-файл '{config.config['ExcelFiles'][count]['ExcelFilename']}' уже существует в папке {path}! Установите в другую папку! ")
                        xlsx_data.save(path + config.config['ExcelFiles'][count]["ExcelFilename"] + '.xlsx')
                    else:
                        if os.path.exists(path + '/' +config.config['ExcelFiles'][count]["ExcelFilename"] + '.xlsx'):
                            raise CustomException(
                                f"Excel-файл '{config.config['ExcelFiles'][count]['ExcelFilename']}' уже существует в папке {path}! Установите в другую папку! ")
                        xlsx_data.save(path + '/' +config.config['ExcelFiles'][count]["ExcelFilename"] + '.xlsx')
            config.config["Status"] = "Installed"
            config.save_config()
        else:
            raise CustomException(f"Не удалось изменить путь установки в файле конфигурации!")
def configure_excelfile(sheet, sheet_config) -> bool:
    for key in sheet_config:
        sheet[key] = sheet_config[key]
        sheet[key].font = Font(size=12, bold=True)
        sheet[key].alignment = Alignment(horizontal = 'center')
        sheet[key].border = Border(bottom=Side(border_style="medium", color="000000"), right=Side(border_style="medium", color="000000"))
        sheet.column_dimensions[key[0]].width = 30
    return True

# create_excel('')

