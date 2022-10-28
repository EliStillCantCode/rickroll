#GOAL: open Chrome and rick roll
import pynput
import time
from pynput.keyboard import Key, Controller
keyboard = Controller()
#
#open windows menu
keyboard.press(Key.cmd_l)
keyboard.press('r')
keyboard.release(Key.cmd_l)
keyboard.release('r')
time.sleep(1)
keyboard.type('chrome')
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
#volume
keyboard.press(Key.media_volume_down)
time.sleep(4)
keyboard.release(Key.media_volume_down)
keyboard.press(Key.media_volume_up)
time.sleep(1)
keyboard.release(Key.media_volume_up)
#rickroll
time.sleep(1)
keyboard.type('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
