from dataclasses import dataclass
from repair import RepairData
from shipment import ShipmentData
@dataclass
class HistoryData:
    ID_repair: RepairData.ID
    ID_shipment: ShipmentData.ID

