import time

def update_lcd():
    local_time = time.localtime()
    time_string_with_colon = time.strftime("%H:%M:%S", local_time)
    time_string_without_colon = time.strftime("%H %M %S", local_time)
    date_string = time.strftime("%d:%m:%Y", local_time)

    update_lcd_line1(time_string_with_colon)
    update_lcd_line2(date_string)
    time.sleep(1)  
    update_lcd_line1(time_string_without_colon)
    update_lcd_line2(date_string)

def update_lcd_line1(text):
    print("LCD Line 1:", text)

def update_lcd_line2(text):
    print("LCD Line 2:", text)

# Main loop to update LCD every second with blinking colons
while True:
    update_lcd()