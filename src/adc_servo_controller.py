from hal import hal_servo as servo

servo()

def read_adc_and_set_servo(adc_value):
    # Map ADC value (0-1023) to servo position (180-0 degrees)
    position = 180 - (adc_value * 180 / 1023)
    servo.set_servo_position(position)

# Main function to initialize and rotate servo based on ADC value
def main():
    servo.init()
    
    while True:
        adc_value = int(input("Enter ADC value (0-1023): "))
            
        if 0 <= adc_value <= 1023:
            read_adc_and_set_servo(adc_value)
        else:
            print("Invalid ADC value. Please enter a value between 0 and 1023.")
    
    

if __name__ == "__main__":
    main()