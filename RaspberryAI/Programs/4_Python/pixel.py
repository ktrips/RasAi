import board
import neopixel

pixels = neopixel.NeoPixel(board.D15, 1)
pixels.fill((255,255,255)) #[0] = (255, 0, 0)

