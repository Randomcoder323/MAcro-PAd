import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.rgb import RGB
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP0, board.GP1, board.GP2, board.GP3)
keyboard.row_pins = (board.GP4, board.GP5, board.GP6, board.GP7)
keyboard.diode_orientation = keyboard.DIODE_COL2ROW

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = (
    ((board.GP8, board.GP9),),
    ((board.GP10, board.GP11),),
)

encoder_handler.map = [
    ((KC.VOLD, KC.VOLU),),
    ((KC.LEFT, KC.RIGHT),),
]

rgb = RGB(
    pixel_pin=board.GP12,
    num_pixels=16,
    hue_default=100,
    sat_default=255,
    val_default=100,
)
keyboard.modules.append(rgb)

keyboard.extensions.append(MediaKeys())

keyboard.keymap = [
    [
        KC.COPY, KC.PASTE, KC.CUT, KC.UNDO,
        KC.REDO, KC.S, KC.Z, KC.Y,
        KC.G, KC.R, KC.E, KC.T,
        KC.ESC, KC.ENTER, KC.SPC, KC.TAB
    ]
]

if __name__ == '__main__':
    keyboard.go()
