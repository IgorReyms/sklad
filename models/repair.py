from dataclasses import dataclass

@dataclass
class RepairData:
    ID: str
    DateOnRepair: str
    Client: str
    ItemQty: int
    Item: str
    DateToClient: str

