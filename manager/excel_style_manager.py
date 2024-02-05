
from openpyxl import load_workbook
from openpyxl.styles import Font, Alignment, Border, Side
from models.exceptions import CustomException
def setExcelStyling(full_path, sheet_config):
    wb = load_workbook(full_path)

    sheet = wb.active
    for key in sheet_config:
        sheet[key] = sheet_config[key]
        sheet[key].font = Font(size=12, bold=True)
        sheet[key].alignment = Alignment(horizontal = 'center')
        sheet[key].border = Border(bottom=Side(border_style="medium", color="000000"), right=Side(border_style="medium", color="000000"))
        sheet.column_dimensions[key[0]].width = 30
    wb.save(full_path)
    return True