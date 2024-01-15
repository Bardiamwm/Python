from charge import Charge
class Phone:
    def __init__(self, model:str, brand:str, color:str, year:int) -> None:
        self.model = model
        self.brand = brand
        self.color = color
        self.year = year
        self.charge = Charge()
        
    def __repr__(self) -> str:
        return f"model: {self.model}\nbrand: {self.brand}\ncolor: {self.color}\nyear: {self.year}"
    
    def chargeChecking(self,  chargeAlarm:int=20, requestedCharge:int=50, fastCharge:bool=True) -> Charge:
        return self.charge.chargingStatus(chargeAlarm, requestedCharge, fastCharge)
    
print(Phone("POCO F3", "Xiaomi", "Blue", 2021).chargeChecking(40, 75))