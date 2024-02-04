import json
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
            'B1': '№ Отправления',
            'C1': 'Клиент',
            'D1': 'От клиента',
            'E1': 'Дата отправления',
            'F1': 'Клиенту',
            'G1': 'Количество изделий',
            'H1': 'Изделия',
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
      "LastRepairNo": "P-001"
    }
}

with open('config.json', 'w') as f:
    json.dump(config, f)