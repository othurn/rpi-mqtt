
import GPIO_PWM

red_pin = 17
green_pin = 27
blue_pin = 22
gpio_pins = [red_pin, green_pin, blue_pin]
is_inverted = True

pwm = GPIO_PWM.GPIO_PWM(gpio_pins, is_inverted)

pwm.write(red_pin,127)
