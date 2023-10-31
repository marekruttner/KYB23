from machine import Pin
from time import sleep_ms
from time import ticks_ms

btn = Pin(15, Pin.IN, Pin.PULL_DOWN)

f = open("data.csv", "w")

f.write("time,state\n")

start = ticks_ms()

now = ticks_ms()

while now - start < 10000:
    now = ticks_ms()
    new_state = btn.value()
    f.write(str(now - start),",",str(new_state),"\n")
    sleep_ms(1)
    print(str(now - start), ',', str(new_state), "\n")

f.close()