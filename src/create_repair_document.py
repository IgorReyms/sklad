#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fpdf import FPDF

import fpdf
from pathlib import Path
import os
import shutil
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

    pdf.cell(pdf.w/2 - 30, pdf.font_size,txt = f'{data["Дата"]}/{data["№ Заказа"]}/РЕМОНТ', align='R')
    pdf.cell(30, pdf.font_size, txt = '')
    pdf.cell(pdf.w/2 - 30, pdf.font_size, txt=f'{data["Дата"]}/{data["№ Заказа"]}/РЕМОНТ', align='R')
    pdf.ln(pdf.font_size*2)


    pdf.add_font('gothampro_bold', '', path + '\\' + 'GothamPro-Bold.ttf', uni=True)
    pdf.set_font('gothampro_bold', '', 16)
    # pdf.set_font('times', '', 16)
    pdf.cell(pdf.w / 2, pdf.font_size, txt=str(data["Клиент"]), align='C')
    pdf.cell(pdf.w / 2, pdf.font_size, txt=str(data["Клиент"]), align='C')
    pdf.ln(pdf.font_size + 5)

    pdf.add_font('gothampro_bold', '', path + '\\' + 'GothamPro-Bold.ttf', uni=True)
    pdf.set_font('gothampro_bold', '', 8)
    # pdf.set_font('times', '', 8)
    name_size = pdf.w / 8
    quantity_size = pdf.w / 12
    comment_size = pdf.w / 4
    cell_height = pdf.font_size *1.2

    pdf.cell(name_size, cell_height, txt='Название', align='C', border=1)
    pdf.cell(quantity_size, cell_height, txt='Количество, шт.', align='C', border=1)
    pdf.cell(comment_size, cell_height, txt='Комментарий', align='C', border=1)

    pdf.cell((pdf.w / 2 - name_size - quantity_size - comment_size), txt='')

    pdf.cell(name_size, cell_height, txt='Название', align='C', border=1)
    pdf.cell(quantity_size, cell_height, txt='Количество, шт.', align='C', border=1)
    pdf.cell(comment_size, cell_height, txt='Комментарий', align='C', border=1)
    pdf.ln(cell_height)

    pdf.add_font('gothampro', '', path + '\\' + 'GothamPro.ttf', uni=True)
    pdf.set_font('gothampro', '', 8)
    # pdf.set_font('times', '', 8)

    name = data['Изделие']
    quantity = data['Количество']
    comment = data['Комментарий']



    for index, elem in enumerate(name):


        strings = pdf.multi_cell(name_size, cell_height, txt=elem, border=1,  split_only=True)
        flag = True

        if len(strings)*2 <= len(pdf.multi_cell(comment_size, cell_height, txt=comment[index], border=1,  split_only=True)):
            strings = pdf.multi_cell(name_size, cell_height, txt=comment[index], border=1,  split_only=True)
            flag = False


        x1 = pdf.get_x()
        y1 = pdf.get_y()
        if flag == True:
            pdf.multi_cell(name_size, cell_height, txt=elem, border=1)
        else:
            pdf.multi_cell(name_size, cell_height * len(strings), txt=elem, border=1)

        pdf.set_y(y1)
        pdf.set_x(x1 + name_size)

        pdf.cell(quantity_size, cell_height * len(strings), txt=quantity[index], border=1)

        x2 = pdf.get_x()
        y2 = pdf.get_y()
        if flag == True:
            pdf.multi_cell(comment_size,cell_height * len(strings), txt=comment[index], border=1 )
        else:
            pdf.multi_cell(comment_size, cell_height , txt=comment[index], border=1)
        pdf.set_y(y2)
        pdf.set_x(x2 + comment_size)



        pdf.cell((pdf.w / 2 - name_size - quantity_size - comment_size), txt='')

        x = pdf.get_x()
        y = pdf.get_y()
        if flag == True:
            pdf.multi_cell(name_size, cell_height, txt=elem, border=1)
        else:
            pdf.multi_cell(name_size, cell_height*len(strings), txt=elem, border=1)

        pdf.set_y(y)
        pdf.set_x(x + name_size)

        pdf.cell(quantity_size, cell_height * len(strings), txt=quantity[index], border=1)

        x = pdf.get_x()
        y = pdf.get_y()
        if flag == True:
            pdf.multi_cell(comment_size, cell_height * len(strings), txt=comment[index], border=1)
        else:
            pdf.multi_cell(comment_size, cell_height , txt=comment[index], border=1)
        pdf.set_y(y)
        pdf.set_x(x + name_size)
        pdf.ln(cell_height * len(strings))

    try:
        # str_save = data['ExcelPath'] + '/АрхивРемонтов/Накладная_по_ремонту_' + str(data["№ Заказа"]) + '.pdf'
        str_save = 'Накладная_по_ремонту_' + str(data["№ Заказа"]) + '.pdf'
        pdf.output(str_save)

        shutil.move('Накладная_по_ремонту_' + str(data["№ Заказа"]) + '.pdf',
                    data['ExcelPath'] + '/АрхивРемонтов/Накладная_по_ремонту_' + str(data["№ Заказа"]) + '.pdf')

        os.system(data['ExcelPath'] + f'/АрхивРемонтов/Накладная_по_ремонту_{data["№ Заказа"]}.pdf')

    except Exception as e:
        print(e.__str__())

def on_create(pdf_data):
    create_pdf(pdf_data)

