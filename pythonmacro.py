import keyboard
import time

button = False

print(f"If you want to disable script hold 'o' key until it stops. ")

def press_key_sequence():
    global button
    sequence = [
        ('w', 1), ('d', 1), ('a', 1), ('s', 1),
        ('d', 1), ('s', 1), ('w', 1), ('a', 1),
        ('s', 1), ('a', 1), ('d', 1), ('w', 1),
        ('a', 1), ('w', 1), ('s', 1), ('d', 1)
    ]
    for key, duration in sequence:
        if not keyboard.is_pressed('o'):
            keyboard.press(key)
            time.sleep(duration)
            keyboard.release(key)
        else:
            button = False
            break

while True:
    if keyboard.is_pressed('p'):
        button = True
        time.sleep(0.3)

    if button:
        press_key_sequence()
        print(f"Current script state is {button}")

    time.sleep(0.1)
