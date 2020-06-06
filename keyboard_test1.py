import curses
from movement import Motor
import time
from picamera import PiCamera

camera = PiCamera()
camera.iso = 800
camera.framerate = 4
camera.brightness = 55
# camera.shutter_speed = 40000

motor = Motor()
motor.kill()
motor.begin()
motor.stop()

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

def sleep(duration):
    if duration > 0:
        time.sleep(duration)
    else:
        pass

sleep_duration = 0.02

def forward(speed):
    motor.forward(speed)
    sleep(sleep_duration)
    motor.stop()

def backward(speed):
    motor.backward(speed)
    sleep(sleep_duration)
    motor.stop()

def right(speed):
    motor.turn_right(speed)
    sleep(sleep_duration)
    motor.stop()

def left(speed):
    motor.turn_left(speed)
    sleep(sleep_duration)
    motor.stop()

actions = {
    curses.KEY_UP: forward,
    curses.KEY_DOWN: backward,
    curses.KEY_LEFT: left,
    curses.KEY_RIGHT: right,
}
speed = 150
next_key = None
# camera.start_preview()

try:
    while True:
        curses.halfdelay(1)
        if next_key is None:
            key = screen.getch()
        else:
            key = next_key
            next_key = None

        if key == ord("q"):
            break
        elif key != -1:
            curses.halfdelay(1)
            action = actions.get(key)
            if action is not None:
                action(speed)
            next_key = key
            # while next_key == key:
        next_key = screen.getch()
        if next_key == key:
            speed = max(speed+1, 180)
        else:
            speed = 150

finally:
    camera.stop_preview()
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()
    motor.kill()

motor.kill()