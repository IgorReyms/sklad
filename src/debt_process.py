import pandas as pd
from manager.config_manager import ConfigParser
from manager.excel_style_manager import setExcelStyling
import datetime
from models.exceptions import CustomException
from src.create_debt_document import on_create
def manage_debt_data(new_data, flag):
    data = read_excel()

    if flag == 1:
        # создание задолженности
        if len(data.loc[(data['№ Задолженности'] == new_data['№ Задолженности'][0]) & (data['Изделие'] == new_data['Изделие'][0])]) > 0:
            data.loc[(data['№ Задолженности'] == new_data['№ Задолженности'][0]) & (data['Изделие'] == new_data['Изделие'][0]), 'Остаток по долгу'] += new_data['Исходный размер задолженности'][0]
            if save_excel(data):
                return True
        string_df = pd.DataFrame.from_dict(new_data)
        data = pd.concat([data, string_df], ignore_index=True)

        if save_excel(data):
            config = ConfigParser()
    elif flag == 2:

        # изменение задолженности
        if len(data.loc[data['№ Задолженности'] == new_data['№ Задолженности'][0]]) != 0:
            if len(data.loc[data['№ Задолженности'] == new_data['№ Задолженности'][0]])== 1:

                if new_data['Количество выданных изделий'][0] == '0' or new_data['Количество выданных изделий'][0] == '':
                    raise CustomException(
                        f"Для задолженности {new_data['№ Задолженности'][0]} не указано количество на выдачу!")

                df_copy = data.copy()
                df_copy[["Количество выданных изделий", "Остаток по долгу"]] =df_copy[["Количество выданных изделий", "Остаток по долгу"]].astype(int)

                df_copy.loc[df_copy['№ Задолженности'] == new_data['№ Задолженности'][0], 'Дата последней выдачи'] =  new_data['Дата последней выдачи'][0]

                df_copy.loc[df_copy['№ Задолженности'] == new_data['№ Задолженности'][0], 'Количество выданных изделий'] = int(new_data['Количество выданных изделий'][0])

                if int(df_copy.loc[df_copy['№ Задолженности'] == new_data['№ Задолженности'][0], 'Остаток по долгу']) - int(new_data['Количество выданных изделий'][0]) < 0:
                    raise CustomException(
                        f"Для задолженности {new_data['№ Задолженности'][0]} отрицательный остаток! Уменьшите количество на выдачу")

                df_copy.loc[df_copy['№ Задолженности'] == new_data['№ Задолженности'][0], 'Остаток по долгу'] = \
                    int(df_copy.loc[df_copy['№ Задолженности'] == new_data['№ Задолженности'][0], 'Остаток по долгу']) - int(new_data['Количество выданных изделий'][0])

            else:
                if new_data['Изделие'][0] == '':
                    raise CustomException(f"Для задолженности {new_data['№ Задолженности'][0]} найдено несколько строк! Укажите название изделия!")
                if new_data['Количество выданных изделий'][0] == '0' or new_data['Количество выданных изделий'][0] == '':
                    raise CustomException(
                        f"Для задолженности {new_data['№ Задолженности'][0]} не указано количество на выдачу!")
                df_copy = data.copy()
                df_copy[["Количество выданных изделий", "Остаток по долгу"]] = df_copy[
                    ["Количество выданных изделий", "Остаток по долгу"]].astype(int)

                df_copy.loc[(df_copy['№ Задолженности'] == new_data['№ Задолженности'][0]) & (df_copy['Изделие'] == new_data['Изделие'][0]), 'Дата последней выдачи'] \
                    =  new_data['Дата последней выдачи'][0]
                df_copy.loc[(df_copy['№ Задолженности'] == new_data['№ Задолженности'][0]) & (df_copy['Изделие'] == new_data['Изделие'][0]), 'Количество выданных изделий'] \
                    =  int(new_data['Количество выданных изделий'][0])
                if int(df_copy.loc[(df_copy['№ Задолженности'] == new_data['№ Задолженности'][0]) & (df_copy['Изделие'] == new_data['Изделие'][0]), 'Остаток по долгу']) - int(new_data['Количество выданных изделий'][0]) < 0:
                    raise CustomException(
                                        f"Для задолженности {new_data['№ Задолженности'][0]} отрицательный остаток! Уменьшите количество на выдачу")
                df_copy.loc[(df_copy['№ Задолженности'] == new_data['№ Задолженности'][0]) & (df_copy['Изделие'] == new_data['Изделие'][0]), 'Остаток по долгу'] = \
                    int(df_copy.loc[(df_copy['№ Задолженности'] == new_data['№ Задолженности'][0]) & (df_copy['Изделие'] == new_data['Изделие'][0]), 'Остаток по долгу']) - int(new_data['Количество выданных изделий'][0])

            if save_excel(df_copy):
                return True
        else:
            raise CustomException(f'Задолженность {new_data["№ Задолженности"][0]} не найдена! Проверьте правильность номера задолженности!')



    elif flag == 3:
        # поиск задолженности
        filters = {'№ Задолженности':'', 'Клиент':'','Изделие':'','Дата последней выдачи':'' }
        filter_level = 4
        if new_data["№ Задолженности"][0] != '':
           filters["№ Задолженности"] = new_data["№ Задолженности"][0]
        else:
            filter_level -= 1

        if new_data['Клиент'][0] != '':
            filters['Клиент'] = new_data['Клиент'][0]
        else:
            filter_level -= 1

        if new_data['Изделие'][0] != '':
            filters['Изделие'] = new_data['Изделие'][0]
        else:
            filter_level -= 1

        if new_data['Дата последней выдачи'][0] != '':
            filters['Дата последней выдачи'] = new_data['Дата последней выдачи'][0]
        else:
            filter_level -= 1

        if filter_level == 0:
            raise CustomException("Поля фильтра пустые! Заполните хотя бы 1 поле!")
        else:
            df_copy = data.copy()
            for key in filters:
                if filters[key] != '':
                    df_copy = df_copy.loc[(df_copy[key] == filters[key]) & (df_copy['Остаток по долгу'] != 0)]

            df_copy = df_copy[['№ Задолженности','Клиент','Остаток по долгу','Изделие']]

            cols = [column for column in df_copy]
            answer = ''
            col_print_width = 40
            answer += str(cols[0]) + ' '*(col_print_width-len(cols[0])) + str(cols[1]) + ' '*(col_print_width-len(cols[1])) + str(cols[2]) + ' '*(col_print_width-len(cols[2])) + str(cols[3]) + ' '*(col_print_width-len(cols[3]))

            answer +='\n'

            indexes = []
            for col in cols:
                indexes.append(answer.find(col))

            for index, row in df_copy.iterrows():

                answer += str(row['№ Задолженности']) + ' '*(indexes[1] +  len('№ Задолженности') - len(str(row['№ Задолженности'])))\
                          + str(row['Клиент']) + ' '*(indexes[2]  - indexes[1] +  len('Клиент') - len(str(row['Клиент'])) )\
                          + str(row['Остаток по долгу']) + ' '*(indexes[3] - indexes[2] + len('Остаток по долгу') - len(str(row['Остаток по долгу'])))\
                          + str(row['Изделие'])  + '\n'


            return answer

    elif flag == 4:
        config = ConfigParser()
        df_copy = data.loc[data["№ Задолженности"] == new_data['№ Задолженности'][0]]
        if df_copy.empty:
            raise CustomException(f'Задолженность {new_data["№ Задолженности"][0]} не найдена! Проверьте номер задолженности!')
        df_copy = df_copy.to_dict("list")

        pdf_data = {
            'ExcelPath': config.config["ExcelPath"],
            'Дата': df_copy['Дата создания'][0],
            'Клиент': df_copy["Клиент"][0],
            '№ Заказа': df_copy['№ Задолженности'][0],
            'Изделие': df_copy["Изделие"],
            'Количество': df_copy['Исходный размер задолженности']
        }
        on_create(pdf_data)
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