import krpc
import system



# Base class for all vehicle types
class Vehicle:
    def __init__(self):
        self.vessel = system.getCurrentVessel()
        self.flightInfo 
        pass
    
    def update(self):
        pass

    def issueCommand(self, commandType, **kwargs):
        pass