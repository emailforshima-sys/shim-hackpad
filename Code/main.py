
print("Starting")

import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.display import Display, TextEntry, ImageEntry


keyboard = KMKKeyboard()


keyboard.row_pins = (board.D0, board.D1, board.D2)
keyboard.col_pins = (board.D3, board.D4, board.D5)

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = (
    (board.D6, board.D7),  
)

encoder_handler.map = [
    ((KC.VOL_UP, KC.VOL_DOWN),),
]

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.A, KC.B, KC.C],
    [KC.D, KC.E, KC.F],
    [KC.G, KC.H, KC.I],
]

i2c = busio.I2C(board.SCL, board.SDA)
display = Display(i2c=i2c)
keyboard.extensions.append(display)

if __name__ == '__main__':
    keyboard.go()
