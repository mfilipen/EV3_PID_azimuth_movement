#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from time import sleep

# devices
sensor = ev3.GyroSensor()
wl = ev3.LargeMotor('outB')
wr = ev3.LargeMotor('outC')
btn = ev3.Button()

# velocity
v = 650;
l=4;
r=1;
k=1;

der=0;
int=0;

def move(angel, kp=5,kd=2,ki=0.05):
    global der, int;

    err = sensor.value() - angel;
    print("alpha", err);

    P = kp * err;

    D = kd * (err - der)
    der = err

    int += err
    I = ki * int

    w=P+I+D;

    vl=(v-w*l)/r;
    vr=(v+w*l)/r;

    if vl>600:
        vl = 650;

    if vr > 650:
        vr = 650;

    if vl < -650:
        vl = -650;

    if vr < -650:
        vr = -650;


    print("vl=", vl);
    print("vr=", vr);

    wl.run_forever(speed_sp=vl)
    wr.run_forever(speed_sp=vr)


angel=sensor.value();

ev3.Sound.speak('I love PID control').wait()
while not btn.any():


    move(angel)
    sleep(0.05);

# stop the program
wl.stop()
wr.stop()