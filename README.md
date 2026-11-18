# Camera-Controlled Robotic Hand

A personal embedded-systems and computer-vision project that translates hand gestures captured by a webcam into real-time motion of a five-finger robotic hand.

**Project period:** June–August 2026  
**Built with:** Python, OpenCV, MediaPipe, PySerial, Arduino Uno, embedded C++, five servo motors, and TinkerCAD

## Overview

The system tracks a user's hand through a camera and converts finger movements into commands for five individual servo motors. Python processes the camera input and communicates with an Arduino Uno over serial, while Arduino firmware drives the motors.

The goal was to make the physical hand reproduce independent finger motion while keeping movement stable rather than jerky.

## System architecture

```text
Camera / webcam
      |
      v
Python: OpenCV + MediaPipe hand tracking
      |
      v
Finger-state processing and command filtering
      |
      v
PySerial communication
      |
      v
Arduino Uno (embedded C++)
      |
      v
Five servo motors -> robotic hand fingers
```

## What I implemented

- Built a computer-vision pipeline with **OpenCV and MediaPipe** to track hand gestures and translate them into individual finger-control signals
- Connected Python to the **Arduino Uno using PySerial** to transmit commands for real-time actuation
- Applied command filtering/smoothing to reduce unwanted jerky movement
- Programmed **embedded C++ firmware** to drive five servo motors independently
- Designed the robotic-hand mechanism in **TinkerCAD**

## Engineering challenges

**Reliable gesture-to-motion translation:** Webcam-based tracking produces changing inputs, so the software needed to interpret hand states before sending commands to the physical mechanism.

**Stable actuation:** Filtering commands helped prevent rapid, unwanted servo changes while keeping the robotic hand responsive.

**Software/hardware integration:** The project required coordinating the camera-processing pipeline, serial communication, microcontroller firmware, and mechanical finger movement.

## Technology

| Layer | Tools / components |
| --- | --- |
| Computer vision | Python, OpenCV, MediaPipe |
| Host-to-microcontroller communication | PySerial |
| Embedded controller | Arduino Uno, embedded C++ |
| Actuation | Five servo motors |
| Mechanical prototyping | TinkerCAD |

## Demonstration and source code

Project photos, a demonstration, and source files will be added here as they are organized for publication.

> This README describes the completed project. It does not yet include the source files or a reproducible build guide.
