from config_manager import ConfigParser
import pandas as pd
def update_repair_page(window, flag):
    config = ConfigParser()

    if flag == 'create_repair':
        last_no = config.config["RepairInfo"]["LastRepairNo"]
        new_no = create_new_repair_no(last_no)
        config.config["RepairInfo"]["LastRepairNo"] = new_no
        config.save_config()

        count_list = update_repair_info()
        window.ui.RepairQtyUnShipInfoTextEdit.setPlainText(str(count_list[0]))
        window.ui.RepairQtyShipInfoTextEdit.setPlainText(str(count_list[1]))
        window.ui.RepairQtyInfoTextEdit.setPlainText(str(count_list[2]))
        window.ui.RepairClientTextEdit.clear()
        window.ui.RepairNoInTextEdit.setPlainText(config.config["RepairInfo"]["LastRepairNo"])
        window.ui.TableRepairDocField.setRowCount(0)

    elif flag == 'create_shipment':
        last_no = config.config["RepairInfo"]["LastShipmentNo"]
        new_no = create_new_repair_shipment_no(last_no)
        config.config["RepairInfo"]["LastShipmentNo"] = new_no
        config.save_config()

        count_list = update_repair_info()
        window.ui.RepairQtyUnShipInfoTextEdit.setPlainText(str(count_list[0]))
        window.ui.RepairQtyShipInfoTextEdit.setPlainText(str(count_list[1]))
        window.ui.RepairQtyInfoTextEdit.setPlainText(str(count_list[2]))

        window.ui.ShipmentNoTextEdit.clear()
        window.ui.ShipmentNoTextEdit.setPlainText(config.config["RepairInfo"]["LastShipmentNo"])

    elif flag == 'repair_to_client':
        count_list = update_repair_info()
        window.ui.RepairQtyUnShipInfoTextEdit.setPlainText(str(count_list[0]))
        window.ui.RepairQtyShipInfoTextEdit.setPlainText(str(count_list[1]))
        window.ui.RepairQtyInfoTextEdit.setPlainText(str(count_list[2]))

        window.ui.RepairNoOutTextEdit.clear()
    elif flag == 'repair_status_info':
        count_list = update_repair_info()
        window.ui.RepairQtyUnShipInfoTextEdit.setPlainText(str(count_list[0]))
        window.ui.RepairQtyShipInfoTextEdit.setPlainText(str(count_list[1]))
        window.ui.RepairQtyInfoTextEdit.setPlainText(str(count_list[2]))

def create_new_repair_shipment_no(last_no) -> str:
    last_no = last_no.split("-")
    new_no = last_no[0] + '-' + str(int(last_no[1]) + 1)
    return new_no
def create_new_repair_no(last_no) -> str:
    last_no = last_no.split("-")
    new_no = last_no[0] + '-' + str(int(last_no[1]) + 1)
    return new_no
def get_full_path() -> str:
    config = ConfigParser()
    path = config.config["ExcelPath"]
    filename = config.config["ExcelFiles"][0]["ExcelFilename"] + '.xlsx'
    full_path = path + '/' + filename
    return full_path
def update_repair_info() -> list:
    repair_data = pd.read_excel(get_full_path())
    count_all = len(repair_data)
    filtered_df = repair_data[(repair_data['Статус'] == 'Не отправлено')]
    count_bad = len(filtered_df)
    filtered_df = repair_data[(repair_data['Статус'] == 'Отправлено')]
    count_good = len(filtered_df)
    return [count_bad, count_good, count_all]

