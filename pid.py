''' 
PID Library for KRPC
'''
import system

class PID:
    def __init__(self, Kp, Ki, Kd, cMin, cMax):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.cMin = cMin
        self.cMax = cMax
        self.setpoint = 0
        self.lastOutput = 0
        self.lastInput = None
        self.lastTime = system.getTime()

        self.proportional = 0
        self.integral = 0
        self.derivative = 0

    def clamp(self, value):
        if value > self.cMax:
            return self.cMax
        elif value < self.cMin:
            return self.cMin
        else:
            return value

    def update(self, input_):
        error = self.setpoint - input_
        now = system.getTime()
        dt = now - self.lastTime

        d_input = input_ - (self.lastInput if (self.lastInput is not None) else input_)
        self.proportional = self.Kp * error 
        self.integral += self.Ki * error * dt
        self.integral = self.clamp(self.integral)
        self.derivative = -self.Kd * d_input / dt

        output = self.proportional + self.integral + self.derivative
        output = self.clamp(output)

        self.lastInput = input_
        self.lastOutput = output
        self.lastTime = now

        return output

    @property 
    def components(self):
        return self.proportional, self.integral, self.derivative

    @property
    def setPoint(self):
        return self.setpoint

    @setPoint.setter
    def setPoint(self, s):
        self.setpoint = s;

    @property
    def tunings(self):
        return self.Kp, self.Ki, self.Kd

    @tunings.setter
    def tunings(self, tunings):
        self.Kp, self.Ki, self.Kd = tunings

    @property
    def outputLimits(self):
        return self.cMin, self.cMax

    @outputLimits.setter
    def outputLimits(self, limits):
        if limits is None:
            raise ValueError("Can't set no limits")

        minOutput, maxOutput = limits

        if (None not in limits) and (maxOutput < minOutput):
            raise ValueError('lower limit must be less than upper limit')

        self.cMin = minOutput
        self.cMax = maxOutput

        self._integral = self.clamp(self._integral)
        self._last_output = self.clamp(self.lastOutput)