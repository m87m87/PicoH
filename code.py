import board
import digitalio
import time
import adafruit_matrixkeypad

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led7 = digitalio.DigitalInOut(board.GP7)
led7.direction = digitalio.Direction.OUTPUT

cols = [digitalio.DigitalInOut(x) for x in (board.GP13, board.GP6, board.GP5)]
rows = [digitalio.DigitalInOut(x)
        for x in (board.GP21, board.GP20, board.GP26, board.GP19)]
keys = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        ('*', 0, '#'))
# keypad_rows = [board.GP21, board.GP20, board.GP26, board.GP19]
# keypad_columns = [board.GP13, board.GP6, board.GP5]


print("#########################")
print("Enter your two digit pins")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")


keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

guess = []

secrets = [[5], [2], [8], [7]]

def checkPin(guess):
    if guess == secrets:
        print("You got it")
        led.value = True
        time.sleep(10)
        led.value = False
        time.sleep(3)


    else:
        print("Sorry....")
        led7.value = True
        time.sleep(10)
        led7.value = False
        time.sleep(3)


def tfMatrix():
    while True:
        key_p = keypad.pressed_keys
        if key_p:
            print("You pressed : %s "% key_p)
            time.sleep(0.6)
            guess.append(key_p)

        if len(guess) == 4:
            checkPin(guess)
            time.sleep(0.5)

            for x in range(0, 4):
                guess.pop()

tfMatrix()

