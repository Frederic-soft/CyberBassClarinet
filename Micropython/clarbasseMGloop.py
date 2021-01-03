import machine
import time
import esp32
import sys

# rest angle
rest = 70
# low D angle (pad 1)
lowD = 100
# c# angle (pad 2)
csharp = 40

# capa threshold
cthres = 260

tp1 = machine.TouchPad(machine.Pin(33))
tp1.config(cthres)
tp2 = machine.TouchPad(machine.Pin(14))
tp2.config(cthres)
# esp32.wake_on_touch(True)
servo = machine.PWM(machine.Pin(21))
servo.freq(50)
servo.duty(rest)
# time.sleep_ms(150)
tp = None
# 32 = +90°
# 81 = 0°
# 128 = -90°
# Stop if pin 5 is grounded (allows pyrshell to take control over the board)
stop = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)
if stop.value() == 0 :
  print("Pin 5 is grounded, stopping.")
  sys.exit(0)

while True :
#  print("Going to sleep")
#  machine.lightsleep()
#  print("Waking up")
  while not (tp1.read() < cthres or tp2.read() < cthres) :
    time.sleep_ms(50)

  if tp1.read() < cthres :
#    print("Pad 1 touched")
    tp = tp1
    servo.duty(lowD)
  else:
#    print("Pad 2 touched")
    tp = tp2
    servo.duty(csharp)
  
  while tp.read() < cthres :
    time.sleep_ms(50)
#  print("Pad released")
  servo.duty(rest)
  time.sleep_ms(50)
