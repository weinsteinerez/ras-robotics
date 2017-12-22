# ras-robotics

This project consists 3 executable .py files.
Redis-server must be up and running (port 6379).

* Pub.py - Gets input from user and publish the msg to INPUT channel
* Sub.py - Imports Listener() object from CalcService and used for printing msgs from OUTPUT channel
* CalcService.py - Runs CalcMsg that listens to msgs in INPUT, do a math logic and publish results to OUTPUT channel

Assumption: 
* A valid input consists a string with 2 operands devided by recognized operator (+,-,*,/). Expression cannot by calculated if it's 
sent in 2 different msgs.
