from time import sleep
from chargingSensor import ChargSensor
class Charge:
    def fastChargeOn(self):
        return "Fast charging started."
        
    def chargeOn(self):
        return "Charging starded."
        
    def chargeOff(self):
        return "Charging stopped."
        
    def chargingStatus(self, chargeAlarm, requestedCharge, fastCharge):
        batteryLevel = ChargSensor().batteryLevel()
        if batteryLevel < chargeAlarm:
            print("battery level is low \U0001F637")
            sleep(0.15)
            print("auto", end=" ")
            sleep(0.15)
            return self.reaachRequestedcharge(batteryLevel, requestedCharge, fastCharge)
        else: return f"Battery level: {batteryLevel}"

    def reaachRequestedcharge(self, batteryLevel, requestedCharge, fastCharge):
        if batteryLevel >= requestedCharge:
            return "your phone is full charge"
        if fastCharge == True:
            self.fastChargeOn()
            while batteryLevel != requestedCharge:
                print(f"Battery level: {batteryLevel}")
                batteryLevel += 1
                sleep(0.25)
        else:
            self.chargeOn()
            while batteryLevel != requestedCharge:
                print(f"Battery level: {batteryLevel}")
                batteryLevel += 1
                sleep(0.5)
        print(f"Battery level: {batteryLevel}")
        return self.chargeOff()