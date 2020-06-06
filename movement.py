import qwiic_scmd
import time
import numpy as np 

class Motor(object):
    def __init__(self):
        super(Motor, self).__init__()

        self.motor = qwiic_scmd.QwiicScmd()
        self.left = 1
        self.right = 0

        self.fwd = 0
        self.bwd = 1

    def begin(self):
        self.motor.begin()
        self.motor.enable()
        self.motor.set_drive(0,0,0)
        self.motor.set_drive(1,0,0)

    def stop(self):
        self.motor.set_drive(0,0,0)
        self.motor.set_drive(1,0,0)

    def kill(self):
        self.motor.disable()
    
    def mv_angle(self, dxL, dxR):
        self.motor.set_drive(self.left, 0, dxL)
        self.motor.set_drive(self.right,0, dxR)

    def turn_right(self, speed):
        self.mv_angle(-speed, speed)

    def turn_left(self, speed):
        self.mv_angle(speed, -speed)

    def forward(self, speed):
        self.mv_angle(speed, speed)

    def backward(self, speed):
        self.mv_angle(-speed, -speed)

    def test_loop(self):
        self.begin()
        for i in range(100):
            self.backward(150)
            time.sleep(0.02)
        # for i in range(20):
        #     self.turn_left(180)
        #     time.sleep(0.02)
        # for i in range(50):
        #     self.forward(160)
        #     time.sleep(0.02)
        # for i in range(20):
        #     self.turn_right(180)
        #     time.sleep(0.02)
        # for i in range(50):
        #     self.backward(160)
        #     time.sleep(0.02)
        self.stop()
