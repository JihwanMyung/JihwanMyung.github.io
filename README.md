# LocomotorBox

LocomotorBox is a set of Arduino software and GUI interface for running 10 Locomotor-Boxes with pre-set schedules.

### Prerequisites

The following Arduino software is used: Arduino 1.8.7

The following Python versions are used: Python 3.7.0, Pyserial 3.4

### Installation

Download Arduino .ino file and Python3 .py file. Upload .ino to Arduino microcontroller using Arduino software.
Run Python GUI interface by double-clicking the .py file or on command-line using python3.

## Deployment

This software system requires Arduino Mega 2560 for controlling 10 boxes and a digital slot extension (custom-made). Each box requires 1 PIR sensor (digital input) and 1 relay switch.

## Figure generation guidelines

- Use Helvetica for all figure text.
- Use journal production-grade font sizes so text remains legible after publication scaling.
- Minimize the use of colors.
- Show axes or frames only on the left and bottom.
- Do not use full boxes unless necessary (for example, parameter-space plots).
- Remove frames and axes when a scale bar or scale axes is sufficient.
- Do not add labels inside figures that merely explain what the figure is.
- Keep figures concise and visually minimal.

## Authors

* Jihwan Myung - initial work
* Vuong Truong - further development on Python GUI interface

## Acknowledgments

Yufen (Janice) Huang helped with improving box design. Vuong Truong and Ying-Ling Shen helped with soldering electrical components. Niall Duncan and Tzu-Yu Hsu contributed financially to support initial purchase of boxes and prototyping materials.
This work was supported by Taiwan Ministry of Science and Technology (MOST) grants (107-2311-B-038-001-MY2, 107-2410-H-038-004-MY2).
