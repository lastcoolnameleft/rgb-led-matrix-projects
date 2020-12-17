import gc
import time
import math
import json
import board
import busio
import displayio
import terminalio
from adafruit_matrixportal.matrixportal import MatrixPortal

BITPLANES = 6      # Ideally 6, but can set lower if RAM is tight
MATRIX = MatrixPortal(status_neopixel=board.NEOPIXEL, debug=True, bit_depth=BITPLANES)
DISPLAY = MATRIX.display
FILENAME = '/bmps/TheLab.bmp'
FILENAME2 = '/bmps/richIQ.bmp'

# Create a new label with the color and text selected
MATRIX.add_text(
    text_font=terminalio.FONT,
    text_position=(0, (MATRIX.graphics.display.height // 2) - 1),
    scrolling=True,
    text_scale=2,
)

# Static 'Connecting' Text
MATRIX.add_text(
    text_font=terminalio.FONT,
    text_position=(2, (MATRIX.graphics.display.height // 2) - 1),
    text_scale=2,
)

contents = [
    { 'text': 'Welcome Richardson IQ!',  'color': '#0846e4'},
]

SCROLL_DELAY = 0.01

while True:
    MATRIX.set_background(FILENAME)
    time.sleep(5)
    MATRIX.set_background(0x0)
    MATRIX.set_background(FILENAME2)
    time.sleep(5)
    MATRIX.set_background(0x0)
    for content in contents:
        MATRIX.set_text(content['text'])

        # Set the text color
        MATRIX.set_text_color(content['color'])

        # Scroll it
        MATRIX.scroll_text(SCROLL_DELAY)
