Notes: There is a small amount of support for an LCD Screen such as this one made by Sunfounder (Link Below)
https://www.amazon.com/gp/product/B01GPUMP9C/ref=ppx_yo_dt_b_asin_title_o08_s00?ie=UTF8&psc=1

However the support is minimal it will display a welcome message when script is initialized and after that tell you when a cue is fired and which number 

This software is not based on any dependacies beside what is included in it's root directory and a few python Modules that can be installed with pip3. This means that in the future so long as python is still working
and doesn't remove any modules or compatibility it should work forever.

These are the Modules Needed for this setup:
1. time
2. os
3. eel (as mentioned later in this Readme
4. board
5. busio
6. adafruit_mcp230xx.mcp23017

This software was designed for my needs as I wanted to build a firework launcher. My goal was to come in at about half or very close to half the cost of a
professional grade Launching system. Either that or the radio controlled ones on amazon. However this software can and will run as just a way to control GPIO/GPIO
expansion boards (primarily the MCP23017 based ones which i used). This meaning you could use it for literally anything that you want to control with GPIO on raspberry pi.

If you have any suggestions on modifications to the python code or any of it really. I'm always interedsted to hear new ways to write code especially shorter ones. :)

Contact Info:
Email: zacharykennedy8@gmail.com
      Note: please use "Launcer Project" in the subject if you email me. I rarely check my email but I would be sure to read and write back if I see that.

Also you will need to install eel from pip or this repository to run the backend from the JavaScript to python.
https://github.com/ChrisKnott/Eel


A short proof of concept video:
https://www.youtube.com/shorts/bcxAyih5HK0
