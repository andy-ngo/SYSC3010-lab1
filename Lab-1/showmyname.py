from sense_hat import SenseHat
sense = SenseHat()

cyan = (0,255,255)
magenta = (255,0,255)

while True:
    sense.show_message("Andy Ngo",text_colour = cyan, back_colour = magenta,scroll_speed = 0.1)


