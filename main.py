import pid 
import system
import time


def main():
    print(system.getTime())
    print(system.getVersion())

    hoverPID = pid.PID(0.2,0.5,0.5,0,1)
    xPID = pid.PID(0.2, 0.5, 0.5, 0, 1)
    yPID = pid.PID(0.2, 0.5, 0.5, 0, 1)
    zPID = pid.PID(0.2, 0.5, 0.5, 0, 1)

    rPID = pid.PID(0.5, 0.5, 0.2, -1, 1)
    rPID.setPoint = 0

    vessel = system.getCurrentVessel()

    flightInfo = vessel.flight()

    targetaltitude = 10
    hoverPID.setPoint = targetaltitude

    controls = vessel.control
    time.sleep(40/1000)

    while(True):
        currentAltitude = flightInfo.surface_altitude

        controls.throttle = hoverPID.update(currentAltitude)

        #controls.roll = rPID.update(flightInfo.roll)
        print(rPID.components)

        time.sleep(40/1000)




main()