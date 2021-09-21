import random
import time

import RPi.GPIO as GPIO

# Stoplight
# Turn on red, yellow, and green LEDs from a Raspberry Pi like a stoplight


def setup_pins():
    """Setup our pins and board
    """
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(4, GPIO.OUT)  # red
    GPIO.setup(17, GPIO.OUT)  # yellow
    GPIO.setup(27, GPIO.OUT)  # green


def main():
    """Run the stoplight script
    """
    print("Running Stoplight script...")
    setup_pins()

    for i in range(10):
        print(i + 1)
        GPIO.output(4, False)
        GPIO.output(27, True)
        time.sleep(random.randint(1, 3))
        GPIO.output(27, False)
        GPIO.output(17, True)
        time.sleep(0.5)
        GPIO.output(17, False)
        GPIO.output(4, True)
        time.sleep(random.randint(1, 3))

    print("Script complete!")
    GPIO.cleanup()


if __name__ == '__main__':
    main()
