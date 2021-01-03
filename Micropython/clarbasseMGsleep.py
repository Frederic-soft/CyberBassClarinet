import machine
import time
import esp32

tp1 = machine.TouchPad(machine.Pin(33))
tp1.config(300)
tp2 = machine.TouchPad(machine.Pin(14))
tp2.config(300)
esp32.wake_on_touch(True)
servo = machine.PWM(machine.Pin(21))
servo.freq(50)
servo.duty(74)
time.sleep_ms(150)
tp = None
# 32 = +90°
# 81 = 0°
# 128 = -90°
while True :
  print("Going to sleep")
  machine.lightsleep()
  print("Waking up")
  if tp1.read() < 300 :
    tp = tp1
    servo.duty(119)
  else:
    tp = tp2
    servo.duty(32)
  
  while tp.read() < 300 :
    time.sleep_ms(10)
  print("Pad released")
  servo.duty(74)
  time.sleep_ms(150)
  # if tp.read() < 300 :
  #   servo.duty(119)
  # else :
  #   servo.duty(74)
  # time.sleep_ms(100)
