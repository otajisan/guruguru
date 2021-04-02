sleep_time = 0

def on_forever():
    global sleep_time
    sleep_time = 100
    while sleep_time >= 0:
        led.plot(2, 2)
        basic.pause(sleep_time)
        sleep_time += -1
        led.plot(3, 3)
        basic.pause(sleep_time)
        sleep_time += -1
        led.plot(2, 4)
        basic.pause(sleep_time)
        sleep_time += -1
        led.plot(1, 4)
        basic.pause(sleep_time)
        sleep_time += -1
        led.plot(0, 3)
        basic.pause(sleep_time)
        sleep_time += -1
        led.plot(0, 2)
        basic.pause(sleep_time)
        sleep_time += -1
        led.plot(0, 1)
        basic.pause(sleep_time)
        sleep_time += -1
        led.plot(1, 0)
        basic.pause(sleep_time)
        sleep_time += -1
        led.plot(2, 0)
        basic.pause(sleep_time)
        sleep_time += -1
        led.plot(3, 0)
        basic.pause(sleep_time)
        sleep_time += -1
        led.plot(4, 1)
        basic.pause(sleep_time)
        sleep_time += -1
        led.plot(4, 2)
        basic.pause(sleep_time)
        sleep_time += -1
        led.plot(4, 3)
        basic.pause(sleep_time)
        sleep_time += -1
        led.unplot(2, 2)
        basic.pause(sleep_time)
        sleep_time += -1
        led.unplot(3, 3)
        basic.pause(sleep_time)
        sleep_time += -1
        led.unplot(2, 4)
        basic.pause(sleep_time)
        sleep_time += -1
        led.unplot(1, 4)
        basic.pause(sleep_time)
        sleep_time += -1
        led.unplot(0, 3)
        basic.pause(sleep_time)
        sleep_time += -1
        led.unplot(0, 2)
        basic.pause(sleep_time)
        sleep_time += -1
        led.unplot(0, 1)
        basic.pause(sleep_time)
        sleep_time += -1
        led.unplot(1, 0)
        basic.pause(sleep_time)
        sleep_time += -1
        led.unplot(2, 0)
        basic.pause(sleep_time)
        sleep_time += -1
        led.unplot(3, 0)
        basic.pause(sleep_time)
        sleep_time += -1
        led.unplot(4, 1)
        basic.pause(sleep_time)
        sleep_time += -1
        led.unplot(4, 2)
        basic.pause(sleep_time)
        sleep_time += -1
        led.unplot(4, 3)
basic.forever(on_forever)
