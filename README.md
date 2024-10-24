# Lego Vernie remote

## Description
This is a Pybricks program to load directly into the lego move hub in order to remote control Vernie from Lego. The program allows you to perform different actions from the remote.

<center><img src="read-me-image.jpg" width="300"></center>

## Features
- Moving Mode: Control Vernie to move front, back, left and right
- Talking Mode: Simulates talking by moving the neck motor (MotorC).
- Dancing Mode: Perform a simple dance routine by moving both wheels in a coordinated pattern.
- Shooting Mode: Activates a motorized shooting action using MotorC.
- Shutdown Mode: Deactivates the robot and prepares for shutdown.
- Shows battery status: Before shothing down the led move hub led will blink green to indicate the level o battery left:
7 times = 7000 (full battery)
6 times = 6000 (still ok)
...
3 times = 3000 (low battery, needs charge)

## Built With
- Python with Pybricks library

## Hardware
- Vernie from Lego Boost
