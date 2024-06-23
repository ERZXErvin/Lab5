from threading import Thread
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD
from hal import hal_buzzer as buzzer
from time import sleep

correct_pin = ['1', '2', '3', '4']  

password = []

# Initialize LCD
lcd = LCD.lcd()
lcd.lcd_clear()


def key_pressed(key):
    global wrong_attempts
    password.append(key)
    if password == correct_pin:
        lcd.lcd_clear()
        lcd.lcd_display_string("Safe Unlocked", 1)
        lcd.lcd_display_string("", 2)  

    elif len(password) == len(correct_pin):  # Wrong PIN entered
        wrong_attempts += 1
        lcd.lcd_clear()
        lcd.lcd_display_string("Wrong PIN", 1)
        lcd.lcd_display_string("", 2)  # Clear the second line
        # Activate the buzzer for 1 second
        buzzer.turn_on()
        sleep(1)  # Wait for 1 second
        buzzer.turn_off()  # Deactivate the buzzer
        if wrong_attempts == 3:
            lcd.lcd_clear()
            lcd.lcd_display_string("Safe Disabled", 1)
            lcd.lcd_display_string("", 2)  # Clear the second line
            # You can add additional actions here, like disabling access or locking the safe

def main():
    
    lcd.lcd_display_string("Safe Lock", 1)
    lcd.lcd_display_string("Enter PIN: ", 2)

    
    keypad.init(key_pressed)

    # Start the keypad scanning which will run forever in an infinite while(True) loop in a new Thread "keypad_thread"
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()

# Main entry point
if __name__ == "__main__":
    main()