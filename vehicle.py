import krpc
import system



# Base class for all vehicle types
class Vehicle:
    def __init__(self):
        self.vessel = system.getCurrentVessel()
        self.velocity = system.add_stream(self.vessel.velocity, self.vessel.surface_reference_frame)
        self.direction = system.add_stream(self.vessel.direction, self.vessel.surface_reference_frame)
        self.rotation = system.add_stream(self.vessel.rotation, self.vessel.surface_reference_frame)
        pass

    # Return direction as (x, y, z)
    def getDirection(self):
        return self.direction

    #return velocity as (x, y, z)
    def getVelocity(self):
        return self.velocity
    
    def update(self):
        pass

    def issueCommand(self, commandType, **kwargs):
        pass