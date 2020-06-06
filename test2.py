from movement import Motor
from picamera import PiCamera
from time import sleep

camera = PiCamera()

# camera.start_preview()
# sleep(20)
# camera.stop_preview()

if __name__ == "__main__":

    motor = Motor()

    try:
        motor.kill()
    except:
        pass

    motor.begin()

    motor.test_loop()

    motor.kill()