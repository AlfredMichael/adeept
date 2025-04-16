import RPi.GPIO as GPIO
import time

SERVO_PIN = 15  # Your connected GPIO pin

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Create PWM instance (50Hz for servos)
pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(0)

def set_angle(angle):
    duty_cycle = (angle / 18) + 2  # Convert angle to duty cycle (approximation)
    GPIO.output(SERVO_PIN, True)
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)
    GPIO.output(SERVO_PIN, False)
    pwm.ChangeDutyCycle(0)  # Stop sending signal

try:
    while True:
        print("Moving to 0°")
        set_angle(0)  # Move servo to 0°
        time.sleep(1)

        print("Moving to 90°")
        set_angle(90)  # Move servo to 90°
        time.sleep(1)

        print("Moving to 180°")
        set_angle(180)  # Move servo to 180°
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping servo control.")
    pwm.stop()
    GPIO.cleanup()
