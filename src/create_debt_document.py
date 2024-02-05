from fpdf import FPDF

import fpdf
from pathlib import Path
import os
def create_pdf(data)->None:
    pdf = FPDF()
    pdf.add_page(orientation='L')

    delta_copy = pdf.w / 4
    path = os.getcwd()

    pdf.image(path + '\\' + '1.jpg', x=10, y=10, w=50, h=12)
    pdf.image(path + '\\' + '1.jpg', x=pdf.w / 2 + 10, y=10, w=50, h=12)

    pdf.add_font('gothampro', '', path + '\\' + 'GothamPro.ttf', uni=True)
    pdf.set_font('gothampro', '', 12)
    pdf.line(pdf.w / 2, pdf.h / 10, pdf.w / 2, pdf.h - pdf.h / 10)
    # pdf.set_font('times','',12)
    pdf.cell(pdf.w * 1 / 4, pdf.font_size, txt='')
    pdf.cell(pdf.w * 1 / 4, pdf.font_size * 2, txt='Тел.: 8(495)580-37-61;')
    pdf.cell(pdf.w * 1 / 4, pdf.font_size, txt='')
    pdf.cell(pdf.w * 1 / 4, pdf.font_size * 2, txt='Тел.: 8(495)580-37-61;')
    pdf.ln(5)

    pdf.cell(pdf.w * 1 / 4, pdf.font_size, txt='')
    pdf.cell(pdf.w * 1 / 4, pdf.font_size * 2, txt='8(495)241-30-85;')
    pdf.cell(pdf.w * 1 / 4, pdf.font_size, txt='')
    pdf.cell(pdf.w * 1 / 4, pdf.font_size * 2, txt='8(495)241-30-85;')
    pdf.ln(50)

    pdf.cell(pdf.w / 2 - 30, pdf.font_size, txt=f'{data["Дата"]}/{data["№ Заказа"]}/ДОЛГ', align='R')
    pdf.cell(30, pdf.font_size, txt='')
    pdf.cell(pdf.w / 2 - 30, pdf.font_size, txt=f'{data["Дата"]}/{data["№ Заказа"]}/ДОЛГ', align='R')
    pdf.ln(pdf.font_size * 2)

    pdf.add_font('gothampro_bold', '', path + '\\' + 'GothamPro-Bold.ttf', uni=True)
    pdf.set_font('gothampro_bold', '', 16)
    # pdf.set_font('times', '', 16)
    pdf.cell(pdf.w / 2, pdf.font_size, txt=str(data["Клиент"]), align='C')
    pdf.cell(pdf.w / 2, pdf.font_size, txt=str(data["Клиент"]), align='C')
    pdf.ln(pdf.font_size + 5)

    pdf.add_font('gothampro_bold', '', path + '\\' + 'GothamPro-Bold.ttf', uni=True)
    pdf.set_font('gothampro_bold', '', 8)
    # pdf.set_font('times', '', 8)
    name_size = pdf.w / 4
    quantity_size = pdf.w / 6

    cell_height = pdf.font_size * 1.2

    pdf.cell(name_size, cell_height, txt='Название', align='C', border=1)
    pdf.cell(quantity_size, cell_height, txt='Количество, шт.', align='C', border=1)


    pdf.cell((pdf.w / 2 - name_size - quantity_size), txt='')

    pdf.cell(name_size, cell_height, txt='Название', align='C', border=1)
    pdf.cell(quantity_size, cell_height, txt='Количество, шт.', align='C', border=1)

    pdf.ln(cell_height)

    pdf.add_font('gothampro', '', path + '\\' + 'GothamPro.ttf', uni=True)
    pdf.set_font('gothampro', '', 8)
    # pdf.set_font('times', '', 8)

    name = data['Изделие']
    quantity = data['Количество']


    for index, elem in enumerate(name):

        strings = pdf.multi_cell(name_size, cell_height, txt=elem, border=1, split_only=True)


        x1 = pdf.get_x()
        y1 = pdf.get_y()
        pdf.multi_cell(name_size, cell_height, txt=elem, border=1)

        pdf.set_y(y1)
        pdf.set_x(x1 + name_size)

        pdf.cell(quantity_size, cell_height * len(strings), txt=str(int(quantity[index])), border=1)



        pdf.cell((pdf.w / 2 - name_size - quantity_size ), txt='')

        x = pdf.get_x()
        y = pdf.get_y()
        pdf.multi_cell(name_size, cell_height, txt=elem, border=1)


        pdf.set_y(y)
        pdf.set_x(x + name_size)

        pdf.cell(quantity_size, cell_height * len(strings), txt=str(int(quantity[index])), border=1)


        pdf.ln(cell_height * len(strings))

    try:
        str_save = data['ExcelPath'] + '/АрхивЗадолженностей/Форма_по_долгу_' + str(data["№ Заказа"]) + '.pdf'
        pdf.output(str_save)
    except Exception as e:
        print(e.__str__())
    os.system(data['ExcelPath'] + f'/АрхивЗадолженностей/Форма_по_долгу_{data["№ Заказа"]}.pdf')
def on_create(pdf_data):
    create_pdf(pdf_data)