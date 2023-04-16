import krpc
from vehicle import Vehicle
import pid

class quadThruster(Vehicle)
    def __init__(self):
        super.__init__(self)
        # Velocity PIDs
        xPID = pid.PID(0.2, 0.5, 0.5, 0, 1)
        yPID = pid.PID(0.2, 0.5, 0.5, 0, 1)
        zPID = pid.PID(0.2, 0.5, 0.5, 0, 1)
        xPID.setPoint = 0
        yPID.setPoint = 0
        zPID.setPoint = 0

    def update(self):
        # use autopilot feature to set the rotation to top dead center
        velocity = self.getVelocity()
        x = velocity[0]
        y = velocity[1]
        z = velocity[2]
        # calculate throttle of each thruster in their space

        # Get PID of X, Y, Z velcocity
        # Calculate the "share" of each thruster in that PID using sin
        # Add to total thrust of that thruster

    def issueCommand(self, commandType, **kwargs):
        pass