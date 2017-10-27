# EV3 azimuth movement with PID controller

### Description of the project
This project is designed to provide azimuth movement with gyroscope sensor for Lego Mindstorm differential drive robot. Sensor provides information about current angel at each iteration, after that it is comparing with desired angel (which was set as angel in initial moment). Information about diifference in desired and curent angels is used for update speed of rotation. And finaly, rotation speed translates to control comands for actuators of the EV3 robot. It used PID controller for smooth and stable movement.

### Description of the work process
[Ev3dev](http://www.ev3dev.org/) was used as operating system. For make ready your robot please follow this instruction [ev3dev Getting Started guide](http://www.ev3dev.org/docs/getting-started/). Python was used as programming language. It becomes possible with [ev3dev-lang-python](https://github.com/ev3dev/ev3dev-lang-python) which is alredy instaled in Ev3dev. Use [this instruction](https://github.com/ev3dev/ev3dev-lang-python/blob/develop/README.rst) to make it run with simple commands. Bluetooth  connection was used for communication with robot how it was described [here](http://www.ev3dev.org/docs/tutorials/connecting-to-the-internet-via-bluetooth/). Finally use SSH for run scripts on you robot.

### Problems
Gyroscope sensor drift indefinitely.
The value sending by sensor is changing without any robot movements.
Solution: Make sure all wires are firmly connected. Reebot system. Try to change conection slot for sensor.

Gyroscope sensor drift on constant. Sometimes after hard impact on robot value showing by sensor can shift on some constant. Solution: Try to be more gently with robot during to test runs.

Robot moves to slow. Solution: set constant speed at maximum. It is about 656.

Robot moves with unevenly with jerks. Solution: use appropriate constants for PID controller.

### Explanation of the result values
The constans for PID controoler was choosen during realworld test process. The transition process was evaluated by the characteristic features of this process (respons time, overshooting, stady error).  

### Explanation why this values are the best
This value was estimated based on my sense of beauty. Proportional coefficient - responsible for response time and overshooting. it was set big (relative to another coefficient) for good response time. After that we should work with overshoot problem. Differential coefficient helps with this problem. It was seasoned to good enough stabilize overshoot. And last integral coefficient was chosen experimentally. It's responsible to compensate the steady state error but it save error.

### link to youtube video
[Video of working setup on Youtube](https://youtu.be/Wj7KsnlTIb0). 



