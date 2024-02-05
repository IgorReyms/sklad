import json
def config_to_default():
    config = {
        "ExcelFilesQty": 2,
        "Status": "NotInstalled",
        "ExcelPath": '',
        "ExcelFiles":[
        {
            "ExcelFilename": "ИсторияОтправлений",

            "ExcelSheetData": {
                'sheetname':"ИсторияОпераций",
                'data':{
                'A1': '№ Заказа',
                'B1': 'Статус',
                'C1': '№ Отправления',
                'D1': 'Клиент',
                'E1': 'От клиента',
                'F1': 'Дата отправления',
                'G1': 'Клиенту',
                'H1': 'Изделие',
                'I1': 'Количество изделий',
                'J1': 'Комментарий'
                        }
                    }
        },
        {
            "ExcelFilename": "Задолженности",
            "ExcelSheetData": {
                 'sheetname': "ИсторияОпераций",
                 'data': {
                     'A1': '№ Задолженности',
                     'B1': 'Дата создания',
                     'C1': 'Клиент',
                     'D1': 'Изделие',
                     'E1': 'Исходный размер задолженности',
                     'F1': 'Дата последней выдачи',
                     'G1': 'Количество выданных изделий',
                     'H1': 'Остаток по долгу'
                 }
             }
             }
        ],
        "Settings":{
            "repairBtnVisible": True,
            "debtBtnVisible": True,
            "installationBtnVisible": True,
        },
        "RepairInfo":{
          "LastRepairNo": "P-1",
          "LastShipmentNo": "SHIP-1"
        },
        "DebtInfo": {
            "LastDebtNo": "DEBT-1"
        }
    }

    with open('config.json', 'w') as f:
        json.dump(config, f)

config_to_default()
