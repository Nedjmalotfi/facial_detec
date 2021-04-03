from pyfirmata import Arduino, util
from time import sleep

arduino = "COM8"
board = Arduino(arduino)

for _ in range(100):
    board.digital[13].write(1)
    sleep(0.5)
    board.digital[13].write(0)
    sleep(0.5)